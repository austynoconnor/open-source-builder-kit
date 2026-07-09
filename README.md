# Open Source Builder Kit

Practical tools, templates, and playbooks for people who maintain open-source projects without a large platform team behind them.

This repository is designed around one goal: make healthy open-source maintenance easier to repeat. It helps maintainers assess community health, generate contributor-facing docs, create release checklists, and turn project metadata into useful reports.

## What is included

- `osbk health`: score a project manifest against community health signals.
- `osbk report`: generate a Markdown health report from project metadata.
- `osbk checklist`: create maintainer checklists for releases, issue triage, docs, and onboarding.
- `osbk scaffold`: copy reusable community templates into a project.
- `templates/`: README, contributing, security, and code of conduct templates.
- `docs/`: maintainer playbooks and practical guidance.
- `examples/`: demo manifests and sample reports.

## Why this helps open source

Small maintainers often lose time to repeated non-code work: unclear contribution paths, thin documentation, inconsistent issue triage, and manual release steps. This kit turns those maintenance patterns into repeatable assets that any project can adapt.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
osbk --help
osbk health examples/project-profiles/civic-data-commons.manifest.json
osbk report examples/project-profiles/civic-data-commons.manifest.json --output work/civic-data-commons-report.md
osbk batch-report data/demo-inputs/cli-batch.json --output-dir work/reports
```

No API keys are required for the core tools.

## Project manifest

The CLI reads a small YAML or JSON manifest:

```yaml
name: Community Notes Toolkit
repository: https://github.com/example/community-notes-toolkit
description: Shared templates and workflows for community documentation.
license: MIT
maintainers:
  - name: Example Maintainer
    role: Lead maintainer
signals:
  readme: true
  contributing: true
  code_of_conduct: true
  security_policy: true
  issue_templates: true
  ci: true
  tests: true
  release_notes: false
  roadmap: true
```

## Design principles

- Useful before it is clever.
- Clear enough for first-time contributors.
- Respectful of maintainers' limited time.
- Automation should produce reviewable text, not hide decisions.
- Templates should invite real community standards, not legal theater.

## Repository status

This is an early public toolkit. The initial focus is practical maintainer operations: docs, reports, checklists, and community scaffolding.
