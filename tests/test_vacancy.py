import pytest

import src
from src.vacancy import Vacancy


@pytest.fixture()
def Vacancy1():
    Vac1 = Vacancy(
        10,
        "name1",
        "Город Н",
        100,
        None,
        "https://gg.com",
        "Уметь всё",
        "Жить на работе",
    )
    return Vac1


@pytest.fixture()
def Vacancy2():
    Vac2 = Vacancy(
        11,
        "name2",
        "Город M",
        110,
        120,
        "https://gg.com",
        "Знать всё",
        "Жить на работе",
    )
    return Vac2


def test_vacancy_init(Vacancy1):
    """Проверка для инициализации объекта в классе Vacancy."""

    assert Vacancy1.id == 10
    assert Vacancy1.name == "name1"
    assert Vacancy1.city == "Город Н"
    assert Vacancy1.salary_from == 100
    assert Vacancy1.salary_to == 0
    assert Vacancy1.url == "https://gg.com"
    assert Vacancy1.requirement == "Уметь всё"
    assert Vacancy1.responsibility == "Жить на работе"


def test_vac_obj_to_dict(Vacancy1):
    """Проверка для преобразования объекта класса в словарь."""

    vacansy_dict = Vacancy.vac_obj_to_dict(Vacancy1)
    assert vacansy_dict.get("name") == "name1"
    assert vacansy_dict.get("id") == 10
    assert vacansy_dict.get("name") == "name1"
    assert vacansy_dict.get("city") == "Город Н"
    assert vacansy_dict.get("salary_from") == 100
    assert vacansy_dict.get("salary_to") == 0
    assert vacansy_dict.get("url") == "https://gg.com"
    assert vacansy_dict.get("requirement") == "Уметь всё"
    assert vacansy_dict.get("responsibility") == "Жить на работе"


def test_vacancies_sort_salary(Vacancy2):
    vac_obj = Vacancy2
    vacans_sort_list = Vacancy.vacancies_sort_salary()
    # assert len(vacans_sort_list) == 4
    assert vacans_sort_list[0].name == vac_obj.name
    assert vacans_sort_list[1].name == "name1"


def test_filter_vacancies(Vacancy2, Vacancy1):
    vac_list = []
    vac_list.append(Vacancy2)
    vac_list.append(Vacancy1)
    filter_words = ["уметь"]
    filtered_vac = Vacancy.filter_vacancies(vac_list, filter_words)
    assert len(filtered_vac) == 1
    assert filtered_vac[0].name == "name1"


def test_filter_vacancies_wrong_word(Vacancy2, Vacancy1):
    vac_list = []
    vac_list.append(Vacancy2)
    vac_list.append(Vacancy1)
    filter_words = ["абракадабра"]
    filtered_vac = Vacancy.filter_vacancies(vac_list, filter_words)
    assert len(filtered_vac) == 0


def test_range_from_salary_wrong(Vacancy2):
    test_vac = Vacancy2
    assert Vacancy.range_from_salary(test_vac, 200, 300) is False


def test_range_from_salary_pass(Vacancy1):
    test_vac = Vacancy1
    assert Vacancy.range_from_salary(test_vac, 0, 0) is True


def test_str(Vacancy1):
    test_vac = Vacancy1
    string_of_obj = str(test_vac).replace("\n", " ")
    assert (
        string_of_obj
        == "name1 Id: 10 Город: Город Н Зарплата от: 100  Зарплата до: Не указана  Ссылка: https://gg.com "
        "Требования: Уметь всё Обязанности: Жить на работе "
    )
def test_vacancies_sort_salary(Vacancy2):
    vac_obj = Vacancy2
    vacans_sort_list = src.vacancy.Vacancy.vacancies_sort_salary()
    # assert len(vacans_sort_list) == 4
    assert vacans_sort_list[0].name == vac_obj.name
    assert vacans_sort_list[1].name == "name1"


def test_filter_vacancies(Vacancy2, Vacancy1):
    vac_list = []
    vac_list.append(Vacancy2)
    vac_list.append(Vacancy1)
    filter_words = ["уметь"]
    filtered_vac = src.vacancy.Vacancy.filter_vacancies(vac_list, filter_words)
    assert len(filtered_vac) == 1
    assert filtered_vac[0].name == "name1"


def test_filter_vacancies_wrong_word(Vacancy2, Vacancy1):
    vac_list = []
    vac_list.append(Vacancy2)
    vac_list.append(Vacancy1)
    filter_words = ["абракадабра"]
    filtered_vac = src.vacancy.Vacancy.filter_vacancies(vac_list, filter_words)
    assert len(filtered_vac) == 0


def test_range_from_salary_wrong(Vacancy2):
    test_vac = Vacancy2
    assert src.vacancy.Vacancy.range_from_salary(test_vac, 200, 300) is False


def test_range_from_salary_pass(Vacancy1):
    test_vac = Vacancy1
    assert src.vacancy.Vacancy.range_from_salary(test_vac, 0, 0) is True


def test_str(Vacancy1):
    test_vac = Vacancy1
    string_of_obj = str(test_vac).replace("\n", " ")
    assert (
        string_of_obj
        == "name1 Id: 10 Город: Город Н Зарплата от: 100  Зарплата до: Не указана  Ссылка: https://gg.com "
        "Требования: Уметь всё Обязанности: Жить на работе "
    )
