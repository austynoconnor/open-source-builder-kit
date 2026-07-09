from __future__ import annotations

from .health import HealthResult, evaluate_health
from .models import ProjectManifest
from .tasks import suggest_tasks_from_result


def render_roadmap(manifest: ProjectManifest, result: HealthResult | None = None) -> str:
    result = result or evaluate_health(manifest)
    tasks = suggest_tasks_from_result(result)
    immediate = tasks[:3]
    next_up = tasks[3:6]
    later = tasks[6:]

    return "\n".join(
        [
            f"# Maintainer Roadmap: {manifest.name}",
            "",
            f"Current health score: {result.score}/100 ({result.grade})",
            "",
            "## Immediate",
            "",
            _render_task_list(immediate, "No immediate gaps were detected."),
            "## Next",
            "",
            _render_task_list(next_up, "No secondary work is queued."),
            "## Later",
            "",
            _render_task_list(later, "No longer-term health tasks are queued."),
            "## Review Cadence",
            "",
            "- Re-run `osbk health` before each release.",
            "- Revisit this roadmap after major contributor-facing changes.",
            "- Move completed work into release notes so users can see maintainer progress.",
            "",
        ]
    )


def _render_task_list(tasks: list[object], empty: str) -> str:
    if not tasks:
        return f"- {empty}\n"
    lines = []
    for task in tasks:
        title = getattr(task, "title")
        area = getattr(task, "area")
        rationale = getattr(task, "rationale")
        lines.append(f"- [ ] **{title}** ({area}) - {rationale}")
    return "\n".join(lines) + "\n"

