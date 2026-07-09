from pathlib import Path

from open_source_builder_kit.batch import run_report_batch


def test_run_report_batch_writes_outputs(tmp_path: Path) -> None:
    results = run_report_batch(Path("data/demo-inputs/cli-batch.json"), output_dir=tmp_path)

    assert [result.project_slug for result in results] == [
        "civic-data-commons",
        "learning-lab-toolkit",
    ]
    assert (tmp_path / "civic-data-commons.health-report.md").exists()
    assert (tmp_path / "learning-lab-toolkit.health-report.md").exists()
