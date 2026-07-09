# Community Health Guide

Community health is the set of practices that helps users, contributors, and maintainers interact with confidence. It is not just friendliness; it is clarity, safety, accountability, and predictable project operation.

Use this guide to evaluate and improve the non-code parts of an open-source repository.

## Community Health Baseline

A credible open-source project should have:

- A README that explains the project, setup, usage, support, and status.
- A contribution guide with local setup and pull request expectations.
- A code of conduct with reporting instructions.
- A security policy with private vulnerability reporting.
- A license.
- Issue and pull request templates, if the project receives regular external contributions.
- A release history or documented release process, if the project publishes versions.

These files should be visible from the repository root or linked from the README.

## User Trust Signals

Users quickly assess whether a project is safe to adopt. Strengthen trust by making these signals obvious:

- Project status is current and honest.
- Installation instructions work on a clean environment.
- Examples match the current API.
- Recent releases include useful notes.
- Security reporting does not require public disclosure.
- Known limitations are documented.
- Maintainers respond with clear decisions, even when the decision is no.

Trust is reduced by stale promises, unclear ownership, broken examples, and unanswered security paths.

## Contributor Experience

Contributors need enough context to make a useful change without guessing.

High-quality contributor experience includes:

- Clear development setup instructions.
- Test and formatting commands.
- Guidance on when to open an issue first.
- Labels that identify beginner-friendly and help-wanted work.
- Review expectations and approximate response windows.
- A respectful path for closing inactive work.

Avoid inviting broad contributions if maintainers do not have capacity to review them. A smaller, accurate invitation is better than a large, ignored queue.

## Issue Quality

Issue templates should help users provide actionable information.

For bug reports, ask for:

- Version.
- Environment.
- Reproduction steps.
- Expected behavior.
- Actual behavior.
- Relevant logs or screenshots.

For feature requests, ask for:

- Problem being solved.
- Proposed behavior.
- Alternatives considered.
- Compatibility or migration concerns.
- Willingness to contribute.

For documentation issues, ask for:

- Page or section.
- What was confusing.
- Suggested correction, if known.

## Support Boundaries

Public repositories often attract support requests. Decide what support the project offers and document it.

Possible support models:

- Community support only: users help each other; maintainers respond when available.
- Maintainer-supported issues: maintainers triage confirmed bugs and project questions.
- Commercial support: paid support exists outside the public issue tracker.
- No support: project is published as-is.

Recommended wording:

> Maintainers prioritize confirmed bugs, security issues, and reviewed contributions. General support is best-effort and may be redirected to discussions or documentation.

## Code of Conduct Operations

A code of conduct is only useful if maintainers know how to act on it.

For each report:

1. Acknowledge receipt privately.
2. Preserve relevant context.
3. Limit access to people who need to investigate.
4. Avoid public debate about the report.
5. Decide on action based on severity, evidence, and risk.
6. Communicate the outcome at the right level of detail.

Possible actions include warning, temporary restriction, permanent removal from project spaces, or no action when evidence does not support enforcement.

## Security Reporting

Security reports should have a private intake channel. Public issues are not appropriate for suspected vulnerabilities.

Security policy should state:

- Supported versions.
- Where to report vulnerabilities.
- What information to include.
- Expected acknowledgement window.
- Disclosure coordination expectations.

Do not promise a fix timeline unless maintainers can consistently meet it.

## Documentation Freshness

Stale documentation is a community health issue because it wastes user and maintainer time.

Review documentation:

- Before each release.
- After public API changes.
- After setup or dependency changes.
- When the same support question appears more than once.
- When onboarding a new contributor reveals missing context.

When in doubt, optimize docs for the person who is qualified but new to the project.

## Measuring Health

Track a few practical indicators:

- Time to first maintainer response on issues and pull requests.
- Number of issues waiting for reproduction.
- Number of open pull requests waiting on maintainer review.
- Frequency of repeated support questions.
- Release note quality.
- Security report handling time.

These metrics are signals for maintainers, not public performance targets unless the project chooses to publish them.

## Community Health Review

Run this review quarterly or before major releases:

- Can a new user install and run the project?
- Can a new contributor make a small change?
- Are open issues labeled and understandable?
- Are stale issues still valuable?
- Are pull requests waiting on a clear next action?
- Are conduct and security reporting paths current?
- Do docs reflect the current project status?

Community health work is maintenance work. Treat it as part of the project, not an optional extra.
