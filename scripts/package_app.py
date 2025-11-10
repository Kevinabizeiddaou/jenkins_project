"""
Create a tiny 'dist' artifact to simulate packaging.
"""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

# Copy the app file as our "package"
shutil.copy2(ROOT / "app.py", DIST / "app.py")

# Also export a VERSION file
with open(DIST / "VERSION", "w", encoding="utf-8") as f:
    f.write("0.1.0\n")

print(f"Packaged artifacts in: {DIST}")
