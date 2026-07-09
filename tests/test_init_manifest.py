from pathlib import Path

from open_source_builder_kit.init_manifest import write_manifest_template
from open_source_builder_kit.models import ProjectManifest


def test_write_manifest_template_creates_loadable_yaml(tmp_path: Path) -> None:
    output = tmp_path / "project.yml"

    write_manifest_template(
        output=output,
        name="Example Project",
        repository="https://github.com/example/project",
        description="A useful project.",
    )

    manifest = ProjectManifest.from_file(output)

    assert manifest.name == "Example Project"
    assert manifest.signals["readme"] is True
    assert manifest.signals["tests"] is False


def test_write_manifest_template_refuses_existing_file(tmp_path: Path) -> None:
    output = tmp_path / "project.json"
    output.write_text("{}", encoding="utf-8")

    try:
        write_manifest_template(
            output=output,
            name="Example Project",
            repository="https://github.com/example/project",
            description="A useful project.",
        )
    except FileExistsError:
        pass
    else:
        raise AssertionError("Expected FileExistsError")
