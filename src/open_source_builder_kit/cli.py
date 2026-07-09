from __future__ import annotations

import argparse
from pathlib import Path

from .batch import run_report_batch
from .checklists import CHECKLISTS, render_checklist
from .health import evaluate_health
from .models import ProjectManifest
from .reports import render_health_report
from .scaffold import scaffold_templates


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
    health.set_defaults(func=_health)

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

    scaffold = subparsers.add_parser("scaffold", help="Copy community templates into a project.")
    scaffold.add_argument("destination", type=Path)
    scaffold.add_argument("--overwrite", action="store_true")
    scaffold.set_defaults(func=_scaffold)

    return parser


def _health(args: argparse.Namespace) -> int:
    manifest = ProjectManifest.from_file(args.manifest)
    result = evaluate_health(manifest)
    print(f"{manifest.name}: {result.score}/100 ({result.grade})")
    if result.missing:
        print("\nMissing signals:")
        for signal in result.missing:
            print(f"- {signal}")
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


def _scaffold(args: argparse.Namespace) -> int:
    written = scaffold_templates(args.destination, overwrite=args.overwrite)
    if written:
        print("Wrote:")
        for path in written:
            print(f"- {path}")
    else:
        print("No files written. Use --overwrite to replace existing files.")
    return 0


def _write_or_print(content: str, output: Path | None) -> None:
    if output is None:
        print(content)
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(f"Wrote {output}")
