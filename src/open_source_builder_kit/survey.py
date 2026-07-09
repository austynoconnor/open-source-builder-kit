from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class SurveyTopicSummary:
    topic: str
    average_rating: float
    notes: list[str] = field(default_factory=list)


@dataclass(slots=True)
class SurveyProjectSummary:
    project_slug: str
    topics: list[SurveyTopicSummary]


def summarize_survey(path: Path) -> list[SurveyProjectSummary]:
    if not path.exists():
        raise FileNotFoundError(path)

    grouped: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"project_slug", "topic", "rating_1_to_5", "note"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            joined = ", ".join(sorted(missing))
            raise ValueError(f"Survey CSV is missing required column(s): {joined}")

        for row in reader:
            grouped[row["project_slug"]][row["topic"]].append(row)

    summaries: list[SurveyProjectSummary] = []
    for project_slug in sorted(grouped):
        topics = []
        for topic in sorted(grouped[project_slug]):
            rows = grouped[project_slug][topic]
            ratings = [float(row["rating_1_to_5"]) for row in rows if row["rating_1_to_5"]]
            average = sum(ratings) / len(ratings) if ratings else 0.0
            notes = [row["note"] for row in rows if row.get("note")]
            topics.append(SurveyTopicSummary(topic=topic, average_rating=average, notes=notes))
        summaries.append(SurveyProjectSummary(project_slug=project_slug, topics=topics))
    return summaries


def render_survey_summary(path: Path) -> str:
    summaries = summarize_survey(path)
    lines = ["# Maintainer Survey Summary", ""]
    for project in summaries:
        lines.extend([f"## {project.project_slug}", ""])
        for topic in project.topics:
            lines.extend(
                [
                    f"### {topic.topic}",
                    "",
                    f"- Average rating: {topic.average_rating:.1f}/5",
                    "- Notes:",
                ]
            )
            lines.extend(f"  - {note}" for note in topic.notes)
            lines.append("")
    return "\n".join(lines)

