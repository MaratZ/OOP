from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    vacancy_1 = Vacancy(vacancy_1)
    assert vacancy_1.name == "Junior Mems Creator"
    assert vacancy_1.salary_from == 0
    assert vacancy_1.salary_to == 1000
    assert vacancy_1.description == "Создание мемов"
    assert vacancy_1.city == "Смоленск"
    assert vacancy_1.link == "https://hh.ru/vacancy/105338852"

    assert (
        str(vacancy_1)
        == "Вакансия: Junior Mems Creator, Зарплата: от 0 до 1000, Описание: Создание мемов, Город: Смоленск, "
        "Ссылка: https://hh.ru/vacancy/105338852"
    )


def test_comparison(vacancy_1, vacancy_2):
    vacancy_1 = Vacancy(vacancy_1)
    vacancy_2 = Vacancy(vacancy_2)
    assert vacancy_1 < vacancy_2
