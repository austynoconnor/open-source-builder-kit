from __future__ import annotations

from dataclasses import dataclass

from .health import HealthResult, evaluate_health
from .models import ProjectManifest


TASK_LIBRARY: dict[str, tuple[str, str, str]] = {
    "readme": (
        "Improve the project README",
        "docs",
        "Add purpose, install steps, quick start, support boundaries, and one realistic example.",
    ),
    "contributing": (
        "Create a contributor guide",
        "community",
        "Document local setup, test commands, review expectations, and beginner-friendly contribution paths.",
    ),
    "code_of_conduct": (
        "Add community conduct guidance",
        "community",
        "Adopt a code of conduct and document how maintainers handle reports.",
    ),
    "security_policy": (
        "Write a security policy",
        "security",
        "Add supported versions, private reporting instructions, and expected response windows.",
    ),
    "issue_templates": (
        "Add issue templates",
        "triage",
        "Create structured templates for bugs, feature requests, documentation, and maintainer tasks.",
    ),
    "pull_request_template": (
        "Add a pull request template",
        "review",
        "Prompt contributors for tests, docs updates, screenshots when relevant, and known risk.",
    ),
    "ci": (
        "Add continuous integration",
        "quality",
        "Run tests and lightweight lint checks on pull requests and pushes to the main branch.",
    ),
    "tests": (
        "Add first-pass tests",
        "quality",
        "Cover the most important behavior with tests contributors can run locally.",
    ),
    "release_notes": (
        "Create a release notes process",
        "release",
        "Document changelog expectations and publish user-facing release notes for each tagged version.",
    ),
    "roadmap": (
        "Publish a lightweight roadmap",
        "planning",
        "Separate committed work, exploration, and community help-wanted areas.",
    ),
    "maintainers_listed": (
        "List maintainers and ownership areas",
        "governance",
        "Explain who maintains the project and where contributors should route questions.",
    ),
}


@dataclass(frozen=True, slots=True)
class SuggestedTask:
    title: str
    area: str
    rationale: str


def suggest_tasks(manifest: ProjectManifest, limit: int | None = None) -> list[SuggestedTask]:
    result = evaluate_health(manifest)
    return suggest_tasks_from_result(result, limit=limit)


def suggest_tasks_from_result(result: HealthResult, limit: int | None = None) -> list[SuggestedTask]:
    tasks = [
        SuggestedTask(title=title, area=area, rationale=rationale)
        for signal in result.missing
        for title, area, rationale in [TASK_LIBRARY.get(signal, _fallback_task(signal))]
    ]
    if limit is None:
        return tasks
    return tasks[: max(limit, 0)]


def render_tasks_markdown(manifest: ProjectManifest, limit: int | None = None) -> str:
    tasks = suggest_tasks(manifest, limit=limit)
    lines = [f"# Suggested Contributor Tasks: {manifest.name}", ""]
    if not tasks:
        lines.extend(["No missing community-health signals were found.", ""])
        return "\n".join(lines)

    for task in tasks:
        lines.extend(
            [
                f"## {task.title}",
                "",
                f"- Area: {task.area}",
                f"- Why it helps: {task.rationale}",
                "",
            ]
        )
    return "\n".join(lines)


def _fallback_task(signal: str) -> tuple[str, str, str]:
    title = signal.replace("_", " ").capitalize()
    return (f"Improve {title}", "maintenance", f"Close the missing `{signal}` health signal.")

