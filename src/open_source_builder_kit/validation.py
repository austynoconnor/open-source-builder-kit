from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .health import evaluate_health
from .models import ProjectManifest


@dataclass(frozen=True, slots=True)
class ExampleValidationResult:
    path: Path
    project_name: str
    score: int


def validate_example_manifests(root: Path = Path("examples/project-profiles")) -> list[ExampleValidationResult]:
    if not root.exists():
        raise FileNotFoundError(root)

    manifest_paths = sorted(
        path for path in root.iterdir() if path.suffix.lower() in {".json", ".yml", ".yaml"}
    )
    if not manifest_paths:
        raise ValueError(f"No example manifests found in {root}")

    results: list[ExampleValidationResult] = []
    for path in manifest_paths:
        manifest = ProjectManifest.from_file(path)
        health = evaluate_health(manifest)
        results.append(
            ExampleValidationResult(path=path, project_name=manifest.name, score=health.score)
        )
    return results

