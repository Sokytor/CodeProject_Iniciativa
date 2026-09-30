#!/usr/bin/env python3
"""Check discoverability, portable resources, and the pinned runtime."""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys


def verify(root):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    agents = root / 'AGENTS.md'
    require(agents.exists() and '<!-- SOKYTOR_CLOUD_START -->' in agents.read_text(), 'Missing project rules')
    require((root / '.agents/cloud/COMPATIBILITY.md').is_file(), 'Missing dependency and connector guidance')
    require('.agents/' in json.loads((root / 'codegraph.json').read_text()).get('exclude', []), 'Skill resources must not crowd out the project index')
    package = json.loads((root / '.agents/cloud/codegraph/package.json').read_text())
    lock = json.loads((root / '.agents/cloud/codegraph/package-lock.json').read_text())
    pin = package['dependencies']['@colbymchenry/codegraph']
    require(pin == '1.6.0', 'Unexpected CodeGraph version')
    require(lock['packages']['']['dependencies']['@colbymchenry/codegraph'] == pin, 'Lockfile does not match the runtime pin')
    for platform in ['linux-x64', 'linux-arm64']:
        key = 'node_modules/@colbymchenry/codegraph-' + platform
        require(key in lock['packages'] and lock['packages'][key]['version'] == pin, 'Missing locked Linux runtime: ' + platform)
    sources = json.loads((root / '.agents/cloud/sources.json').read_text())
    skills = list((root / '.agents/skills').glob('*/SKILL.md'))
    expected = set(sources['public_skills']['names'] + sources['adapted_skills'] + ['codegraph-cloud', 'sokytor-github-cloud'])
    require({p.parent.name for p in skills} == expected, 'Incomplete skill collection')
    names = set()
    for p in skills:
        text = p.read_text()
        require(text.startswith('---\n') and '\n---\n' in text[4:], 'Invalid skill frontmatter: ' + str(p))
        front = text.split('---', 2)[1]
        name_match = re.search(r'^name:\s*["\']?([a-z0-9-]+)', front, re.M)
        require(bool(name_match), 'Missing skill name: ' + str(p))
        if name_match:
            name = name_match.group(1)
            require(name not in names, 'Duplicate skill name: ' + name)
            names.add(name)
        require(bool(re.search(r'^description:\s*\S', front, re.M)), 'Missing skill description: ' + str(p))
        prose = re.sub(r'(?m)^```[^\n]*\n.*?^```\s*$', '', text, flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', prose):
            target = target.split('#', 1)[0]
            if not target or '://' in target or target.startswith(('/', '$', '<')):
                continue
            require((p.parent / target).exists(), 'Missing skill resource: ' + str(p.parent / target))
    for name in sources['public_skills']['names']:
        require((root / '.agents/skills' / name / 'LICENSE.txt').is_file(), 'Missing upstream license: ' + name)
    for p in (root / 'tools').glob('*.py'):
        ast.parse(p.read_text(), filename=str(p))
    for path in ['.agents/cloud/bootstrap.sh', '.agents/bin/codegraph']:
        require(subprocess.run(['bash', '-n', str(root / path)], capture_output=True).returncode == 0, 'Invalid shell script: ' + path)
        require((root / path).stat().st_mode & 0o111, 'Script is not executable: ' + path)
    if (root / '.git').exists():
        receipt = json.loads((root / '.agents/sokytor-kit.json').read_text())
        tracked = set(subprocess.check_output(['git', '-C', str(root), 'ls-files'], text=True).splitlines())
        if '.agents/sokytor-kit.json' in tracked:
            missing = set(receipt['files']) - tracked
            require(not missing, 'Kit files are not tracked by Git: ' + ', '.join(sorted(missing)))
    if errors:
        raise ValueError('\n'.join(errors))
    return {'skills': len(skills), 'codegraph_version': pin, 'rules': 'ok', 'resources': 'ok'}


if __name__ == '__main__':
    try:
        print(json.dumps(verify(Path(__file__).resolve().parent.parent)))
    except (ValueError, OSError, KeyError, SyntaxError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
