#!/usr/bin/env python3
"""Extract question metadata from a web_app `index.html` file.

The script looks for a JavaScript array assignment like ``const questions = [...]``.
It parses the array using ``json5`` when available so that single quotes or
trailing commas are accepted.  If ``json5`` is missing, a more robust fallback
uses Node.js to evaluate the snippet and return valid JSON.  Only if Node.js is
unavailable do we attempt a very simple transformation to standard JSON.  All
keys present in the HTML are preserved in the resulting list of dictionaries.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup
import re

try:  # json5 is optional
    import json5  # type: ignore
except ImportError:  # pragma: no cover - fallback if json5 unavailable
    json5 = None


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
            array_text = match.group(1)
            if json5:
                return json5.loads(array_text)
            try:  # attempt Node.js evaluation for robust parsing
                with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
                    tmp.write(array_text)
                    tmp_path = tmp.name
                node_script = (
                    "const fs=require('fs');"
                    "const vm=require('vm');"
                    "const s=fs.readFileSync(process.argv[1],'utf8');"
                    "const d=vm.runInNewContext('(' + s + ')');"
                    "process.stdout.write(JSON.stringify(d));"
                )
                result = subprocess.run(
                    ['node', '-e', node_script, tmp_path],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                os.unlink(tmp_path)
                return json.loads(result.stdout)
            except Exception:
                # simple transformation as last resort
                safe = re.sub(r"(\w+)\s*:", r'"\1":', array_text)
                safe = re.sub(r",\s*(?=[}\]])", "", safe)
                return json.loads(safe)

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
