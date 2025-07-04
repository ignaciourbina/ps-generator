#!/usr/bin/env python3
"""Pipeline to generate PDF problem sets from a question bank."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from generator import build_ps


def compile_tex(tex_path: Path) -> None:
    """Run pdflatex on the given TeX file."""
    subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_path.name,
        ],
        cwd=tex_path.parent,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        check=True,
    )


def build_and_compile(bank: Path, out_dir: Path) -> None:
    """Generate TeX and compile them to PDFs."""
    build_ps.build(bank, out_dir)
    for name in ("problem_set", "solutions"):
        compile_tex(out_dir / f"{name}.tex")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate PDFs from a question bank"
    )
    parser.add_argument(
        "--bank", type=Path, required=True, help="Path to question_bank.json"
    )
    parser.add_argument(
        "--out", type=Path, default=Path("build"), help="Output directory"
    )
    args = parser.parse_args()
    build_and_compile(args.bank, args.out)


if __name__ == "__main__":
    main()
