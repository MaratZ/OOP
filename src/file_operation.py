import json
import os
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from config import DATA_DIR
from src.vacancy import Vacancy


class FileChange(ABC):
    """Абстрактный (родительский) класс для работы с API - платформой по поиску вакансий."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass


class FileOperation(FileChange):
    """Дочерний класс для работы с файлами."""

    def __init__(self, filename: str = "Vacans_list"):
        # if filename is None:
        #     filename = datetime.now().strftime("%Y_%m_%d-%H_%M")
        self.__filename = filename + "_" + datetime.now().strftime("%Y_%m_%d-%H_%M")

    def load_file(self):
        """Метод для загрузки файла данных."""

        with open(self.__filename, encoding="utf-8") as json_file:
            data_list = json.load(json_file)

        return data_list

    def write_file(self, data_list: list):  # type: ignore
        """Метод для записи списка данных в файл."""

        with open(
            os.path.join(DATA_DIR, self.__filename + ".vac"),
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

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
            "w",
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


def load_file() -> tuple[list[str], str] | tuple[Any, str]:
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
