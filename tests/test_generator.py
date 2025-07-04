import subprocess
from pathlib import Path
import shutil
import pytest


def test_build_tex(tmp_path: Path):
    bank = Path('problem-set-1/question_bank.json')
    out = tmp_path
    subprocess.run([
        'python', '-m', 'generator.build_ps',
        '--bank', str(bank),
        '--out', str(out)
    ], check=True)
    ps = out / 'problem_set.tex'
    sol = out / 'solutions.tex'
    assert ps.exists()
    assert sol.exists()
    tex = ps.read_text()
    assert '\\begin{enumerate}' in tex
    assert tex.count('\\item') >= 14


@pytest.mark.skipif(
    shutil.which('pdflatex') is None,
    reason='pdflatex not installed'
)
def test_build_pdf_pipeline(tmp_path: Path):
    bank = Path('problem-set-1/question_bank.json')
    out = tmp_path
    subprocess.run([
        'python', '-m', 'generator.build_pdf',
        '--bank', str(bank),
        '--out', str(out)
    ], check=True)
    assert (out / 'problem_set.pdf').exists()
    assert (out / 'solutions.pdf').exists()
