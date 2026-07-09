# Contributing to [Project Name]

Thank you for your interest in improving [Project Name]. This guide explains how to propose changes, set up the project locally, and submit pull requests maintainers can review efficiently.

## Project Scope

[Briefly describe what belongs in the project and what does not.]

Good contributions usually include:

- Bug fixes with a reproduction or test.
- Documentation improvements that remove confusion.
- Small features aligned with existing project direction.
- Maintenance improvements that reduce risk or complexity.

Open an issue before starting work on:

- New public APIs.
- Breaking changes.
- Large refactors.
- New dependencies.
- Changes to security, release, or governance policy.

## Code of Conduct

All project spaces follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). By participating, you agree to follow those expectations.

## Development Setup

### Requirements

- [Runtime and version]
- [Package manager]
- [Additional tools]

### Install Dependencies

```sh
[install command]
```

### Run Locally

```sh
[local run command]
```

### Run Checks

```sh
[test command]
[lint command]
[format command]
```

If a command is not available yet, document the manual verification maintainers expect.

## Issue Workflow

Before opening an issue:

- Search existing issues and discussions.
- Confirm you are using a supported version.
- Collect reproduction steps, logs, or screenshots when relevant.

Use issues for:

- Confirmed or suspected bugs.
- Feature proposals.
- Documentation problems.
- Project maintenance tasks.

Do not use public issues for security vulnerabilities. Follow [SECURITY.md](SECURITY.md).

## Pull Request Workflow

1. Open or find an issue for significant changes.
2. Fork the repository or create a branch.
3. Keep the change focused.
4. Add or update tests when behavior changes.
5. Update documentation when user-facing behavior changes.
6. Run the required checks.
7. Open a pull request with a clear summary and verification notes.

## Pull Request Checklist

Before requesting review, confirm:

- The change has a clear purpose.
- The pull request is limited to one topic.
- Tests, docs, or examples are updated where needed.
- Public behavior changes are described.
- Breaking changes are clearly marked.
- Required checks pass.

## Review Expectations

Maintainers review for:

- Fit with project scope.
- Correctness and maintainability.
- Compatibility and migration impact.
- Test coverage appropriate to the risk.
- Documentation quality.

Maintainers may ask for changes, suggest a different direction, or close a pull request that does not fit the project. Review comments marked `Required` must be addressed before merge.

## Commit Style

[Describe preferred commit style, if any. If the project does not require a specific convention, say so.]

Example:

```text
fix: handle empty configuration file
docs: clarify local setup
```

## Documentation Standards

Documentation changes should be:

- Accurate for the current version.
- Specific enough for a new user to follow.
- Free of unexplained internal shorthand.
- Updated alongside behavior changes.

Prefer one working example over several incomplete examples.

## Testing Standards

Add tests when:

- Fixing a bug.
- Adding behavior.
- Changing parsing, validation, security, or compatibility logic.
- Refactoring code with meaningful risk.

If tests are not practical, explain the manual verification in the pull request.

## Maintainer Response Windows

[State realistic response expectations, such as "Maintainers review issues weekly" or "This project is maintained best-effort."]

Please do not ping maintainers repeatedly unless the issue is urgent, security-sensitive, or blocking a release.

## Recognition

Contributors may be credited in release notes when their work ships. If you prefer not to be named publicly, mention that in your pull request.
