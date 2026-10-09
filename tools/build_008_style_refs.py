#!/usr/bin/env python3
"""Extract eight unchanged source-image frames from the user-approved 008 digestion longform.

Usage:
    python tools/build_008_style_refs.py "/path/to/final-video(10).mp4"

Requires ffmpeg on PATH. Does not invent, recolor or style-transfer frames.
Writes to assets/channel/references/video008/ (no large MP4 needed in Git).
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys

SHOTS = [
    (18, "008_01_organ_transport.jpg"),
    (84, "008_02_peristalsis.jpg"),
    (108, "008_03_stomach_tissue.jpg"),
    (204, "008_04_intestine_cutaway.jpg"),
    (228, "008_05_intestinal_villi.jpg"),
    (252, "008_06_tissue_network.jpg"),
    (264, "008_07_blood_cell.jpg"),
    (336, "008_08_microbiome.jpg"),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path, help="Actual approved 008 MP4, not a different render")
    args = parser.parse_args()
    if not args.video.is_file():
        raise SystemExit(f"Originalvideo fehlt: {args.video}")
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg fehlt. Auf macOS bei Bedarf mit Homebrew installieren.")

    root = Path(__file__).resolve().parents[1]
    target = root / "assets/channel/references/video008"
    target.mkdir(parents=True, exist_ok=True)
    for second, name in SHOTS:
        dest = target / name
        cmd = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-ss", str(second), "-i", str(args.video),
            "-frames:v", "1", "-q:v", "3", "-update", "1", str(dest),
        ]
        subprocess.run(cmd, check=True)
        if dest.stat().st_size < 10_000:
            raise SystemExit(f"Bild unvollstaendig: {dest}")
        print(f"{second:>3}s → {dest.relative_to(root)}")

    print("Acht Original-008-Stilbilder erzeugt.")
    print("Beim neuen Video 2–4 passende Frames in Flow als echte Bildreferenzen hochladen.")


if __name__ == "__main__":
    main()
