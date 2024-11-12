from src.utils import VacanciesFilterSort
from src.vacancy import Vacancy


def test_filter_init():
    test = VacanciesFilterSort(
        filter_word="python", filter_city="москва", filter_salary=[0, 1000], top_n=5
    )
    assert test.filter_word == "python"
    assert test.filter_city == "москва"
    assert test.filter_salary == [0, 1000]

    assert test.top_n == 5


def test_filter_by_description(vac_list_1, vacancy_1):
    test = VacanciesFilterSort(
        filter_word="Создание", filter_city="Смоленск", filter_salary=[0, 1000], top_n=5
    )
    assert test.filter_by_description(vac_list_1) == [Vacancy(vacancy_1)]


def test_filter_by_city(vac_list_1, vacancy_2):
    test = VacanciesFilterSort(
        filter_word="Создание",
        filter_city="Москва",
        filter_salary=[12000, 20000],
        top_n=5,
    )
    assert test.filter_by_city(vac_list_1) == [Vacancy(vacancy_2)]


def test_filter_by_salary(vac_list_1, vacancy_2):
    test = VacanciesFilterSort(
        filter_word="Создание", filter_city="Москва", filter_salary=[1, 21000], top_n=5
    )
    assert test.filter_by_city(vac_list_1) == [Vacancy(vacancy_2)]


def test_sort_vacancies_by_salary(vac_list_1, vacancy_1, vacancy_2):
    test = VacanciesFilterSort(
        filter_word="Создание", filter_city="Москва", filter_salary=[0, 20000], top_n=5
    )
    assert test.sort_vacancies_by_salary(vac_list_1) == [
        Vacancy(vacancy_2),
        Vacancy(vacancy_1),
    ]


def test_get_top_vacancies(vac_list_1):
    test = VacanciesFilterSort(
        filter_word="Создание", filter_city="Москва", filter_salary=[0, 20000], top_n=5
    )
    assert test.get_top_vacancies(vac_list_1) == (
        "Вакансия 1:\nВакансия: Junior Mems Creator, Зарплата: от 0 до 1000, Описание: Создание мемов, "
        "Город: Смоленск, Ссылка: https://hh.ru/vacancy/105338852\n\nВакансия 2:\nВакансия: Python Guru, Зарплата: от "
        "12000 до 20000, Описание: Поиск Python профи, Город: Москва, Ссылка: https://hh.ru/vacancy/105338852\n\n"
    )
