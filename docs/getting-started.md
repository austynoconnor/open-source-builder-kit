# Getting Started with Open Source Builder Kit

Open Source Builder Kit is a practical documentation and governance starter set for maintainers who want their project to be easier to adopt, contribute to, support, and release.

Use this guide to turn the kit into a working project foundation in under an hour.

## What This Kit Helps You Build

The kit is designed for maintainers who need clear operating defaults without turning the repository into a process-heavy organization. It focuses on four outcomes:

- New users can understand what the project does and try it quickly.
- New contributors can find safe, useful work and submit changes with confidence.
- Maintainers can triage issues, review pull requests, and publish releases consistently.
- The community has explicit expectations for conduct, security, support, and decision-making.

## Repository Setup Checklist

Start with the templates in `templates/`, then adapt them to your project:

1. Copy `templates/README-template.md` to `README.md`.
2. Copy `templates/CONTRIBUTING-template.md` to `CONTRIBUTING.md`.
3. Copy `templates/CODE_OF_CONDUCT-template.md` to `CODE_OF_CONDUCT.md`.
4. Copy `templates/SECURITY-template.md` to `SECURITY.md`.
5. Replace every placeholder wrapped in square brackets, such as `[Project Name]`.
6. Delete sections that do not apply yet instead of leaving vague promises.
7. Link the finished files from the README so users can find them.

Recommended repository files:

- `README.md`: product explanation, quick start, usage examples, support links.
- `CONTRIBUTING.md`: local setup, issue workflow, pull request expectations.
- `CODE_OF_CONDUCT.md`: behavioral standard and reporting process.
- `SECURITY.md`: supported versions and private vulnerability reporting.
- `LICENSE`: open-source license terms.
- `CHANGELOG.md`: release history, if the project publishes versions.

## First Hour Implementation Plan

Use this sequence when starting from a new or under-documented repository.

### 1. Define the Maintainer Promise

Write a short answer to each question before editing files:

- Who is this project for?
- What problem does it solve?
- What does the project intentionally not solve?
- What is the expected support level?
- What kinds of contributions are welcome now?

These answers should appear in the README and CONTRIBUTING files. Clear boundaries prevent user frustration and reduce maintainer load.

### 2. Create a Useful README

Your README should let a qualified user decide whether to keep reading in less than two minutes. Prioritize:

- A plain-language project description.
- Installation or setup steps that have been tested on a clean machine.
- One complete working example.
- Links to contribution, conduct, security, and release information.
- Project status, such as experimental, stable, or maintenance mode.

Avoid treating the README as a marketing page. It should answer the user's operational questions first.

### 3. Make Contributions Predictable

Good contribution docs reduce back-and-forth. Include:

- How to set up the local environment.
- How to run tests, linting, formatting, and build checks.
- What kind of changes need an issue before a pull request.
- How maintainers evaluate pull requests.
- What contributors can expect after opening a pull request.

If the project is small, keep the process lightweight. Predictable does not mean bureaucratic.

### 4. Set Community Health Defaults

Add a code of conduct and security policy before the project has a problem. These files are not just formalities; they tell contributors and users how serious the project is about trust.

At minimum, define:

- Acceptable and unacceptable behavior.
- How to report conduct issues.
- How to report security vulnerabilities privately.
- Which versions receive security fixes.
- Expected response times, only if you can honor them.

### 5. Establish Release Discipline

Even small projects benefit from a release checklist. Decide:

- How versions are numbered.
- What must be true before a release.
- Where release notes are written.
- Who can publish a release.
- What happens when a release has to be rolled back.

Use `docs/release-guide.md` as your operating procedure.

## Suggested Labels

These labels help contributors self-select work and help maintainers triage quickly:

- `bug`: confirmed or likely defect.
- `documentation`: docs-only change.
- `enhancement`: user-facing improvement.
- `good first issue`: small, well-scoped contributor task.
- `help wanted`: useful contribution with enough context to start.
- `needs reproduction`: issue needs a minimal example or more details.
- `question`: support or clarification request.
- `security`: security-sensitive tracking item, used only for public-safe metadata.
- `blocked`: waiting on a dependency, decision, or external action.
- `breaking change`: change requires migration or compatibility review.

## Minimum Governance Model

For early-stage projects, a simple governance model is usually enough:

- Maintainers own final decisions.
- Significant changes should be discussed in an issue before implementation.
- Pull requests require at least one maintainer review.
- Security reports are handled privately.
- Releases are approved by a maintainer.

Document stricter rules only when the project needs them.

## Quality Bar

Before announcing the project or inviting contributors, verify:

- A new user can install and run the project from the README alone.
- A new contributor can find setup, test, and pull request instructions.
- The project states its license.
- There is a private path for security reports.
- Community behavior expectations are visible.
- Maintainers have a release checklist.

The goal is not perfect process. The goal is a repository that feels cared for, clear, and credible.
