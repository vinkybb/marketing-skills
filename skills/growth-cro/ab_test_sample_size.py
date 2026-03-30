"""Legacy entrypoint: delegates to ab-test-sample-size/main.py (same CLI and output)."""

from __future__ import annotations

import runpy
from pathlib import Path

if __name__ == "__main__":
    main_script = Path(__file__).resolve().parent / "ab-test-sample-size" / "main.py"
    runpy.run_path(str(main_script), run_name="__main__")
