# Changelog

## 2026-07-08 21:16:19 -05:00

AI model: GPT-5 Codex.

Added manifest initialization.

- Added `osbk init-manifest` to create starter JSON or YAML project manifests.
- Added manifest template generation with default community-health signals.
- Documented the manifest initialization flow in the README and CLI recipes.

## 2026-07-08 19:56:58 -05:00

AI model: GPT-5 Codex.

Added example manifest validation.

- Added `osbk validate-examples` to load and score every example manifest.
- Added validation to the CI check script so sample content cannot drift silently.
- Documented example validation in the README and CLI recipes.

## 2026-07-08 19:56:25 -05:00

AI model: GPT-5 Codex.

Added machine-readable health output.

- Added `osbk health --json` for CI, dashboards, and downstream automation.
- Documented JSON health output in the README and CLI recipes.
- Added CLI coverage for the JSON health output shape.

## 2026-07-08 19:55:48 -05:00

AI model: GPT-5 Codex.

Added CLI workflow documentation and refreshed examples.

- Added `docs/cli-recipes.md` with practical maintainer workflows for health checks, reports, contributor tasks, batch reporting, release checklists, and scaffolding.
- Refreshed sample health reports using the current report renderer.
- Linked the new recipe documentation from the README.

## 2026-07-08 19:55:14 -05:00

AI model: GPT-5 Codex.

Improved generated health reports.

- Added score-band language and maintainer focus guidance to generated reports.
- Embedded the top contributor-ready tasks in health reports so reports lead directly to action.
- Added regression coverage for the new report sections.

## 2026-07-08 19:54:25 -05:00

AI model: GPT-5 Codex.

Added contributor task suggestions.

- Added `osbk tasks` to convert missing health signals into scoped contributor work items.
- Added task rendering for docs, triage, review, quality, release, security, planning, and governance gaps.
- Updated the README quick start with the new contributor task command.

## 2026-07-08 19:12:00 -05:00

AI model: GPT-5 Codex.

Added batch health report generation.

- Added `osbk batch-report` for generating multiple project health reports from a single JSON batch file.
- Added batch job result handling and path resolution for repo-local manifests and outputs.
- Updated the README and demo batch input to document the new command.

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
