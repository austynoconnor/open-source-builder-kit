# CLI Recipes

These recipes show practical ways maintainers can use Open Source Builder Kit during normal project work.

## Review a Project Before Asking for Help

Create a starter manifest for a project:

```bash
osbk init-manifest --name "My Project" --repository "https://github.com/me/my-project" --description "What the project helps people do." --output work/my-project.yml
```

Run a health score first so the project has a clear baseline:

```bash
osbk health examples/project-profiles/civic-data-commons.manifest.json
```

Use JSON output when another script needs to read the score:

```bash
osbk health examples/project-profiles/civic-data-commons.manifest.json --json
```

Then generate a report that can be attached to an issue, planning note, or maintainer discussion:

```bash
osbk report examples/project-profiles/civic-data-commons.manifest.json --output work/civic-data-commons-report.md
```

## Turn Health Gaps Into Contributor Work

Use `tasks` when a maintainer knows the project needs help but does not yet have well-scoped issues:

```bash
osbk tasks examples/project-profiles/civic-data-commons.manifest.json --limit 5 --output work/contributor-tasks.md
```

The output is intentionally reviewable Markdown. Maintainers should edit it before opening public issues.

## Build a Maintainer Roadmap

Create a roadmap from the same health signals:

```bash
osbk roadmap examples/project-profiles/civic-data-commons.manifest.json --output work/roadmap.md
```

The generated roadmap is a starting point for maintainer planning. It groups work by urgency and includes a review cadence.

## Generate Reports for Multiple Projects

Use a batch file when reviewing multiple community projects or examples:

```bash
osbk batch-report data/demo-inputs/cli-batch.json --output-dir work/reports
```

Each job in the batch file points at a manifest and produces one Markdown report.

## Validate Demo Content

Run this before publishing changes to examples:

```bash
osbk validate-examples
```

This confirms each example manifest can be loaded and scored.

## Prepare for a Release

Generate a release checklist before tagging:

```bash
osbk checklist release --output work/release-checklist.md
```

Use the checklist as a working document. It should not replace maintainer judgment, but it helps avoid missed documentation, testing, and release-note steps.

## Bootstrap Community Files

Copy starter community files into another project:

```bash
osbk scaffold ../my-open-source-project
```

Review every generated file before publishing. Templates are meant to accelerate maintainer work, not pretend every project has the same governance model.
