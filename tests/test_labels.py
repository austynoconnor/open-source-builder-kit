import json

import yaml

from open_source_builder_kit.labels import render_labels


def test_render_labels_yaml_contains_triage_label() -> None:
    labels = yaml.safe_load(render_labels("yaml"))

    assert any(label["name"] == "needs triage" for label in labels)


def test_render_labels_json_is_machine_readable() -> None:
    labels = json.loads(render_labels("json"))

    assert labels[0]["name"] == "area: docs"
