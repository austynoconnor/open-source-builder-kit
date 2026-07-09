from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_MAP: dict[str, str] = {
    "README-template.md": "README.md",
    "CONTRIBUTING-template.md": "CONTRIBUTING.md",
    "CODE_OF_CONDUCT-template.md": "CODE_OF_CONDUCT.md",
    "SECURITY-template.md": "SECURITY.md",
}


def scaffold_templates(destination: Path, overwrite: bool = False) -> list[Path]:
    template_dir = ROOT / "templates"
    if not template_dir.exists():
        raise FileNotFoundError("templates directory was not found")

    destination.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for source_name, target_name in TEMPLATE_MAP.items():
        source = template_dir / source_name
        target = destination / target_name
        if target.exists() and not overwrite:
            continue
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        written.append(target)
    return written

