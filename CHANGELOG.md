# Changelog

## 2026-07-08 19:02:07 -05:00

AI model: GPT-5 Codex.

Improved CLI compatibility with richer project-profile examples.

- Added normalization for nested demo profiles with `project`, `community`, and `healthSignals` sections.
- Added test coverage proving example project profiles can be loaded and scored by the CLI health model.

## 2026-07-08 19:01:18 -05:00

AI model: GPT-5 Codex.

Polished the initial repository integration before publishing.

- Added `.gitignore` to keep Python, test, lint, and build artifacts out of version control.
- Added `MANIFEST.in` so docs, examples, and templates are included in source distributions.
- Corrected README quick-start commands to point at the actual example manifests.

## 2026-07-08 18:56:57 -05:00

AI model: GPT-5 Codex.

Added professional GitHub community automation.

- Added structured issue templates for bugs, feature requests, and documentation issues.
- Added pull request template, funding placeholder, CODEOWNERS, and Dependabot configuration.
- Added GitHub Actions workflows for CI and documentation link checking.
- Added reusable scripts for Python/Node lint-test checks and Markdown link validation.

## 2026-07-08 18:56:49 -05:00

AI model: GPT-5 Codex.

Created maintainer-focused documentation and reusable community templates.

- Added getting started guidance for adopting the kit and setting up repository health files.
- Added a maintainer playbook covering triage, pull request review, governance, contributor onboarding, and maintainer boundaries.
- Added community health guidance for support boundaries, issue quality, security reporting, conduct operations, and documentation freshness.
- Added a release guide with versioning policy, release checklists, changelog standards, security release flow, rollback planning, and post-release verification.
- Added reusable README, contributing, code of conduct, and security policy templates for open-source maintainers.

## 2026-07-08 18:54:02 -05:00

AI model: GPT-5 Codex.

Initial repository build for `open-source-builder-kit`.

- Added a Python CLI package for open-source project health checks, reports, checklists, and template scaffolding.
- Added project metadata, license, README, tests, examples, documentation, templates, and GitHub community automation.
- Built the repository around practical maintainer support: contributor onboarding, release hygiene, security posture, issue triage, and community health.
