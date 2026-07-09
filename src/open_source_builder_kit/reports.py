from __future__ import annotations

from datetime import UTC, datetime

from .health import HealthResult, evaluate_health
from .models import ProjectManifest


def render_health_report(manifest: ProjectManifest, result: HealthResult | None = None) -> str:
    result = result or evaluate_health(manifest)
    maintainers = "\n".join(
        f"- {maintainer.name} ({maintainer.role})" for maintainer in manifest.maintainers
    )
    if not maintainers:
        maintainers = "- Not listed yet"

    tags = ", ".join(manifest.tags) if manifest.tags else "None listed"
    notes = "\n".join(f"- {note}" for note in manifest.notes) if manifest.notes else "- None"
    present = "\n".join(f"- {signal}" for signal in result.present) or "- None"
    missing = "\n".join(f"- {signal}" for signal in result.missing) or "- None"
    recommendations = "\n".join(f"- {item}" for item in result.recommendations) or "- No gaps found."

    generated = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    return f"""# Open Source Health Report: {manifest.name}

Generated: {generated}

## Summary

{manifest.description}

- Repository: {manifest.repository}
- License: {manifest.license}
- Tags: {tags}
- Health score: {result.score}/100
- Grade: {result.grade}

## Maintainers

{maintainers}

## Signals Present

{present}

## Signals Missing

{missing}

## Recommended Next Actions

{recommendations}

## Maintainer Notes

{notes}
"""

