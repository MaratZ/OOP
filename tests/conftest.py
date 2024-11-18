import pytest

from src.vacancy import Vacancy


@pytest.fixture
def serialized():
    return [
        {
            "name": "Junior Python",
            "link": "https://hh.ru/vacancy/105338726",
            "salary": 10,
            "description": "Создание скриптов",
            "area": "Могилев",
        }
    ]


@pytest.fixture
def serialized_for_json():
    return [
        {
            "name": "Junior Python developer",
            "link": "https://hh.ru/vacancy/105338726",
            "salary": 0,
            "description": "Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации тестирования "
            "блокчейн и инфраструктурных проектов. Разработка сценариев, имитирующих взаимодействие "
            "пользователя с веб-приложением, включая...",
            "area": "Могилев",
        }
    ]


@pytest.fixture
def serialized_for_user():
    return (
        "Вакансия: Junior Python developer"
        "Ссылка: https://hh.ru/vacancy/105338726)"
        "Зарплата от: 0"
        "Описание: Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации тестирования блокчейн "
        "и инфраструктурных проектов. Разработка сценариев, имитирующих взаимодействие пользователя с "
        "веб-приложением, включая..."
        "Город: Могилев"
    )


@pytest.fixture
def hh_vacs_list():
    return [
        {
            "name": "Junior Python developer",
            "alternate_url": "https://hh.ru/vacancy/105338726",
            "salary": 0,
            "snippet": {
                "responsibility": "Создание скриптов на <highlighttext>Python</highlighttext> для автоматизации "
                "тестирования блокчейн и инфраструктурных проектов. Разработка сценариев, "
                "имитирующих взаимодействие пользователя с веб-приложением, включая..."
            },
            "area": {"name": "Могилев"},
        }
    ]


@pytest.fixture
def vacancy_1():
    return {
        "name": "Junior Mems Creator",
        "alternate_url": "https://hh.ru/vacancy/105338852",
        "salary": {"from": 0, "to": 1000},
        "snippet": {"responsibility": "Создание мемов"},
        "area": {
            "name": "Смоленск",
        },
    }


@pytest.fixture
def vacancy_2():
    return {
        "name": "Python Guru",
        "alternate_url": "https://hh.ru/vacancy/105338852",
        "salary": {"from": 12000, "to": 20000},
        "snippet": {"responsibility": "Поиск Python профи"},
        "area": {
            "name": "Москва",
        },
    }


@pytest.fixture
def vac_list_1(vacancy_1, vacancy_2):
    return [Vacancy(vacancy_1), Vacancy(vacancy_2)]
