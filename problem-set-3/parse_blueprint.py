from __future__ import annotations

import json
import re
from pathlib import Path
from typing import List, Dict


def extract_question_blocks(md_text: str) -> List[Dict]:
    pattern = re.compile(r"```jsonc\n(.*?)```", re.DOTALL)
    blocks = pattern.findall(md_text)
    questions = []
    for block in blocks:
        obj = json.loads(block)
        questions.append(obj)
    return questions


def convert_to_bank(objs: List[Dict]) -> List[Dict]:
    bank = []
    for idx, obj in enumerate(objs, start=1):
        options = []
        for key, val in obj["choices"].items():
            options.append({"text": val, "value": key.lower()})
        bank.append(
            {
                "id": idx,
                "text": obj["stem"],
                "topic_short": obj["tags"][0] if obj.get("tags") else obj.get("category", ""),
                "options": options,
                "correctAnswer": obj["answer"].lower(),
                "explanation": obj["rationale"],
            }
        )
    return bank


def main() -> None:
    md_path = Path("problem_set_blueprint.md")
    out_path = Path("question_bank.json")
    md_text = md_path.read_text(encoding="utf-8")
    objs = extract_question_blocks(md_text)
    bank = convert_to_bank(objs)
    out_path.write_text(json.dumps(bank, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
