from __future__ import annotations

import json
from dataclasses import asdict, dataclass

import yaml


@dataclass(frozen=True, slots=True)
class Label:
    name: str
    color: str
    description: str


DEFAULT_LABELS: tuple[Label, ...] = (
    Label("area: docs", "0E8A16", "Documentation, examples, or educational content."),
    Label("area: tests", "5319E7", "Test coverage, fixtures, and validation changes."),
    Label("area: community", "1D76DB", "Contributor onboarding, conduct, or support workflows."),
    Label("area: security", "D93F0B", "Security policy, reporting, or vulnerability handling."),
    Label("type: bug", "D73A4A", "Something is broken or behaving incorrectly."),
    Label("type: feature", "A2EEEF", "New capability or enhancement request."),
    Label("type: maintenance", "C2E0C6", "Repository upkeep, dependencies, or automation."),
    Label("good first issue", "7057FF", "Scoped work suitable for newer contributors."),
    Label("help wanted", "008672", "Work where maintainer support from the community is welcome."),
    Label("needs triage", "FBCA04", "Needs maintainer review before work starts."),
)


def render_labels(format_name: str = "yaml") -> str:
    payload = [asdict(label) for label in DEFAULT_LABELS]
    normalized = format_name.lower()
    if normalized == "json":
        return json.dumps(payload, indent=2) + "\n"
    if normalized in {"yaml", "yml"}:
        return yaml.safe_dump(payload, sort_keys=False)
    raise ValueError("Label format must be 'yaml' or 'json'")

