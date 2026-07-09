from pathlib import Path

from open_source_builder_kit.compare import render_comparison


def test_render_comparison_outputs_markdown_table() -> None:
    comparison = render_comparison(
        [
            Path("examples/project-profiles/civic-data-commons.manifest.json"),
            Path("examples/project-profiles/learning-lab-toolkit.manifest.json"),
        ]
    )

    assert comparison.startswith("# Project Health Comparison")
    assert "| Civic Data Commons |" in comparison
    assert "| Learning Lab Toolkit |" in comparison
