from __future__ import annotations

import argparse
import json
from pathlib import Path

from .batch import run_report_batch
from .checklists import CHECKLISTS, render_checklist
from .health import evaluate_health
from .init_manifest import write_manifest_template
from .models import ProjectManifest
from .reports import render_health_report
from .roadmap import render_roadmap
from .scaffold import scaffold_templates
from .survey import render_survey_summary
from .tasks import render_tasks_markdown
from .validation import validate_example_manifests


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="osbk",
        description="Tools for practical open-source project maintenance.",
    )
    subparsers = parser.add_subparsers(required=True)

    health = subparsers.add_parser("health", help="Score a project manifest.")
    health.add_argument("manifest", type=Path)
    health.add_argument("--json", action="store_true", help="Print machine-readable health output.")
    health.set_defaults(func=_health)

    init = subparsers.add_parser("init-manifest", help="Create a starter project manifest.")
    init.add_argument("--name", required=True)
    init.add_argument("--repository", required=True)
    init.add_argument("--description", required=True)
    init.add_argument("--license", default="MIT", dest="license_name")
    init.add_argument("--output", "-o", type=Path, required=True)
    init.add_argument("--overwrite", action="store_true")
    init.set_defaults(func=_init_manifest)

    report = subparsers.add_parser("report", help="Generate a Markdown health report.")
    report.add_argument("manifest", type=Path)
    report.add_argument("--output", "-o", type=Path)
    report.set_defaults(func=_report)

    batch = subparsers.add_parser("batch-report", help="Generate reports for every job in a batch file.")
    batch.add_argument("batch_file", type=Path)
    batch.add_argument("--output-dir", "-o", type=Path)
    batch.set_defaults(func=_batch_report)

    checklist = subparsers.add_parser("checklist", help="Print a maintainer checklist.")
    checklist.add_argument("kind", choices=sorted(CHECKLISTS))
    checklist.add_argument("--output", "-o", type=Path)
    checklist.set_defaults(func=_checklist)

    tasks = subparsers.add_parser("tasks", help="Suggest contributor tasks from health gaps.")
    tasks.add_argument("manifest", type=Path)
    tasks.add_argument("--limit", type=int)
    tasks.add_argument("--output", "-o", type=Path)
    tasks.set_defaults(func=_tasks)

    roadmap = subparsers.add_parser("roadmap", help="Generate a maintainer roadmap from health gaps.")
    roadmap.add_argument("manifest", type=Path)
    roadmap.add_argument("--output", "-o", type=Path)
    roadmap.set_defaults(func=_roadmap)

    survey = subparsers.add_parser("survey-summary", help="Summarize maintainer survey CSV data.")
    survey.add_argument("survey_csv", type=Path)
    survey.add_argument("--output", "-o", type=Path)
    survey.set_defaults(func=_survey_summary)

    scaffold = subparsers.add_parser("scaffold", help="Copy community templates into a project.")
    scaffold.add_argument("destination", type=Path)
    scaffold.add_argument("--overwrite", action="store_true")
    scaffold.set_defaults(func=_scaffold)

    validate = subparsers.add_parser(
        "validate-examples", help="Validate that example manifests load and score."
    )
    validate.add_argument("--root", type=Path, default=Path("examples/project-profiles"))
    validate.set_defaults(func=_validate_examples)

    return parser


def _health(args: argparse.Namespace) -> int:
    manifest = ProjectManifest.from_file(args.manifest)
    result = evaluate_health(manifest)
    if args.json:
        print(
            json.dumps(
                {
                    "name": manifest.name,
                    "repository": manifest.repository,
                    "score": result.score,
                    "grade": result.grade,
                    "present": result.present,
                    "missing": result.missing,
                    "recommendations": result.recommendations,
                },
                indent=2,
            )
        )
        return 0

    print(f"{manifest.name}: {result.score}/100 ({result.grade})")
    if result.missing:
        print("\nMissing signals:")
        for signal in result.missing:
            print(f"- {signal}")
    return 0


def _init_manifest(args: argparse.Namespace) -> int:
    output = write_manifest_template(
        output=args.output,
        name=args.name,
        repository=args.repository,
        description=args.description,
        license_name=args.license_name,
        overwrite=args.overwrite,
    )
    print(f"Wrote {output}")
    return 0


def _report(args: argparse.Namespace) -> int:
    manifest = ProjectManifest.from_file(args.manifest)
    report = render_health_report(manifest)
    _write_or_print(report, args.output)
    return 0


def _batch_report(args: argparse.Namespace) -> int:
    results = run_report_batch(args.batch_file, output_dir=args.output_dir)
    print("Wrote batch reports:")
    for result in results:
        print(f"- {result.project_slug}: {result.output}")
    return 0


def _checklist(args: argparse.Namespace) -> int:
    checklist = render_checklist(args.kind)
    _write_or_print(checklist, args.output)
    return 0


def _tasks(args: argparse.Namespace) -> int:
    manifest = ProjectManifest.from_file(args.manifest)
    tasks = render_tasks_markdown(manifest, limit=args.limit)
    _write_or_print(tasks, args.output)
    return 0


def _roadmap(args: argparse.Namespace) -> int:
    manifest = ProjectManifest.from_file(args.manifest)
    roadmap = render_roadmap(manifest)
    _write_or_print(roadmap, args.output)
    return 0


def _survey_summary(args: argparse.Namespace) -> int:
    summary = render_survey_summary(args.survey_csv)
    _write_or_print(summary, args.output)
    return 0


def _scaffold(args: argparse.Namespace) -> int:
    written = scaffold_templates(args.destination, overwrite=args.overwrite)
    if written:
        print("Wrote:")
        for path in written:
            print(f"- {path}")
    else:
        print("No files written. Use --overwrite to replace existing files.")
    return 0


def _validate_examples(args: argparse.Namespace) -> int:
    results = validate_example_manifests(args.root)
    print("Validated example manifests:")
    for result in results:
        print(f"- {result.project_name}: {result.score}/100 ({result.path})")
    return 0


def _write_or_print(content: str, output: Path | None) -> None:
    if output is None:
        print(content)
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(f"Wrote {output}")
