from __future__ import annotations

from pathlib import Path

from .health import evaluate_health
from .models import ProjectManifest


def render_comparison(manifest_paths: list[Path]) -> str:
    if not manifest_paths:
        raise ValueError("At least one manifest path is required")

    rows = []
    for path in manifest_paths:
        manifest = ProjectManifest.from_file(path)
        result = evaluate_health(manifest)
        rows.append((manifest.name, result.score, result.grade, ", ".join(result.missing[:3]) or "None"))

    lines = [
        "# Project Health Comparison",
        "",
        "| Project | Score | Grade | Top gaps |",
        "| --- | ---: | --- | --- |",
    ]
    lines.extend(f"| {name} | {score} | {grade} | {gaps} |" for name, score, grade, gaps in rows)
    lines.append("")
    return "\n".join(lines)

