from pathlib import Path


def test_command_reference_mentions_core_commands() -> None:
    text = Path("docs/command-reference.md").read_text(encoding="utf-8")

    assert "## `osbk health`" in text
    assert "## `osbk scaffold`" in text
    assert "## `osbk validate-examples`" in text
