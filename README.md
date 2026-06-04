# FLAPI Developer MCP

A local MCP server for Claude Code that makes Claude an expert FLAPI (FilmLight
Baselight) developer. It discovers your local Baselight installation, gathers
FLAPI context, scaffolds scripts with the right boilerplate, and runs them to
verify they work. macOS + Python only for v1.

See [CLAUDE.md](CLAUDE.md) for the full design spec.

## Status

Step 1 (skeleton) is in place: a stdio MCP server exposing a single `flapi_dev_ping`
connectivity tool, plus a CLI with stubbed `init` / `update` / `config` subcommands.

## Install (macOS, via uv)

This ships as a [uv](https://docs.astral.sh/uv/) tool: uv builds an isolated
environment for the server and puts the `flapi-dev-mcp` command on your PATH, so
there's no venv to manage by hand.

```bash
# 1. Install uv if you don't have it:
brew install uv                      # or: curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install the server as a tool, straight from the git URL:
uv tool install git+https://github.com/JasonMakes801/flapi-dev-mcp
uv tool update-shell                 # one-time: puts the command on PATH (restart your shell)

# 3. Onboard (discovers Baselight, clones the examples repo, writes config):
flapi-dev-mcp init

# 4. Register with Claude Code (available in all your projects):
claude mcp add --scope user flapi-dev flapi-dev-mcp
```

Then open Claude Code in any folder and ask it to write a FLAPI script.

## Updating

```bash
uv tool upgrade flapi-dev-mcp        # pulls the latest release
# if a change doesn't show up, force a clean re-fetch:
uv tool install --reinstall git+https://github.com/JasonMakes801/flapi-dev-mcp
```

## Contributing

For development, an editable install in a local venv is convenient:

```bash
uv venv && uv pip install -e .       # or: python3.12 -m venv .venv && .venv/bin/pip install -e .
```
