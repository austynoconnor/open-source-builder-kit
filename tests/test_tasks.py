from open_source_builder_kit.models import ProjectManifest
from open_source_builder_kit.tasks import render_tasks_markdown, suggest_tasks


def test_suggest_tasks_maps_missing_signals_to_contributor_work() -> None:
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

    tasks = suggest_tasks(manifest, limit=1)

    assert len(tasks) == 1
    assert tasks[0].title
    assert tasks[0].area


def test_render_tasks_markdown_includes_project_name() -> None:
    manifest = ProjectManifest.from_dict(
        {
            "name": "Example",
            "repository": "https://github.com/example/project",
            "description": "Example project",
            "signals": {},
        }
    )

    markdown = render_tasks_markdown(manifest, limit=2)

    assert markdown.startswith("# Suggested Contributor Tasks: Example")
    assert markdown.count("## ") == 2
