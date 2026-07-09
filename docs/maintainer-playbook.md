# Maintainer Playbook

This playbook gives maintainers a practical operating model for running an open-source project without relying on memory, heroics, or hidden context.

Use it as the internal standard for triage, reviews, decisions, community support, and maintenance work.

## Maintainer Responsibilities

Maintainers are responsible for the health of the project, not for satisfying every request. A strong maintainer practice balances user value, contributor experience, technical quality, and sustainability.

Core responsibilities:

- Keep the project direction understandable.
- Protect the quality and security of the codebase.
- Respond to issues and pull requests with clear next steps.
- Make contribution paths visible and realistic.
- Publish releases with accurate notes.
- Enforce community standards consistently.
- Say no when a request does not fit the project.

## Operating Principles

Use these principles when making tradeoffs:

- Prefer clear scope over vague ambition.
- Prefer reproducible reports over long discussion threads.
- Prefer small pull requests over broad rewrites.
- Prefer explicit decisions over implied consensus.
- Prefer documented policy over case-by-case memory.
- Prefer maintainer sustainability over constant availability.

## Weekly Maintainer Routine

For active projects, run this routine once per week:

1. Review new issues and assign labels.
2. Close duplicates with links to canonical issues.
3. Ask for reproductions where bug reports are incomplete.
4. Review pull requests that are ready and scoped.
5. Move stale discussions toward a decision or close them.
6. Check dependency, security, and CI alerts.
7. Update project notes, roadmap, or release tracking as needed.

For lower-activity projects, run the same routine before each release or monthly.

## Issue Triage

Triage turns incoming work into an actionable queue.

### Bug Reports

A bug report should include:

- Project version or commit.
- Environment details.
- Expected behavior.
- Actual behavior.
- Minimal reproduction.
- Logs, screenshots, or failing tests when relevant.

If a report does not include enough detail, ask for the missing information and apply `needs reproduction`. Close the issue if it remains inactive after the documented response window.

### Feature Requests

Evaluate feature requests against:

- Fit with project scope.
- Number of users helped.
- Maintenance cost.
- Compatibility impact.
- Availability of a contributor or maintainer to implement it.
- Whether the feature belongs in core, an integration, or documentation.

When declining a request, be direct and kind:

> Thanks for the suggestion. This does not fit the current scope because [reason]. We are going to close this rather than leave it open without a realistic path to implementation.

### Questions and Support

If the project has a discussion forum, route questions there. If it does not, use issues only for questions that reveal documentation gaps or likely defects.

Convert repeated support questions into documentation improvements.

## Pull Request Review

Pull request review should protect the project while helping contributors understand what is needed.

### Review Checklist

Before merging, confirm:

- The change fits the project scope.
- The implementation is understandable and maintainable.
- Tests or examples cover the changed behavior.
- Documentation is updated when user behavior changes.
- Public APIs, configuration, and data formats are compatible or clearly marked as breaking.
- Errors and edge cases are handled intentionally.
- CI passes.

### Review Style

Good reviews are specific and actionable:

- Explain the concern, not just the preference.
- Distinguish required changes from optional suggestions.
- Use examples when the requested change may be unclear.
- Avoid expanding scope after the contributor has satisfied the original request.

Useful review language:

- `Required:` This can break existing users because...
- `Suggestion:` This would be easier to maintain if...
- `Question:` I may be missing context. Why does this need to...
- `Blocking:` We need a test for this path before merging.

## Decision-Making

Not every decision needs a formal process. Use the lightest process that still creates clarity.

### Routine Decisions

Maintainers can decide directly on:

- Bug fixes.
- Documentation updates.
- Internal refactors with no public behavior change.
- Small dependency updates.
- Minor developer experience improvements.

### Significant Decisions

Open an issue or proposal for:

- Breaking changes.
- New public APIs.
- License changes.
- Governance changes.
- Major dependency or platform shifts.
- Features that materially increase maintenance burden.

Record the decision in the issue before implementation starts.

## Contributor Onboarding

Make it easy for contributors to succeed:

- Keep `good first issue` truly small and well-defined.
- Include expected files, acceptance criteria, and test commands.
- Avoid assigning critical-path work to first-time contributors without support.
- Thank contributors by name in release notes when appropriate.
- Close abandoned contributor pull requests respectfully and explain how to reopen.

## Handling Conflict

When disagreement happens:

1. Restate the concrete decision being made.
2. Separate user impact, technical risk, and personal preference.
3. Ask for evidence: reproduction, benchmark, prior art, or design rationale.
4. Make a decision and document why.
5. Move on.

If behavior violates the code of conduct, follow the reporting and enforcement process instead of debating in public.

## Maintainer Boundaries

Healthy boundaries make the project more reliable.

It is acceptable to:

- Close issues that lack enough information.
- Decline features that do not fit.
- Pause reviews when maintainers are unavailable.
- Require tests and documentation.
- Stop engaging in unproductive threads.
- Put the project into maintenance mode if needed.

State boundaries clearly in the README or CONTRIBUTING file so users know what to expect.

## Project Status Levels

Choose and publish a status:

- `Experimental`: APIs and behavior may change quickly.
- `Active`: new features and fixes are being accepted.
- `Stable`: changes are conservative and compatibility matters.
- `Maintenance`: only critical fixes and security updates are expected.
- `Archived`: no active maintenance is planned.

Status should reflect reality. Overpromising creates support debt.

## Maintainer Handoff

When adding or replacing maintainers:

- Confirm the person has made sustained, constructive contributions.
- Grant permissions gradually where possible.
- Document release, security, and moderation responsibilities.
- Make access ownership visible to existing maintainers.
- Remove access promptly when a maintainer steps down.

For critical projects, avoid a single maintainer owning all release and security access.
