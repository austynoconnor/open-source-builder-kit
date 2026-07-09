from __future__ import annotations

from .models import ProjectManifest
from .tasks import suggest_tasks


def render_issue_plan(manifest: ProjectManifest, limit: int | None = None) -> str:
    tasks = suggest_tasks(manifest, limit=limit)
    lines = [f"# Issue Plan: {manifest.name}", ""]
    if not tasks:
        lines.extend(["No issue drafts were generated because no health gaps were found.", ""])
        return "\n".join(lines)

    for index, task in enumerate(tasks, start=1):
        lines.extend(
            [
                f"## Issue {index}: {task.title}",
                "",
                "```markdown",
                f"# {task.title}",
                "",
                "## Goal",
                "",
                task.rationale,
                "",
                "## Suggested Scope",
                "",
                f"- Area: `{task.area}`",
                "- Keep this issue focused enough for one pull request.",
                "- Update documentation or tests when relevant.",
                "",
                "## Done When",
                "",
                "- [ ] The change is implemented.",
                "- [ ] The relevant docs or examples are updated.",
                "- [ ] Maintainers can verify the outcome from the pull request.",
                "```",
                "",
            ]
        )
    return "\n".join(lines)

