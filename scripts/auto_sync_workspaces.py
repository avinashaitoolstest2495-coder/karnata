"""auto_sync_workspaces.py — Universal Workspace Synchronizer for Karnata.in"""
import os, shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if BASE_DIR.name == "namma-karnataka":
    SUB_DIR = BASE_DIR
    ROOT_DIR = BASE_DIR.parent
else:
    ROOT_DIR = BASE_DIR
    SUB_DIR = BASE_DIR / "namma-karnataka"

IGNORE_DIRS = {".git", "node_modules", "scratch", "logs", ".system_generated", "__pycache__", ".wrangler", ".vscode"}

def sync_directories(src: Path, dst: Path):
    if not src.exists() or not dst.exists(): return 0
    synced = 0
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not (src == ROOT_DIR and d == "namma-karnataka")]
        rel = os.path.relpath(root, src)
        target_dir = dst / rel if rel != "." else dst
        target_dir.mkdir(parents=True, exist_ok=True)
        for f in files:
            sf = Path(root) / f
            df = target_dir / f
            if not df.exists() or (sf.stat().st_mtime > df.stat().st_mtime and sf.stat().st_size != df.stat().st_size):
                try:
                    shutil.copy2(sf, df)
                    synced += 1
                except Exception: pass
    return synced

def sync_all():
    if not SUB_DIR.exists(): return
    c1 = sync_directories(ROOT_DIR, SUB_DIR)
    c2 = sync_directories(SUB_DIR, ROOT_DIR)
    if c1 + c2 > 0:
        print(f"[AUTO-SYNC] Synced {c1 + c2} files across workspace directories.")
    else:
        print("[AUTO-SYNC] Workspace directories are in sync.")

if __name__ == "__main__":
    sync_all()