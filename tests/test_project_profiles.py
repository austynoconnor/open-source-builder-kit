from pathlib import Path

from open_source_builder_kit.health import evaluate_health
from open_source_builder_kit.models import ProjectManifest


def test_nested_project_profile_loads_as_manifest() -> None:
    manifest = ProjectManifest.from_file(
        Path("examples/project-profiles/civic-data-commons.manifest.json")
    )

    result = evaluate_health(manifest)

    assert manifest.name == "Civic Data Commons"
    assert manifest.repository == "https://github.com/example/civic-data-commons"
    assert manifest.maintainers
    assert result.score > 0
