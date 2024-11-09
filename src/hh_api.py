from abc import ABC, abstractmethod
from typing import List

import requests


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с платформой hh.ru
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__code_status = requests.get(self.__url).status_code
        self.vacancies = []

    def load_vacancies(self, keyword: str):
        """
        Функция для получения вакансий по заданному слову.
        """
        self.__params["text"] = keyword
        if self.__code_status != 200:
            raise NameError(f"Возникла ошибка: {self.__code_status}")
        else:
            while self.__params.get("page") != 2:
                try:
                    response = requests.get(
                        self.__url, headers=self.__headers, params=self.__params
                    )
                except Exception as e:
                    print(f"Произошла ошибка {e}")
                else:
                    vacancies = response.json()["items"]
                    self.vacancies.extend(vacancies)
                    self.__params["page"] += 1

    def get_vacancies(self) -> List:
        """
        Возвращает список вакансий
        """
        return self.vacancies


# if __name__ == "__main__":
hh = HeadHunterAPI()
hh.load_vacancies("Python")
hh_vacancies = hh.get_vacancies()
# print(hh_vacancies)