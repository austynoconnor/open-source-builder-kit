from pathlib import Path

from open_source_builder_kit.issues import render_issue_plan
from open_source_builder_kit.models import ProjectManifest


def test_render_issue_plan_outputs_issue_drafts() -> None:
    manifest = ProjectManifest.from_file(
        Path("examples/project-profiles/civic-data-commons.manifest.json")
    )

    plan = render_issue_plan(manifest, limit=2)

    assert plan.startswith("# Issue Plan: Civic Data Commons")
    assert plan.count("```markdown") == 2
    assert "## Done When" in plan
