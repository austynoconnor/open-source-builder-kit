from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


SignalMap = dict[str, bool]


@dataclass(slots=True)
class Maintainer:
    name: str
    role: str = "Maintainer"


@dataclass(slots=True)
class ProjectManifest:
    name: str
    repository: str
    description: str
    license: str = "Unspecified"
    maintainers: list[Maintainer] = field(default_factory=list)
    signals: SignalMap = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @classmethod
    def from_file(cls, path: Path) -> "ProjectManifest":
        data = _read_structured_file(path)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProjectManifest":
        if "project" in data and isinstance(data["project"], dict):
            return cls._from_project_profile(data)

        required = ["name", "repository", "description"]
        missing = [key for key in required if not data.get(key)]
        if missing:
            joined = ", ".join(missing)
            raise ValueError(f"Manifest is missing required field(s): {joined}")

        maintainers = [
            Maintainer(name=str(item.get("name", "")).strip(), role=str(item.get("role", "Maintainer")))
            for item in data.get("maintainers", [])
            if item.get("name")
        ]

        raw_signals = data.get("signals", {})
        if not isinstance(raw_signals, dict):
            raise ValueError("Manifest field 'signals' must be a mapping of signal names to booleans")

        return cls(
            name=str(data["name"]).strip(),
            repository=str(data["repository"]).strip(),
            description=str(data["description"]).strip(),
            license=str(data.get("license", "Unspecified")).strip(),
            maintainers=maintainers,
            signals={str(key): bool(value) for key, value in raw_signals.items()},
            tags=[str(tag) for tag in data.get("tags", [])],
            notes=[str(note) for note in data.get("notes", [])],
        )

    @classmethod
    def _from_project_profile(cls, data: dict[str, Any]) -> "ProjectManifest":
        project = data["project"]
        required = ["name", "repository", "description"]
        missing = [key for key in required if not project.get(key)]
        if missing:
            joined = ", ".join(f"project.{key}" for key in missing)
            raise ValueError(f"Project profile is missing required field(s): {joined}")

        community = data.get("community", {})
        health_signals = data.get("healthSignals", {})
        docs = health_signals.get("docs", {}) if isinstance(health_signals, dict) else {}
        backlog = health_signals.get("issueBacklog", {}) if isinstance(health_signals, dict) else {}
        pull_requests = health_signals.get("pullRequests", {}) if isinstance(health_signals, dict) else {}
        contributor_stats = health_signals.get("community", {}) if isinstance(health_signals, dict) else {}

        maintainer_count = int(contributor_stats.get("maintainerCount", 0) or 0)
        maintainers = [
            Maintainer(name=f"Maintainer {index}", role="Project maintainer")
            for index in range(1, maintainer_count + 1)
        ]

        signals = {
            "readme": bool(docs.get("hasQuickstart")),
            "license": str(project.get("license", "")).lower() not in {"", "unspecified", "none"},
            "contributing": bool(community.get("contributionPaths")),
            "code_of_conduct": bool(community.get("codeOfConduct")),
            "security_policy": False,
            "issue_templates": int(backlog.get("untriagedIssues", 1) or 0) < 10,
            "pull_request_template": int(pull_requests.get("openPullRequests", 0) or 0) > 0,
            "ci": bool(docs.get("hasArchitectureGuide")),
            "tests": bool(docs.get("hasArchitectureGuide")),
            "release_notes": False,
            "roadmap": bool(data.get("toolkitGoals")),
            "maintainers_listed": maintainer_count > 0,
        }

        notes = [str(goal) for goal in data.get("toolkitGoals", [])]
        if isinstance(community, dict) and community.get("maintainerModel"):
            notes.insert(0, f"Maintainer model: {community['maintainerModel']}")

        return cls(
            name=str(project["name"]).strip(),
            repository=str(project["repository"]).strip(),
            description=str(project["description"]).strip(),
            license=str(project.get("license", "Unspecified")).strip(),
            maintainers=maintainers,
            signals=signals,
            tags=[str(item) for item in project.get("audience", [])],
            notes=notes,
        )


def _read_structured_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        data = yaml.safe_load(text)
    elif path.suffix.lower() == ".json":
        import json

        data = json.loads(text)
    else:
        raise ValueError("Manifest must be a .yml, .yaml, or .json file")

    if not isinstance(data, dict):
        raise ValueError("Manifest root must be an object")
    return data
