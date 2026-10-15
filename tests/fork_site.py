"""测试用的站点 origin（读仓库根 site.json，见 scripts/site_config.py）。"""

from __future__ import annotations

import json
from pathlib import Path

ORIGIN = json.loads(
    (Path(__file__).resolve().parents[1] / "site.json").read_text(encoding="utf-8")
)["origin"].rstrip("/")
