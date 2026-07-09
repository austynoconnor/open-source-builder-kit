from __future__ import annotations

from .models import ProjectManifest


def render_support_policy(manifest: ProjectManifest) -> str:
    return f"""# Support Policy: {manifest.name}

This project welcomes clear, actionable requests. Use this policy to choose the right support path.

## Use Issues For

- Reproducible bugs.
- Documentation gaps.
- Small, scoped feature proposals.
- Maintainer tasks that are ready for public discussion.

## Use Discussions For

- Questions about project direction.
- Early ideas that are not ready for implementation.
- Community examples and adoption notes.

## Do Not Use Public Issues For

- Private security reports.
- Account-specific support.
- Requests that require sensitive logs, credentials, or private data.

## Maintainer Response Expectations

Maintainers will prioritize reports that include context, reproduction steps, expected behavior, and project version information. Reports that are incomplete may be closed with a request to reopen when the missing information is available.

## Repository

{manifest.repository}
"""

