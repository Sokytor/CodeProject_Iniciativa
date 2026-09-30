#!/usr/bin/env python3
"""Apply the portable Codex kit while preserving project-specific content."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

KIT_ROOT = Path(__file__).resolve().parent.parent
START = '<!-- SOKYTOR_CLOUD_START -->'
END = '<!-- SOKYTOR_CLOUD_END -->'
IGNORE_BLOCK = '\n# Sokytor Codex Cloud: generated tools and index\n.codegraph/\n.agents/.runtime/\n.agents/**/__pycache__/\n'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_files():
    paths = []
    for folder in ['.agents/bin', '.agents/cloud', '.agents/skills', 'tools', '.github/workflows']:
        root = KIT_ROOT / folder
        if root.exists():
            paths.extend(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    return sorted(paths)


def apply(target, check=False):
    target = target.resolve()
    if target == Path.home() or target == Path(target.anchor):
        raise ValueError('Choose a project directory, not a home or filesystem root')
    if not target.is_dir():
        raise ValueError(f'Project directory does not exist: {target}')
    receipt_path = target / '.agents/sokytor-kit.json'
    old = json.loads(receipt_path.read_text()) if receipt_path.exists() else {}
    old_hashes = old.get('files', {})
    planned, conflicts, hashes = [], [], {}
    for src in source_files():
        relative = str(src.relative_to(KIT_ROOT))
        dst = target / relative
        desired = src.read_bytes()
        hashes[relative] = digest(desired)
        if dst.exists():
            current = dst.read_bytes()
            if current == desired:
                continue
            if relative not in old_hashes or digest(current) != old_hashes[relative]:
                conflicts.append(relative)
                continue
        planned.append((dst, desired, src.stat().st_mode & 0o777))

    agents = target / 'AGENTS.md'
    original = agents.read_text() if agents.exists() else '# Instrucciones del proyecto\n'
    block = (KIT_ROOT / '.agents/cloud/AGENTS-block.md').read_text().strip()
    if START in original or END in original:
        if original.count(START) != 1 or original.count(END) != 1:
            conflicts.append('AGENTS.md: malformed managed block')
            desired_agents = original
        else:
            desired_agents = re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda _: block, original, flags=re.S)
    else:
        desired_agents = original.rstrip() + '\n\n' + block + '\n'
    if desired_agents != original:
        planned.append((agents, desired_agents.encode(), 0o644))

    ignore = target / '.gitignore'
    old_ignore = ignore.read_text() if ignore.exists() else ''
    if '# Sokytor Codex Cloud: generated tools and index' not in old_ignore:
        planned.append((ignore, (old_ignore.rstrip() + '\n' + IGNORE_BLOCK).encode(), 0o644))

    config_path = target / 'codegraph.json'
    config = json.loads(config_path.read_text()) if config_path.exists() else {}
    if not isinstance(config, dict) or not isinstance(config.get('exclude', []), list):
        raise ValueError('Invalid existing codegraph.json; merge it manually')
    excludes = config.get('exclude', [])
    if '.agents/' not in excludes:
        config['exclude'] = excludes + ['.agents/']
        planned.append((config_path, (json.dumps(config, indent=2, ensure_ascii=False) + '\n').encode(), 0o644))

    receipt = {'version': '1.0.0', 'template': 'https://github.com/Sokytor/codex-project-template', 'files': hashes}
    receipt_bytes = (json.dumps(receipt, indent=2, ensure_ascii=False) + '\n').encode()
    if not receipt_path.exists() or receipt_path.read_bytes() != receipt_bytes:
        planned.append((receipt_path, receipt_bytes, 0o644))
    if conflicts:
        raise ValueError('Personalized files preserved; resolve conflicts before applying: ' + ', '.join(conflicts))
    if not check:
        for dst, data, mode in planned:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(data)
            dst.chmod(mode)
    return {'project': str(target), 'changes': len(planned), 'check_only': check, 'skills': len(list((KIT_ROOT / '.agents/skills').glob('*/SKILL.md')))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('--check', action='store_true', help='Report changes without writing files')
    args = parser.parse_args()
    try:
        print(json.dumps(apply(args.project, args.check), ensure_ascii=False))
    except (ValueError, OSError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
