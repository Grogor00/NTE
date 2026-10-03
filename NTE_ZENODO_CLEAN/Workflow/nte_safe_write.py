# -*- coding: utf-8 -*-
"""Atomic text write for NTE corpus files.

Why: pathlib.Path.write_text(..., newline=bad) opens with mode 'w' (truncate)
*before* validating newline, leaving a 0-byte file on ValueError. Seen
2026-09-30 on NTE_Workflow_Manifest_v10_18.md.

Usage:
  from nte_safe_write import safe_write_text
  safe_write_text(path, text, min_bytes=1000)  # refuse tiny overwrite of large file
"""
from __future__ import annotations

import os
from pathlib import Path


def safe_write_text(
    path: str | Path,
    text: str,
    *,
    encoding: str = "utf-8",
    min_bytes: int | None = None,
    backup_suffix: str | None = ".bak",
) -> Path:
    """Write *text* to *path* via same-dir tempfile + os.replace.

    If *path* already exists and *min_bytes* is set, refuse to replace when
    the new payload would be shorter than *min_bytes* (guards against
    accidental wipe of the Manifest / Parts).

    If *backup_suffix* is set and *path* exists, copy current bytes to
    path+suffix before replace (best-effort; non-fatal if copy fails).
    """
    path = Path(path)
    data = text if isinstance(text, str) else str(text)
    payload = data.encode(encoding)
    if min_bytes is not None and path.exists() and len(payload) < min_bytes:
        raise ValueError(
            f"safe_write_text refused: new payload {len(payload)} bytes "
            f"< min_bytes={min_bytes} for {path} (would risk wipe)"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    if backup_suffix and path.exists():
        try:
            bak = path.with_name(path.name + backup_suffix)
            bak.write_bytes(path.read_bytes())
        except OSError:
            pass
    tmp = path.with_name(path.name + ".tmp")
    try:
        with open(tmp, "wb") as f:
            f.write(payload)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except Exception:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
        raise
    return path


if __name__ == "__main__":
    import tempfile

    d = Path(tempfile.mkdtemp())
    p = d / "demo.md"
    p.write_text("ORIGINAL", encoding="utf-8")
    safe_write_text(p, "REPLACED SAFELY\n", min_bytes=1)
    assert p.read_text(encoding="utf-8") == "REPLACED SAFELY\n"
    print("nte_safe_write self-check OK", p, p.stat().st_size)
