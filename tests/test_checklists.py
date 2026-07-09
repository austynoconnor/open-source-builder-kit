from open_source_builder_kit.checklists import render_checklist
from open_source_builder_kit.scaffold import TEMPLATE_MAP


def test_render_checklist_contains_markdown_tasks() -> None:
    checklist = render_checklist("release")

    assert checklist.startswith("# Release Checklist")
    assert "- [ ] Confirm CI is green" in checklist


def test_scaffold_includes_decision_log_template() -> None:
    assert TEMPLATE_MAP["DECISION_LOG-template.md"] == "DECISION_LOG.md"
