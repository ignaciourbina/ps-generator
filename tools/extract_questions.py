#!/usr/bin/env python3
"""Extract questions from a web_app index.html file."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from bs4 import BeautifulSoup
import json5


def extract_questions(html_path: Path) -> list[dict]:
    """Return the questions array parsed from the given HTML file."""
    text = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "html.parser")
    script = next((s for s in soup.find_all("script") if s.string and "const questions" in s.string), None)
    if not script:
        raise ValueError("questions array not found")
    stext = script.string
    start = stext.index("const questions")
    start = stext.index("[", start)
    end = stext.index("];", start)
    array_str = stext[start:end + 1]
    return json5.loads(array_str)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract question array from HTML")
    parser.add_argument("html", type=Path, help="Path to web_app/index.html")
    parser.add_argument("output", type=Path, help="Destination JSON file")
    args = parser.parse_args()
    data = extract_questions(args.html)
    args.output.write_text(json.dumps(data, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
