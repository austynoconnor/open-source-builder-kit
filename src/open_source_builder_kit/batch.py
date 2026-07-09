from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .models import ProjectManifest
from .reports import render_health_report


@dataclass(frozen=True, slots=True)
class BatchJobResult:
    project_slug: str
    output: Path


def run_report_batch(batch_file: Path, output_dir: Path | None = None) -> list[BatchJobResult]:
    data = _read_batch_file(batch_file)
    jobs = data.get("jobs", [])
    if not isinstance(jobs, list) or not jobs:
        raise ValueError("Batch file must include a non-empty 'jobs' list")

    results: list[BatchJobResult] = []
    base_dir = batch_file.parent
    for job in jobs:
        if not isinstance(job, dict):
            raise ValueError("Each batch job must be an object")

        manifest_path = _resolve_path(base_dir, str(job.get("manifest", "")))
        manifest = ProjectManifest.from_file(manifest_path)
        project_slug = str(job.get("projectSlug") or _slugify(manifest.name))

        if output_dir is not None:
            output = output_dir / f"{project_slug}.health-report.md"
        else:
            output = _resolve_path(base_dir, str(job.get("output", "")))

        if not str(output):
            raise ValueError(f"Batch job for {project_slug} is missing an output path")

        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_health_report(manifest), encoding="utf-8")
        results.append(BatchJobResult(project_slug=project_slug, output=output))

    return results


def _read_batch_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Batch file root must be an object")
    return data


def _resolve_path(base_dir: Path, raw_path: str) -> Path:
    if not raw_path:
        return Path()
    path = Path(raw_path)
    if path.is_absolute():
        return path
    candidate = base_dir / path
    if candidate.exists() or str(raw_path).startswith(".."):
        return candidate
    return Path.cwd() / path


def _slugify(value: str) -> str:
    normalized = "".join(char.lower() if char.isalnum() else "-" for char in value)
    return "-".join(part for part in normalized.split("-") if part)

