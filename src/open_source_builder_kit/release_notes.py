from __future__ import annotations

from .health import evaluate_health
from .models import ProjectManifest


def render_release_notes(manifest: ProjectManifest, version: str) -> str:
    result = evaluate_health(manifest)
    gaps = "\n".join(f"- {gap.replace('_', ' ')}" for gap in result.missing[:5]) or "- None"
    return f"""# {manifest.name} {version}

## Highlights

- Summarize user-facing improvements here.
- Summarize maintainer-facing improvements here.
- Mention contributor-visible documentation, testing, or workflow changes.

## Upgrade Notes

- Document any breaking changes, migrations, or manual steps.
- If there are no upgrade steps, say so clearly.

## Community Health

- Current health score: {result.score}/100 ({result.grade})
- Top open health gaps:
{gaps}

## Thanks

Thank contributors, reviewers, reporters, and maintainers who helped with this release.

## Repository

{manifest.repository}
"""

