from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


EXPECTED_FILES: tuple[str, ...] = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
)


@dataclass(frozen=True, slots=True)
class DoctorResult:
    root: Path
    present: list[str]
    missing: list[str]

    @property
    def ok(self) -> bool:
        return not self.missing


def inspect_repository(root: Path) -> DoctorResult:
    if not root.exists():
        raise FileNotFoundError(root)
    if not root.is_dir():
        raise NotADirectoryError(root)

    present = []
    missing = []
    for relative in EXPECTED_FILES:
        target = root / relative
        if target.exists():
            present.append(relative)
        else:
            missing.append(relative)
    return DoctorResult(root=root, present=present, missing=missing)


def render_doctor_result(result: DoctorResult) -> str:
    lines = [f"# Repository Doctor: {result.root}", ""]
    lines.append(f"Status: {'pass' if result.ok else 'needs attention'}")
    lines.extend(["", "## Present", ""])
    lines.extend(f"- {item}" for item in result.present)
    lines.extend(["", "## Missing", ""])
    lines.extend(f"- {item}" for item in result.missing or ["None"])
    lines.append("")
    return "\n".join(lines)

