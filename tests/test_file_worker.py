import os

from config import DATA_DIR
from src.file_worker import JSONSaver


def test_init():
    assert JSONSaver().filename == os.path.join(DATA_DIR, "vacancies.json")
