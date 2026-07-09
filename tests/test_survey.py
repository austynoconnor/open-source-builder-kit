from pathlib import Path

from open_source_builder_kit.survey import render_survey_summary, summarize_survey


def test_summarize_survey_groups_projects_and_topics() -> None:
    summaries = summarize_survey(Path("data/demo-inputs/maintainer-survey.csv"))

    assert len(summaries) == 2
    civic = next(summary for summary in summaries if summary.project_slug == "civic-data-commons")
    assert {topic.topic for topic in civic.topics} == {
        "onboarding_clarity",
        "release_confidence",
        "triage_capacity",
    }


def test_render_survey_summary_outputs_markdown() -> None:
    markdown = render_survey_summary(Path("data/demo-inputs/maintainer-survey.csv"))

    assert markdown.startswith("# Maintainer Survey Summary")
    assert "Average rating:" in markdown
    assert "civic-data-commons" in markdown
