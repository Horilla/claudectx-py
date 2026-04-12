# claudectx-py

Python wrapper for [claudectx](https://github.com/Horilla/claudectx) — reduce Claude Code token usage by up to 80%.

## Install

```bash
pip install claudectx-py
```

This installs the `claudectx` command into your Python environment's PATH. The wrapper delegates to the underlying npm package, which must be installed separately:

```bash
npm install -g claudectx
# or
brew tap Horilla/claudectx && brew install claudectx
```

## Usage

Once both are installed, use `claudectx` exactly as you would from npm:

```bash
claudectx analyze                    # Token breakdown per context component
claudectx optimize --apply           # Auto-fix all token waste
claudectx report                     # 7-day usage analytics
claudectx watch                      # Live token dashboard
claudectx budget "src/**/*.py"       # Estimate cost before a big task
claudectx warmup                     # Pre-warm the Anthropic prompt cache
claudectx drift                      # Find stale CLAUDE.md references
claudectx compress                   # Compress session into MEMORY.md
claudectx teams export               # Export usage for team cost reporting
```

## Why a Python wrapper?

If your team uses Python-based tooling (pyenv, pip, Poetry, uv), this lets you add `claudectx` as a project dependency in `pyproject.toml` alongside your other dev tools — no separate npm install step in your CI.

```toml
[tool.poetry.dev-dependencies]
claudectx-py = "^1.1.2"
```

The wrapper is intentionally thin: it locates the `claudectx` binary on PATH and delegates all arguments to it. No logic is duplicated.

## Requirements

- Python 3.8+
- Node.js 18+ with `claudectx` installed globally (`npm install -g claudectx`)

## License

MIT — see [claudectx LICENSE](https://github.com/Horilla/claudectx/blob/master/LICENSE)
