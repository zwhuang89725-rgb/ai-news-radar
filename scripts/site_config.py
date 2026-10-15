"""本 fork 的站点 origin 唯一真值源（读仓库根的 site.json）。

上游把 https://news.learnprompt.pro 硬编码在脚本/测试里，导致域名一变处处失配。
这里收敛成一处：脚本、测试、CI 都从 site.json 取。
"""

from __future__ import annotations

import json
from pathlib import Path

SITE_JSON = Path(__file__).resolve().parents[1] / "site.json"


def origin() -> str:
    """站点根地址，不带结尾斜杠，例如 https://user.github.io/repo"""
    return json.loads(SITE_JSON.read_text(encoding="utf-8"))["origin"].rstrip("/")


def host() -> str:
    """origin 的主机+路径部分（去掉 scheme）。"""
    return origin().split("://", 1)[-1]


def load() -> str:
    """供脚本顶部直接赋值用。"""
    return origin()
