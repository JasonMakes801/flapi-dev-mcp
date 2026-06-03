"""The canonical FLAPI enhancements repo — community/official scripts, shaders,
and tools, maintained by FilmLight at github.com/FilmLightAPI/enhancements.

`init` clones it to ~/.flapi-dev-mcp/repo/ as the primary git context source;
`update` git-pulls it. Additional context (e.g. Frame.io integrations) is added
separately via init's extra-source setting. Degrades gracefully offline.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from flapi_dev_mcp.config import REPO_DIR

REPO_URL = "https://github.com/FilmLightAPI/enhancements.git"


def _run(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(args, capture_output=True, text=True)


def is_cloned(dest: Path = REPO_DIR) -> bool:
    return (Path(dest) / ".git").is_dir()


def head_commit(dest: Path = REPO_DIR) -> str | None:
    if not is_cloned(dest):
        return None
    r = _run(["git", "-C", str(dest), "rev-parse", "--short", "HEAD"])
    return r.stdout.strip() or None


def clone_or_update(url: str = REPO_URL, dest: Path = REPO_DIR) -> dict:
    """Clone the repo if absent, else fast-forward pull. Never raises."""
    dest = Path(dest)
    if is_cloned(dest):
        # -c pull.rebase=false guards against a broken/deprecated global git
        # config (e.g. pull.rebase=preserve) that would otherwise fail the pull.
        r = _run(["git", "-C", str(dest), "-c", "pull.rebase=false", "pull", "--ff-only"])
        action = "pull"
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        r = _run(["git", "clone", url, str(dest)])
        action = "clone"
    return {
        "action": action,
        "ok": r.returncode == 0,
        "url": url,
        "path": str(dest),
        "commit": head_commit(dest),
        "message": (r.stderr or r.stdout).strip()[:500],
    }
