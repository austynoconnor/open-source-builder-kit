# Release Guide

This guide defines a practical release process for open-source maintainers. Adapt the commands and approval rules to match your project tooling.

## Release Goals

A good release should be:

- Reproducible: another maintainer can follow the same steps.
- Reviewable: changes and risk are visible before publishing.
- Reversible: the team knows what to do if a release is bad.
- Understandable: users can tell what changed and whether they need to act.

## Versioning Policy

Use semantic versioning when the project exposes a public API, CLI, configuration format, protocol, or package interface:

- `MAJOR`: incompatible or breaking changes.
- `MINOR`: backward-compatible features.
- `PATCH`: backward-compatible bug fixes, docs, and maintenance changes.

For projects that are pre-1.0, document whether minor versions may include breaking changes.

Example policy:

> This project uses semantic versioning. Before 1.0, minor releases may include breaking changes, and release notes will call them out explicitly.

## Release Types

Common release types:

- Patch release: bug fixes, documentation corrections, small maintenance updates.
- Minor release: new backward-compatible functionality.
- Major release: breaking changes or migration-required behavior.
- Security release: vulnerability fix coordinated through the security policy.
- Pre-release: preview build for testing, such as `1.4.0-beta.1`.

## Pre-Release Checklist

Before publishing:

- Confirm the release scope is clear.
- Confirm CI passes on the release branch.
- Run the test suite locally if the project requires local verification.
- Review dependency changes.
- Review public API, CLI, configuration, and data format changes.
- Confirm documentation reflects changed behavior.
- Confirm examples still work.
- Update changelog or release notes.
- Confirm version number matches the change type.
- Confirm security-sensitive changes have been handled privately.

## Changelog Standards

Release notes should help users decide whether to upgrade.

Use sections such as:

- `Added`: new features.
- `Changed`: updates to existing behavior.
- `Deprecated`: features that will be removed later.
- `Removed`: removed features.
- `Fixed`: bug fixes.
- `Security`: vulnerability fixes or hardening.

Call out:

- Breaking changes.
- Required migrations.
- New minimum runtime or dependency versions.
- Contributor credits when appropriate.

Avoid vague entries such as "misc fixes" when the change affects users.

## Release Preparation Flow

1. Create or select a release branch.
2. Confirm all intended changes are merged.
3. Update version metadata.
4. Update changelog or draft release notes.
5. Run required checks.
6. Ask for maintainer review if required.
7. Tag the release.
8. Publish artifacts.
9. Publish release notes.
10. Announce the release in the project channels.

## Example Release Notes

```markdown
## 1.4.0 - 2026-07-08

### Added

- Added support for configuring project labels from a YAML file.

### Changed

- Improved pull request template guidance for documentation-only changes.

### Fixed

- Fixed release checklist ordering so version updates happen before tagging.

### Migration Notes

No migration is required.
```

## Security Release Flow

Security releases require more care than normal releases.

1. Receive the report through the private security channel.
2. Acknowledge receipt within the documented response window.
3. Confirm impact and affected versions.
4. Prepare a fix in a private branch or restricted fork if needed.
5. Request review from trusted maintainers only.
6. Publish patched versions.
7. Publish a security advisory after users can upgrade.
8. Credit the reporter if they want public credit.

Do not discuss suspected vulnerabilities in public issues before a fix or mitigation is available.

## Rollback Plan

Every release should have a rollback or mitigation plan.

If a release is bad:

- Stop promoting the release.
- Mark the release as problematic in release notes if the platform supports it.
- Publish a patch release when possible.
- Yank or deprecate the artifact only if the ecosystem supports it and the risk justifies it.
- Open a public issue explaining user impact when it is safe to do so.

Rollback communication should be factual and specific.

## Post-Release Checklist

After publishing:

- Verify installation from the public package or artifact.
- Verify the release tag and notes are visible.
- Verify documentation links point to the released version when applicable.
- Monitor issues, discussions, and error reports.
- Close or update tracking issues.
- Start a follow-up issue for known cleanup work.

## Release Owner Role

For each release, identify a release owner. The release owner is responsible for:

- Coordinating the checklist.
- Confirming version and changelog accuracy.
- Making the publish decision.
- Watching for immediate post-release problems.

The release owner does not need to do every task personally, but they own the outcome.
