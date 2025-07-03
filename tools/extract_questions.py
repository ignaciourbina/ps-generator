#!/usr/bin/env python3
"""Extract questions from a web_app index.html file."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from bs4 import BeautifulSoup
import json5
import re


def extract_questions(html_path: Path) -> list[dict]:
    """Return the questions array parsed from the given HTML file."""
    text = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "html.parser")
    pattern = re.compile(r"(?:const|let|var)\s+questions\s*=\s*(\[[\s\S]*?\])\s*;")

    for script in soup.find_all("script"):
        if not script.string:
            continue
        match = pattern.search(script.string)
        if match:
            return json5.loads(match.group(1))

    raise ValueError("questions array not found")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract question array from HTML")
    parser.add_argument("html", type=Path, help="Path to web_app/index.html")
    parser.add_argument("output", type=Path, help="Destination JSON file")
    args = parser.parse_args()
    data = extract_questions(args.html)
    args.output.write_text(json.dumps(data, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
