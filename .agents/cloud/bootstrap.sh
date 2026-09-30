#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
runtime_dir="${CODEX_CODEGRAPH_RUNTIME:-$repo_root/.agents/.runtime/codegraph}"
cli="$runtime_dir/node_modules/.bin/codegraph"
export DO_NOT_TRACK=1 CODEGRAPH_TELEMETRY=0 CODEGRAPH_NO_UPDATE_CHECK=1 CODEGRAPH_NO_DOWNLOAD=1

if [[ ! -x "$cli" ]] || [[ "$("$cli" --version 2>/dev/null)" != "1.6.0" ]]; then
  command -v npm >/dev/null || { echo 'CodeGraph necesita npm en el entorno de preparación.' >&2; exit 1; }
  mkdir -p "$runtime_dir"
  cp "$script_dir/codegraph/package.json" "$runtime_dir/package.json"
  cp "$script_dir/codegraph/package-lock.json" "$runtime_dir/package-lock.json"
  npm ci --prefix "$runtime_dir" --include=optional --ignore-scripts --no-audit --no-fund
fi

"$cli" --version
if [[ -f "$repo_root/.codegraph/codegraph.db" ]]; then
  "$cli" sync "$repo_root"
else
  "$cli" init --yes "$repo_root"
fi
"$cli" status "$repo_root"
printf '\nCodeGraph listo. Consulta: .agents/bin/codegraph explore "archivo o símbolos"\n'
