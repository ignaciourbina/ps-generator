#!/usr/bin/env python3
"""Build problem set and solutions TeX files from a question bank."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def load_bank(path: Path) -> list[dict]:
    """Return list of questions from a JSON bank."""
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def render(template, context: dict, out_path: Path) -> None:
    out_path.write_text(template.render(context), encoding="utf-8")


def build(bank_path: Path, out_dir: Path) -> None:
    questions = load_bank(bank_path)
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
    ctx = {"questions": questions, "today": date.today()}
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in ("problem_set", "solutions"):
        tmpl = env.get_template(f"{name}.tex.j2")
        render(tmpl, ctx, out_dir / f"{name}.tex")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate TeX problem set")
    parser.add_argument("--bank", type=Path, required=True, help="question_bank.json")
    parser.add_argument("--out", type=Path, default=Path("."), help="output directory")
    args = parser.parse_args()
    build(args.bank, args.out)


if __name__ == "__main__":
    main()
