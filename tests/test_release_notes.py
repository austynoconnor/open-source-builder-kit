from pathlib import Path

from open_source_builder_kit.models import ProjectManifest
from open_source_builder_kit.release_notes import render_release_notes


def test_render_release_notes_contains_version_and_health() -> None:
    manifest = ProjectManifest.from_file(
        Path("examples/project-profiles/civic-data-commons.manifest.json")
    )

    notes = render_release_notes(manifest, "v0.1.0")

    assert notes.startswith("# Civic Data Commons v0.1.0")
    assert "Community Health" in notes
    assert manifest.repository in notes
