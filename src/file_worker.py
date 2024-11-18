import json
import os
from abc import ABC, abstractmethod
from typing import List

from config import DATA_DIR
from src.vacancy import Vacancy



class FileChange(ABC):
    """Абстрактный (родительский) класс для работы с API - платформой по поиску вакансий."""

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def read_file(self):
        pass
    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass

class FileOperation(FileChange):
    """Дочерний класс для работы с файлами."""

    filename_value = "vacancies.json"

    def __init__(self, filename=filename_value):
        self.vacs_list = []
        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self):
        return self.__filename

    def read_file(self):
        """
        Функция для чтения файла. Проверяет, есть ли файл. И, если есть, сохраняет список объектов
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="UTF-8") as f:
                vacs = json.load(f)
            self.vacs_list = [Vacancy(i) for i in vacs]
        return self.vacs_list
    def write_file(self, vacs_obj: list):
        """
        Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy.
        """
        vacs_list = []
        for i in vacs_obj:
            vacs_list.append(
                {
                    "name": Vacancy(i).name,
                    "salary": {
                        "from": Vacancy(i).salary_from,
                        "to": Vacancy(i).salary_to,
                    },
                    # "salary_to": {"to": Vacancy(i).salary_to},
                    "snippet": {"responsibility": Vacancy(i).description},
                    "area": {"name": Vacancy(i).city},
                    "alternate_url": Vacancy(i).link,
                }
            )
        with open(self.filename, "a+", encoding="utf-8") as f:
            json.dump(vacs_list, f, ensure_ascii=False, indent=4)

    def load_file(self):
        """Метод для загрузки файла данных."""

        with open(self.__filename, encoding="utf-8") as json_file:
            data_list = json.load(json_file)

        return data_list



    def delete_by_id(self, id_list: list):
        data_list = self.load_file()
        save_list = [
            vac_data for vac_data in data_list if vac_data.get("id") not in id_list
        ]
        self.write_file(save_list)

    @staticmethod
    def delete_vacans_in_file(selected_file: str, id_list: list):
        """Метод для удаления из файла вакансий selected_file вакансий,
        с id  перечисленными в списке id_list."""

        with open(selected_file, encoding="utf-8") as json_file:
            data_list = json.load(json_file)
            save_list = []
        for item in data_list:

            if item.get("id") not in id_list:
                # print(item)
                save_list.append(item)

        with open(
            os.path.join(selected_file),
            "a",
            encoding="utf-8",
        ) as f:
            json.dump(save_list, f, ensure_ascii=False, indent=4)


def vac_file_list():
    """Функция для вывода списка файлов VAC_JSON."""

    file_list = []
    for entry in os.scandir(DATA_DIR):  # вывод списка файлов
        if entry.is_dir():
            # skip directories
            continue
        elif entry.name.split(".")[-1] != "vac":
            continue
        else:
            # print(entry.name)
            file_list.append(entry.name)

    for i, name_file in enumerate(file_list):
        print(i, name_file)  # вывод списка файлов VAC_JSON
    return file_list


def vac_obj_from_file() -> list:
    """Функция для создания списка объектов класса Vacancy из vac-файла."""

    vac_list = load_file()
    vac_obj_list = []
    for item in vac_list:
        vac_obj_list.append(Vacancy(**item))  # type: ignore
    return vac_obj_list


def load_file() -> tuple[list[str], str] | tuple[any, str]:
    """Метод выбора файла в папке DATA и его чтения."""

    print("Список файлов в папке DATA")
    file_list = vac_file_list()
    if len(file_list) == 0:
        print("файлов не найдено")
        return [""], ""
    # file_name = input("Введите имя файла в директории дата \n")
    file_index = int(input("Введите индекс файла из списка \n"))
    file_name = file_list[file_index]
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, encoding="utf-8") as json_file:
        data_list = json.load(json_file)
    return data_list, file_name


class BaseFileReader(ABC):
    """
    Абстрактный класс для чтения и записи файла
    """

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, ser_vacs):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JSONSaver(BaseFileReader):
    """
    Класс для чтения из файла, записи в файл списка вакансий

    """

    filename_value = "vacancies.json"

    def __init__(self, filename=filename_value):
        self.vacs_list = []
        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self):
        return self.__filename

    def read_file(self):
        """
        Функция для чтения файла. Проверяет, есть ли файл. И, если есть, сохраняет список объектов
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="UTF-8") as f:
                vacs = json.load(f)
            self.vacs_list = [Vacancy(i) for i in vacs]
        return self.vacs_list

    def write_file(self, vacs_obj: List):
        """
        Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy.
        """
        with open(self.filename, "r", encoding="UTF-8") as f:
            vacs = json.load(f)

        vacs_list = []
        for i in vacs_obj:
            vacs_list.append(
                {
                    "name": Vacancy(i).name,
                    "salary": {
                        "from": Vacancy(i).salary_from,
                        "to": Vacancy(i).salary_to,
                    },
                    # "salary_to": {"to": Vacancy(i).salary_to},
                    "snippet": {"responsibility": Vacancy(i).description},
                    "area": {"name": Vacancy(i).city},
                    "alternate_url": Vacancy(i).link,
                }
            )
        vacs.extend(vacs_list)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacs, f, ensure_ascii=False, indent=4)


    def add_vacancy(self, vacancy):
        pass

    def del_vacancy(self):
        with open(self.filename, "w"):
            pass
