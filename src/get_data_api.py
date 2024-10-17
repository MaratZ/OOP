from abc import ABC, abstractmethod

import requests


class JobsAPI(ABC):
    """Абстрактный (родительский) класс для работы с API - платформой по поиску работы."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacans_short(self):
        pass


class HeadHunterAPI(JobsAPI):
    """Дочерний класс для получения вакансий из API - платформы HeadHunter."""

    def __init__(self, keyword: str):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "text": keyword,
            "area": 113,  # Россия
            "only_with_salary": True,  # Указана зарплата
            "page": 0,
            "per_page": 100,  # Вакансий на странице
        }

    def get_vacancies(self):
        """Метод, который возвращает вакансии по заданному параметру."""

        response = requests.get(self.url, params=self.params)
        if response.status_code != 200:
            return [{}]
        else:
            return response.json().get("items", {})
        # return response.json()

    def get_vacans_short(self):
        """
        Метод для получения упрощенной информации о вакансии.
        return: vacancies - список словарей с вакансиями
        """

        vacancies = []
        for vacans in self.get_vacancies():
            vacancies.append(
                {
                    "id": int(vacans.get("id")),
                    "name": vacans.get("name"),
                    "city": vacans.get("area").get("name"),
                    # "salary_from": vacans.get("salary").get("from"),
                    "salary_from": (
                        vacans.get("salary").get("from")
                        if vacans.get("salary").get("from") is not None
                        else 0
                    ),
                    # "salary_to": vacans.get("salary").get("to"),
                    "salary_to": (
                        vacans.get("salary").get("to")
                        if vacans.get("salary").get("to") is not None
                        else 0
                    ),
                    "url": vacans.get("url"),
                    "requirement": (
                        vacans.get("snippet").get("requirement")
                        if vacans.get("snippet").get("requirement") is not None
                        else "Не указано"
                    ),
                    "responsibility": (
                        vacans.get("snippet").get("responsibility")
                        if vacans.get("snippet").get("responsibility") is not None
                        else "Не указано"
                    ),
                }
            )
        return vacancies


# class HH(Parser):
#     """Класс для работы с API HeadHunter"""
#     def __init__(self):
#         self.url: str = 'https://api.hh.ru/vacancies'
#         self.headers: dict = {'User-Agent': 'HH-User-Agent'}
#         self.params: dict = {'text': '', 'page': 0, 'per_page': 100}
#         self.vacancies: list = []
#         print("Загрузка данных с ресурса HH.ru. Ждите.")
#
#     def load_vacancies(self, keyword: str):
#         """Метод для получения данных с ресурса HH.ru"""
#         self.params['text'] = keyword
#         while self.params.get('page') != 20:
#             response = requests.get(self.url, headers=self.headers, params=self.params)
#             vacancies = response.json()['items']
#             self.vacancies.extend(vacancies)
#             self.params['page'] += 1
#         return self.vacancies
