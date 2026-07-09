from open_source_builder_kit.models import ProjectManifest
from open_source_builder_kit.reports import render_health_report


def test_report_includes_focus_and_contributor_tasks() -> None:
    manifest = ProjectManifest.from_dict(
        {
            "name": "Example",
            "repository": "https://github.com/example/project",
            "description": "Example project",
            "license": "MIT",
            "maintainers": [{"name": "Maintainer"}],
            "signals": {
                "readme": True,
                "contributing": True,
                "security_policy": False,
            },
        }
    )

    report = render_health_report(manifest)

    assert "## Maintainer Focus" in report
    assert "## Contributor-Ready Tasks" in report
    assert "Score band:" in report
