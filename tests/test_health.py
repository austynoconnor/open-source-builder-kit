from open_source_builder_kit.health import evaluate_health
from open_source_builder_kit.models import ProjectManifest


def test_health_score_rewards_present_signals() -> None:
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
                "tests": False,
            },
        }
    )

    result = evaluate_health(manifest)

    assert result.score > 0
    assert "readme" in result.present
    assert "tests" in result.missing

