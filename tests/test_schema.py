import json
from pathlib import Path


def test_manifest_schema_is_valid_json() -> None:
    schema = json.loads(Path("schema/manifest.schema.json").read_text(encoding="utf-8"))

    assert schema["title"] == "Open Source Builder Kit Manifest"
    assert "name" in schema["required"]
