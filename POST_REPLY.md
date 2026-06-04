All of the above is hopefully fixed. You can install straight from the git URL now (no clone needed):

```
uv tool install --reinstall git+https://github.com/JasonMakes801/flapi-dev-mcp
```
After that, updates are just `uv tool upgrade flapi-dev-mcp`, no more `uv cache clean`/`--reinstall` dance.

@**Sam Lempp** the second `_miss` crash is fixed too. Your null `flapi_python_path`/`active_venv` just means the FLAPI venv hasn't been built yet. It now detects a missing venv and offers to build it for you when you re-run `flapi-dev-mcp init` (also hopefully: I couldn't reproduce your exact null config, but I tested the missing-venv path).

@**Peter Postma** the 6.0-vs-Current default now follows `/Applications/Baselight/Current`, and the "Dev build roots" prompt is hidden behind `--dev` so it won't confuse end users.

Caveat: it's the middle of the night here and I got a bit obsessed with this. Tested as best I could locally, but it's really only been run on my one machine, so consider it midnight-oil code and expect a few rough edges.
