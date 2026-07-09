from __future__ import annotations


CHECKLISTS: dict[str, list[str]] = {
    "release": [
        "Confirm CI is green on the release branch.",
        "Review merged pull requests and label user-facing changes.",
        "Update changelog with date, highlights, migrations, and known issues.",
        "Run package build locally and inspect generated artifacts.",
        "Tag the release using semantic versioning.",
        "Publish release notes with upgrade guidance.",
        "Open a follow-up issue for deferred work found during release review.",
    ],
    "triage": [
        "Thank the reporter and confirm the issue category.",
        "Check whether the report includes version, environment, reproduction steps, and expected behavior.",
        "Apply labels for area, impact, and contribution readiness.",
        "Link related issues or discussions.",
        "Ask one focused follow-up question if reproduction is blocked.",
        "Close respectfully when the issue is out of scope, duplicate, or not actionable.",
    ],
    "onboarding": [
        "Verify the README explains what the project does and who it serves.",
        "Make setup commands copy-pasteable for a clean environment.",
        "Provide a small first contribution path.",
        "Document test commands and expected runtime.",
        "Explain review expectations and maintainer response windows.",
        "Mark beginner-friendly issues only when they are genuinely scoped.",
    ],
    "docs": [
        "Document the common path before edge cases.",
        "Include one minimal example and one realistic example.",
        "Keep configuration reference separate from tutorial flow.",
        "Add troubleshooting for the three most common failure modes.",
        "Check links and command snippets before release.",
    ],
}


def render_checklist(kind: str) -> str:
    normalized = kind.lower().strip()
    if normalized not in CHECKLISTS:
        available = ", ".join(sorted(CHECKLISTS))
        raise ValueError(f"Unknown checklist '{kind}'. Available checklists: {available}")

    title = normalized.replace("_", " ").title()
    lines = [f"# {title} Checklist", ""]
    lines.extend(f"- [ ] {item}" for item in CHECKLISTS[normalized])
    lines.append("")
    return "\n".join(lines)

