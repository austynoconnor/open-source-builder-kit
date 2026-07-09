from pathlib import Path

from open_source_builder_kit.models import ProjectManifest
from open_source_builder_kit.support import render_support_policy


def test_render_support_policy_includes_project_repository() -> None:
    manifest = ProjectManifest.from_file(
        Path("examples/project-profiles/civic-data-commons.manifest.json")
    )

    policy = render_support_policy(manifest)

    assert policy.startswith("# Support Policy: Civic Data Commons")
    assert manifest.repository in policy
    assert "Use Issues For" in policy
