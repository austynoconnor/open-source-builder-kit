from __future__ import annotations

import json
from pathlib import Path

import yaml


def build_manifest_template(
    name: str,
    repository: str,
    description: str,
    license_name: str = "MIT",
) -> dict[str, object]:
    return {
        "name": name,
        "repository": repository,
        "description": description,
        "license": license_name,
        "maintainers": [{"name": "Maintainer Name", "role": "Lead maintainer"}],
        "tags": ["community", "open-source"],
        "notes": ["Replace this note with the project's current maintainer goals."],
        "signals": {
            "readme": True,
            "contributing": False,
            "code_of_conduct": False,
            "security_policy": False,
            "issue_templates": False,
            "pull_request_template": False,
            "ci": False,
            "tests": False,
            "release_notes": False,
            "roadmap": False,
        },
    }


def write_manifest_template(
    output: Path,
    name: str,
    repository: str,
    description: str,
    license_name: str = "MIT",
    overwrite: bool = False,
) -> Path:
    if output.exists() and not overwrite:
        raise FileExistsError(output)

    manifest = build_manifest_template(name, repository, description, license_name)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".json":
        output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    elif output.suffix.lower() in {".yml", ".yaml"}:
        output.write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
    else:
        raise ValueError("Output path must end in .json, .yml, or .yaml")
    return output

