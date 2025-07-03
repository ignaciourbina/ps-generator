import json
from pathlib import Path


def load_bank(path: Path):
    with path.open() as f:
        return json.load(f)


def test_problem_set_1_count_and_ids():
    data = load_bank(Path('problem-set-1/question_bank.json'))
    assert len(data) == 14
    assert data[0]['id'] == 1
    assert data[-1]['id'] == 14


def test_problem_set_2_count_and_ids():
    data = load_bank(Path('problem-set-2/question_bank.json'))
    assert len(data) == 21
    assert data[0]['id'] == 1
    assert data[-1]['id'] == 21
