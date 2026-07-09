import json

from open_source_builder_kit.cli import main


def test_health_json_output(capsys) -> None:  # type: ignore[no-untyped-def]
    exit_code = main(
        [
            "health",
            "examples/project-profiles/civic-data-commons.manifest.json",
            "--json",
        ]
    )

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["name"] == "Civic Data Commons"
    assert isinstance(payload["score"], int)
    assert "missing" in payload
