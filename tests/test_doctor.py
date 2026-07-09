from pathlib import Path

from open_source_builder_kit.doctor import inspect_repository, render_doctor_result


def test_inspect_repository_reports_missing_files(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Example\n", encoding="utf-8")

    result = inspect_repository(tmp_path)

    assert "README.md" in result.present
    assert "LICENSE" in result.missing
    assert result.ok is False


def test_render_doctor_result_includes_status(tmp_path: Path) -> None:
    result = inspect_repository(tmp_path)
    report = render_doctor_result(result)

    assert report.startswith("# Repository Doctor:")
    assert "Status: needs attention" in report
