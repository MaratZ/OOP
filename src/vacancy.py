class Vacancy:
    """
    Класс для формирования вакансии
    """

    __slots__ = (
        "vacancy_data",
        "__name",
        "__salary_from",
        "__salary_to",
        "__description",
        "__city",
        "__link",
            )

    def __init__(self, vacancy):
        self.vacancy_data = vacancy
        self.__name = None
        self.__salary_from = None
        self.__salary_to = None
        self.__description = None
        self.__city = None
        self.__link = None
        self.__validate()

    def __validate(self):
        if self.vacancy_data["name"]:
            self.__name = self.vacancy_data["name"]
        else:
            self.__name = "Название вакансии не указано"

        if self.vacancy_data["salary"]:
            if self.vacancy_data["salary"]["from"]:
                self.__salary_from = self.vacancy_data["salary"]["from"]
            else:
                self.__salary_from = 0

            if self.vacancy_data["salary"]["to"]:
                self.__salary_to = self.vacancy_data["salary"]["to"]
            else:
                self.__salary_to = 0
        else:
            self.__salary_from = 0
            self.__salary_to = 0

        if self.vacancy_data["snippet"]["responsibility"]:
            self.__description = self.vacancy_data["snippet"]["responsibility"]
        else:
            self.__description = "Описание отсутствует"

        if self.vacancy_data["area"]["name"]:
            self.__city = self.vacancy_data["area"]["name"]
        else:
            self.__city = "Город не указан"

        if self.vacancy_data["alternate_url"]:
            self.__link = self.vacancy_data["alternate_url"]
        else:
            self.__link = "Ссылка не указана"


    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def description(self):
        return self.__description

    @property
    def city(self):
        return self.__city

    def __str__(self) -> str:
        name = f"Вакансия: {self.name}"
        salary = f"Зарплата: от {self.__salary_from} до {self.__salary_to}"
        description = f"Описание: {self.description}"
        city = f"Город: {self.city}"
        link = f"Ссылка: {self.link}"
        return f"{name}, {salary}, {description}, {city}, {link}"

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from


if __name__ == "__main__":
    vacancy1 = {
        "name": "Junior Mems Creator",
        "alternate_url": "https://hh.ru/vacancy/105338852",
        "salary": {"from": 0, "to": 1000},
        "snippet": {"responsibility": "Создание мемов"},
        "area": {
            "name": "Смоленск",
        },
    }

    vacancy2 = {
        "name": "Python Guru",
        "alternate_url": "https://hh.ru/vacancy/105338852",
        "salary": {"from": 12000, "to": 20000},
        "snippet": {"responsibility": "Поиск Python профи"},
        "area": {
            "name": "Москва",
        },
    }
    x = Vacancy(vacancy1)
    print(x)
    y = Vacancy(vacancy2)
    print(y)

    print(x>y)
