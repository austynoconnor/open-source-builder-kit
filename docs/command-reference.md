# Command Reference

Open Source Builder Kit exposes the `osbk` command.

## `osbk health`

Score a project manifest and list missing community-health signals.

```bash
osbk health examples/project-profiles/civic-data-commons.manifest.json
osbk health examples/project-profiles/civic-data-commons.manifest.json --json
```

## `osbk init-manifest`

Create a starter JSON or YAML manifest.

```bash
osbk init-manifest --name "My Project" --repository "https://github.com/me/my-project" --description "What the project helps people do." --output work/my-project.yml
```

## `osbk report`

Generate a Markdown health report.

```bash
osbk report examples/project-profiles/civic-data-commons.manifest.json --output work/report.md
```

## `osbk batch-report`

Generate reports for every job in a batch file.

```bash
osbk batch-report data/demo-inputs/cli-batch.json --output-dir work/reports
```

## `osbk compare`

Compare multiple project manifests in one Markdown table.

```bash
osbk compare examples/project-profiles/civic-data-commons.manifest.json examples/project-profiles/learning-lab-toolkit.manifest.json
```

## `osbk tasks`

Suggest contributor tasks from missing health signals.

```bash
osbk tasks examples/project-profiles/civic-data-commons.manifest.json --limit 3
```

## `osbk issue-plan`

Create GitHub issue drafts from suggested health work.

```bash
osbk issue-plan examples/project-profiles/civic-data-commons.manifest.json --limit 3 --output work/issues.md
```

## `osbk roadmap`

Generate a maintainer roadmap.

```bash
osbk roadmap examples/project-profiles/civic-data-commons.manifest.json --output work/roadmap.md
```

## `osbk survey-summary`

Summarize maintainer survey CSV data.

```bash
osbk survey-summary data/demo-inputs/maintainer-survey.csv --output work/survey-summary.md
```

## `osbk labels`

Print recommended GitHub labels as YAML or JSON.

```bash
osbk labels --format yaml --output work/labels.yml
```

## `osbk support-policy`

Generate a project support policy from a manifest.

```bash
osbk support-policy examples/project-profiles/civic-data-commons.manifest.json --output work/SUPPORT.md
```

## `osbk release-notes`

Draft release notes from a manifest.

```bash
osbk release-notes examples/project-profiles/civic-data-commons.manifest.json --version v0.1.0 --output work/release-notes.md
```

## `osbk scaffold`

Copy community templates into another project.

```bash
osbk scaffold ../my-open-source-project
```

## `osbk doctor`

Check a repository for key community files.

```bash
osbk doctor .
```

## `osbk validate-examples`

Validate example manifests in this repository.

```bash
osbk validate-examples
```

