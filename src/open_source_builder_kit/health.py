from __future__ import annotations

from dataclasses import dataclass

from .models import ProjectManifest


SIGNAL_WEIGHTS: dict[str, int] = {
    "readme": 12,
    "license": 8,
    "contributing": 12,
    "code_of_conduct": 8,
    "security_policy": 8,
    "issue_templates": 8,
    "pull_request_template": 6,
    "ci": 10,
    "tests": 10,
    "release_notes": 6,
    "roadmap": 6,
    "maintainers_listed": 6,
}

SIGNAL_RECOMMENDATIONS: dict[str, str] = {
    "readme": "Add a README with purpose, install steps, usage examples, and support boundaries.",
    "license": "Choose an OSI-approved license and place it at the repository root.",
    "contributing": "Add CONTRIBUTING.md with setup steps, review expectations, and contribution types.",
    "code_of_conduct": "Add a code of conduct that explains behavior expectations and reporting paths.",
    "security_policy": "Add SECURITY.md with supported versions and private vulnerability reporting guidance.",
    "issue_templates": "Add issue templates for bugs, features, docs, and maintainer tasks.",
    "pull_request_template": "Add a PR template with testing, docs, and risk prompts.",
    "ci": "Add CI that runs tests and lightweight quality checks on every pull request.",
    "tests": "Add tests for core behavior and examples that contributors can run locally.",
    "release_notes": "Publish release notes so users can understand changes and upgrade risk.",
    "roadmap": "Maintain a roadmap that separates committed work from exploration.",
    "maintainers_listed": "List maintainers and areas of ownership so contributors know where to ask.",
}


@dataclass(frozen=True, slots=True)
class HealthResult:
    score: int
    grade: str
    present: list[str]
    missing: list[str]
    recommendations: list[str]


def evaluate_health(manifest: ProjectManifest) -> HealthResult:
    signals = dict(manifest.signals)
    signals.setdefault("license", manifest.license.lower() not in {"", "unspecified", "none"})
    signals.setdefault("maintainers_listed", bool(manifest.maintainers))

    possible = sum(SIGNAL_WEIGHTS.values())
    earned = sum(weight for signal, weight in SIGNAL_WEIGHTS.items() if signals.get(signal))
    score = round((earned / possible) * 100)
    missing = [signal for signal in SIGNAL_WEIGHTS if not signals.get(signal)]
    present = [signal for signal in SIGNAL_WEIGHTS if signals.get(signal)]

    return HealthResult(
        score=score,
        grade=_grade(score),
        present=present,
        missing=missing,
        recommendations=[SIGNAL_RECOMMENDATIONS[signal] for signal in missing],
    )


def _grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "Needs attention"

