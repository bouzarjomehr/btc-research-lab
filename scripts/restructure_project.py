import os
import shutil
from pathlib import Path

ROOT = Path(".").resolve()

# -----------------------------
# 1. Define new structure
# -----------------------------
STRUCTURE = [
    "notebooks/hypotheses",
    "data/signals",
    "data/backtests",
    "data/equity",
    "reports",
    "strategies",
    "scripts"
]

def create_dirs():
    for path in STRUCTURE:
        full_path = ROOT / path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"[OK] ensured: {full_path}")

# -----------------------------
# 2. Safe move helper
# -----------------------------
def safe_move(src, dst):
    src_path = ROOT / src
    dst_path = ROOT / dst

    if not src_path.exists():
        return

    dst_path.parent.mkdir(parents=True, exist_ok=True)

    # prevent overwrite
    if dst_path.exists():
        print(f"[SKIP] exists: {dst_path}")
        return

    shutil.move(str(src_path), str(dst_path))
    print(f"[MOVED] {src} -> {dst}")

# -----------------------------
# 3. Migration rules (legacy cleanup)
# -----------------------------
def migrate_existing_files():
    # reports cleanup (optional normalization)
    reports_dir = ROOT / "reports"

    if reports_dir.exists():
        for f in reports_dir.glob("*"):
            if f.is_file():
                new_name = f.name.replace(" ", "_")
                target = reports_dir / new_name

                if not target.exists() and new_name != f.name:
                    f.rename(target)
                    print(f"[RENAMED] {f.name} -> {new_name}")

    # signals/backtests/equity already OK (just ensure folder exists)
    print("[INFO] No destructive migration applied")

# -----------------------------
# 4. Validate structure
# -----------------------------
def validate():
    required = [
        "data/signals",
        "data/backtests",
        "data/equity",
        "reports",
        "notebooks/hypotheses"
    ]

    print("\n=== STRUCTURE CHECK ===")
    for r in required:
        exists = (ROOT / r).exists()
        print(r, "OK" if exists else "MISSING")

# -----------------------------
# 5. Main
# -----------------------------
if __name__ == "__main__":
    print("=== BTC RESEARCH LAB RESTRUCTURE START ===\n")

    create_dirs()
    migrate_existing_files()
    validate()

    print("\n=== DONE ===")