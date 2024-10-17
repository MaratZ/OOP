from src.file_operation import FileOperation, load_file
from src.get_data_api import HeadHunterAPI
from src.vacancy import Vacancy


def select_source():
    """Функция для выбора источника данных."""

    print(
        "Здравствуйте.Это программа выводит информацию о вакансиях,\n"
        "опубликованных на сайте hh.ru"
    )
    print("Выберите источник данных")
    print("0 - данные с сайта hh.ru")
    print("1 - загрузка из файла")
    select_sourse = input("")
    if select_sourse == "0":
        print("Начнем с получения списка вакансий по выбранной профессии\n")
        print("Введите название профессии,например - программист\n")
        search_vacancy = input("Введите запрос:\n")
        print(f"Будем искать вакансии по запросу : {search_vacancy}")
        vac_data_list = HeadHunterAPI(search_vacancy).get_vacans_short()
        return search_vacancy, vac_data_list
    elif select_sourse == "1":
        vac_data_list, file_name = load_file()
        if vac_data_list == [""]:
            exit(0)
        search_vacancy = file_name.split("_")[0]
        return search_vacancy, vac_data_list
    else:
        exit()


def user_interaction():
    """Функция для взаимодействия с пользователем."""

    search_vacancy, vac_data_list = select_source()
    count_vac = len(vac_data_list)
    print(f"Найдено - {count_vac} вакансий")

    create_vacancy_object(vac_data_list)

    sort_vac_obj_list = select_top_vac_from_salary(count_vac)

    sort_vac_obj_list = filtered_vac_from_salary_range(sort_vac_obj_list)

    filter_keyword_vac_obj_list = filtered_vac_from_keywords(sort_vac_obj_list)

    final_func(filter_keyword_vac_obj_list, search_vacancy)


def create_vacancy_object(vac_data_list):
    """Функция для создания объектов вакансий."""

    vac_obj_list = []
    for item in vac_data_list:
        vac_obj_list.append(Vacancy(**item))


def select_top_vac_from_salary(count_vac):
    """Функция для сортировки вакансий по зарплате."""

    print("Отсортируем по зарплате и выведем топ самых высокооплачиваемых.")
    print("Эти вакансии будут отобраны дла работы с ними")
    input_top_n = input("Ведите количество вакансий для вывода")
    if input_top_n == "":
        top_n = count_vac
    else:
        if input_top_n.isdigit():
            top_n = int(input_top_n)
    if top_n > count_vac:
        top_n = count_vac

    sort_vac_obj_list = Vacancy.vacancies_sort_salary()[0:top_n]
    for item in sort_vac_obj_list:
        print(item)
    return sort_vac_obj_list


def filtered_vac_from_salary_range(sort_vac_obj_list):
    """Функция, которая отбирает вакансии по зарплатной вилке."""

    print("Отфильтруем вакансии по зарплатной вилке")
    print("Ведите через запятую желаемый уровень зарплаты,")
    print("от минимально приемлимого до желаемого,")
    print("например 50000,70000")
    print("если указать 0 в качестве одной из границ в диапазон попадут зарплаты,")
    print("в которых граница не задана")

    salary_list = input("Введите диапазон через запятую: ").split(",")
    if salary_list == [""]:
        salary_list = ["0", "0"]
    in_salary_from, in_salary_to = map(int, salary_list)

    for item in sort_vac_obj_list:
        if Vacancy.range_from_salary(item, in_salary_from, in_salary_to) is False:
            sort_vac_obj_list.remove(item)
    return sort_vac_obj_list


def filtered_vac_from_keywords(sort_vac_obj_list):
    """Функция, которая сортирует вакансии по ключевым словам."""

    print("Отфильтруем по ключевым словам")
    print("Введите через запятую ключевые слова,")
    print("например - без опыта,обучение")

    keyword_list = input("Введите ключевые слова: ").split(",")
    print(keyword_list)
    if keyword_list != [""]:
        filter_keyword_vac_obj_list = Vacancy.filter_vacancies(
            sort_vac_obj_list, keyword_list
        )
        return filter_keyword_vac_obj_list
    else:
        filter_keyword_vac_obj_list = sort_vac_obj_list
        return filter_keyword_vac_obj_list
    print(f"осталось - {len(filter_keyword_vac_obj_list)} вакансий  ")


def final_func(filter_keyword_vac_obj_list, search_vacancy):
    """Функция, которая выводит список оставшихся вакансий и сохраняет их в файл."""
    if len(filter_keyword_vac_obj_list) > 0:

        print("Список оставшихся вакансий:")
        vac_dict_list = []
        for item in filter_keyword_vac_obj_list:  # сериализация в json
            print(item)
            vac_dict_list.append(Vacancy.vac_obj_to_dict(item))

        save = FileOperation(search_vacancy)
        save.write_file(vac_dict_list)
        print("Список сохранен")
        print(f"Сохранено {len(filter_keyword_vac_obj_list)} вакансий")
    else:
        print("Вакансий по выбранным критериям не осталось,\n необходимо начать заново")
