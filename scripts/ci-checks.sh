#!/usr/bin/env bash
set -euo pipefail

ran_checks=false

if [[ -f pyproject.toml ]]; then
  echo "Python project detected; installing development dependencies."
  python -m pip install --upgrade pip
  python -m pip install -e ".[dev]"

  echo "Running ruff."
  python -m ruff check .

  echo "Running pytest."
  python -m pytest
  ran_checks=true
fi

if [[ -f package.json ]]; then
  echo "Node project detected; installing dependencies."

  if [[ -f package-lock.json || -f npm-shrinkwrap.json ]]; then
    npm ci
  elif [[ -f pnpm-lock.yaml ]]; then
    corepack enable pnpm
    pnpm install --frozen-lockfile
  elif [[ -f yarn.lock ]]; then
    corepack enable yarn
    yarn install --immutable
  else
    npm install
  fi

  node <<'NODE'
const { readFileSync } = require('node:fs');
const { spawnSync } = require('node:child_process');

const pkg = JSON.parse(readFileSync('package.json', 'utf8'));
const scripts = pkg.scripts || {};
const packageManager = pkg.packageManager || '';
const runner = packageManager.startsWith('pnpm@')
  ? ['pnpm', ['run']]
  : packageManager.startsWith('yarn@')
    ? ['yarn', []]
    : ['npm', ['run']];

for (const name of ['lint', 'test']) {
  if (!scripts[name]) {
    console.log(`No "${name}" script found; skipping.`);
    continue;
  }

  const [command, baseArgs] = runner;
  const args = [...baseArgs, name];
  console.log(`Running ${command} ${args.join(' ')}`);
  const result = spawnSync(command, args, { stdio: 'inherit', shell: process.platform === 'win32' });
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}
NODE
  ran_checks=true
fi

if [[ "$ran_checks" == false ]]; then
  echo "No supported project manifest found; skipping lint/test checks."
fi
