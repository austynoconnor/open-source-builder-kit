from __future__ import annotations

from datetime import UTC, datetime

from .health import HealthResult, evaluate_health
from .models import ProjectManifest
from .tasks import suggest_tasks_from_result


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
    task_lines = "\n".join(
        f"- **{task.title}** ({task.area}): {task.rationale}"
        for task in suggest_tasks_from_result(result, limit=3)
    )
    if not task_lines:
        task_lines = "- No immediate contributor tasks generated."

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
- Score band: {_score_band(result.score)}

## Maintainer Focus

{_maintainer_focus(result)}

## Maintainers

{maintainers}

## Signals Present

{present}

## Signals Missing

{missing}

## Recommended Next Actions

{recommendations}

## Contributor-Ready Tasks

{task_lines}

## Maintainer Notes

{notes}
"""


def _score_band(score: int) -> str:
    if score >= 90:
        return "Healthy and well documented"
    if score >= 75:
        return "Strong foundation with a few visible gaps"
    if score >= 60:
        return "Usable, but maintainers should prioritize community-health work"
    return "High maintenance risk until the basics are documented"


def _maintainer_focus(result: HealthResult) -> str:
    if not result.missing:
        return "Keep the project healthy by reviewing docs and automation after every release."

    highest_priority = result.missing[:3]
    readable = ", ".join(signal.replace("_", " ") for signal in highest_priority)
    return f"Prioritize {readable}. These gaps have the clearest effect on contributor trust and maintainer load."
