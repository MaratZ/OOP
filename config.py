import os

# Получаем абсолютный путь до текущей директории
ROOT_DIR = os.path.dirname(__file__)

# Создаем путь до директории data
DATA_DIR = os.path.join(ROOT_DIR, "data")

#Создаем путь до файла vacancies.json относительно текущей директории.
REL_JSON_DIR = os.path.join(DATA_DIR, "https://github.com/MaratZ/OOP/tree/feature/data/vacancies.json")
JSON_DIR = os.path.abspath(REL_JSON_DIR)