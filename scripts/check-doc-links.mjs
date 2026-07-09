import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { extname, dirname, join, normalize, relative, resolve, sep } from 'node:path';

const root = process.cwd();
const checkExternal = process.env.CHECK_EXTERNAL_LINKS === 'true';
const ignoredDirs = new Set(['.git', 'node_modules', 'dist', 'build', 'coverage', '.next', '.turbo', '__pycache__', 'templates']);
const markdownFiles = [];
const failures = [];

function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!ignoredDirs.has(entry.name)) {
        walk(join(dir, entry.name));
      }
      continue;
    }

    if (entry.isFile() && ['.md', '.mdx'].includes(extname(entry.name).toLowerCase())) {
      markdownFiles.push(join(dir, entry.name));
    }
  }
}

function stripAnchor(link) {
  const index = link.indexOf('#');
  return index === -1 ? link : link.slice(0, index);
}

function isSkippable(link) {
  return (
    !link ||
    link.startsWith('#') ||
    link.startsWith('mailto:') ||
    link.startsWith('tel:') ||
    link.startsWith('sms:') ||
    link.startsWith('javascript:') ||
    link.startsWith('data:') ||
    link.includes('{{') ||
    link.includes('}}')
  );
}

function extractLinks(content) {
  const links = [];
  const markdownLinkPattern = /!?\[[^\]]*]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;
  const htmlHrefPattern = /\bhref=["']([^"']+)["']/g;
  let match;

  while ((match = markdownLinkPattern.exec(content)) !== null) {
    links.push(match[1]);
  }

  while ((match = htmlHrefPattern.exec(content)) !== null) {
    links.push(match[1]);
  }

  return links;
}

async function checkHttpLink(link, source) {
  if (!checkExternal || !/^https?:\/\//i.test(link)) {
    return;
  }

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10000);

  try {
    let response = await fetch(link, {
      method: 'HEAD',
      redirect: 'follow',
      signal: controller.signal,
      headers: { 'user-agent': 'open-source-builder-kit-link-checker' },
    });

    if ([403, 405].includes(response.status)) {
      response = await fetch(link, {
        method: 'GET',
        redirect: 'follow',
        signal: controller.signal,
        headers: { 'user-agent': 'open-source-builder-kit-link-checker' },
      });
    }

    if (response.status >= 400) {
      failures.push(`${source}: ${link} returned HTTP ${response.status}`);
    }
  } catch (error) {
    failures.push(`${source}: ${link} could not be reached (${error.message})`);
  } finally {
    clearTimeout(timeout);
  }
}

function checkLocalLink(link, file) {
  if (/^[a-z][a-z0-9+.-]*:/i.test(link) || link.startsWith('//')) {
    return;
  }

  let withoutAnchor;
  try {
    withoutAnchor = stripAnchor(decodeURIComponent(link));
  } catch {
    failures.push(`${file}: ${link} is not valid URL encoding`);
    return;
  }

  if (!withoutAnchor) {
    return;
  }

  const sourceDir = dirname(file);
  const target = normalize(withoutAnchor.startsWith('/') ? join(root, withoutAnchor) : join(sourceDir, withoutAnchor));
  const resolvedTarget = resolve(target);
  const relativeTarget = relative(root, resolvedTarget);

  if (relativeTarget === '..' || relativeTarget.startsWith(`..${sep}`)) {
    failures.push(`${file}: ${link} resolves outside the repository`);
    return;
  }

  if (existsSync(resolvedTarget)) {
    return;
  }

  if (existsSync(`${resolvedTarget}.md`) || existsSync(`${resolvedTarget}.mdx`)) {
    return;
  }

  if (existsSync(dirname(resolvedTarget))) {
    const base = resolvedTarget.split(/[\\/]/).pop();
    const sibling = readdirSync(dirname(resolvedTarget)).find((name) => name.toLowerCase() === base.toLowerCase());
    if (sibling) {
      failures.push(`${file}: ${link} differs by case from ${sibling}`);
      return;
    }
  }

  failures.push(`${file}: ${link} does not resolve to a local file`);
}

walk(root);

for (const file of markdownFiles) {
  const content = readFileSync(file, 'utf8');
  const links = extractLinks(content);

  for (const link of links) {
    if (isSkippable(link)) {
      continue;
    }

    checkLocalLink(link, file);
    await checkHttpLink(link, file);
  }
}

if (markdownFiles.length === 0) {
  console.log('No Markdown files found; skipping documentation link checks.');
} else {
  console.log(`Checked links in ${markdownFiles.length} Markdown file(s).`);
}

if (failures.length > 0) {
  console.error('\nDocumentation link check failed:');
  for (const failure of failures) {
    console.error(`- ${failure}`);
  }
  process.exit(1);
}
