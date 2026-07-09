from pathlib import Path

from open_source_builder_kit.models import ProjectManifest
from open_source_builder_kit.roadmap import render_roadmap


def test_render_roadmap_groups_health_work() -> None:
    manifest = ProjectManifest.from_file(
        Path("examples/project-profiles/civic-data-commons.manifest.json")
    )

    roadmap = render_roadmap(manifest)

    assert roadmap.startswith("# Maintainer Roadmap: Civic Data Commons")
    assert "## Immediate" in roadmap
    assert "## Review Cadence" in roadmap
