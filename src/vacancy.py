from abc import ABC, abstractmethod
from builtins import list


class VacansABS(ABC):
    """Абстрактный (родительский) класс для работы с вакансиями."""

    @abstractmethod
    def __init__(self):
        """Инициализация."""
        pass

    @abstractmethod
    def __str__(self):
        """Метод для получение строковых значений."""
        pass


class Vacancy(VacansABS):
    """Дочерний класс для работы с вакансиями."""

    vac_list: list = []

    def __init__(
        self,
        id: int,
        name: str,
        city: str,
        salary_from: int,
        salary_to: int,
        url: str,
        requirement: str,
        responsibility: str,
    ):
        self.id = id
        self.name = name
        self.city = city
        self.salary_from = (
            salary_from if salary_from is not None else 0
        )  # None заменяем на 0
        self.salary_to = salary_to if salary_to is not None else 0  # None заменяем на 0
        # self.salary_from = salary_from
        # self.salary_to = salary_to
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        Vacancy.vac_list.append(self)

    def __str__(self):
        """Метод для получения строковых значений объектов класса."""
        return (
            f"{self.name}\n"
            f"Id: {self.id}\n"
            f"Город: {self.city}\n"
            f"Зарплата от: {self.salary_from if self.salary_from else "Не указана"} \n"
            f"Зарплата до: {self.salary_to if self.salary_to else "Не указана"} \n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
            f"Обязанности: {self.responsibility}\n"
        )

    def vac_obj_to_dict(self):
        """Метод для преобразования объекта вакансий в словарь."""

        dict_of_vac = {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
        return dict_of_vac

    @classmethod
    def vacancies_sort_salary(cls) -> list:
        """
        Класс - метод, который сортирует вакансии по зарплате и
        возвращает отфильтрованный список экземпляров класса по убыванию зарплаты.
        """

        # cls.vac_list.sort(cls.vac_list, key=lambda x: x.salary_from, reverse=True)
        # key=lambda book: book.pages, reverse=True
        # cls.vac_list.sort(key=lambda x: x.salary_from, reverse=True)
        cls.vac_list.sort(reverse=True)
        return cls.vac_list

    @classmethod
    def vacancies_filtered_city(cls, city) -> list:
        """
        Класс - метод, который сортирует вакансии по городам
        и возвращает список вакансий с нужным городом.
        """

        filter_city: list = []
        for item in cls.vac_list:
            if item.city == city:
                filter_city.append(item)
        return filter_city

    @classmethod
    def filter_vacancies(cls, vacancies_list: list, filter_words: list) -> list:
        """Класс - метод для фильтрации вакансий по ключевым словам."""

        filtered_list = []
        for vacancy in vacancies_list:
            # print(vacancy.requirement)#отладка
            for word in filter_words:
                if word.lower() in vacancy.requirement.lower().split():
                    filtered_list.append(vacancy)

        if len(filtered_list) == 0:
            print(*filter_words)
            print("Вакансий с такими критериями не найдено")
        return filtered_list

    def range_from_salary(self, salary_from, salary_to) -> bool:  # type: ignore
        """Метод проверки объекта - вакансии перекрытия зарплатной вилки
        salary_from: int - зарплата "ОТ"
        salary_to: int - зарплата "ДО"
        возвращает bool.
        """
        if isinstance(salary_from, int) is True and isinstance(salary_to, int) is True:
            if self.salary_from >= salary_from and self.salary_to >= salary_to:
                return True
            else:
                return False
                # return self

    def __lt__(self, other):
        """Метод для сравнения вакансий между собой."""

        if isinstance(other, Vacancy) is True:
            return self.salary_from < other.salary_from
        raise TypeError("сравнению подлежат элементы класса Vacancy")

    def validate__(self):
        """Валидация отображения ЗП по признаку отсутствия информации или цифр в графе ЗП от или до"""
        if not self.salary:
            self.salary_from = 0
            self.salary_to = 0
            return

        if not self.salary["from"]:
            self.salary_from = 0
        else:
            self.salary_from = self.salary["from"]

        if not self.salary["to"]:
            self.salary_to = 0
        else:
            self.salary_to = self.salary["to"]