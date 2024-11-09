from src.file_worker import JSONSaver
from src.hh_api import HeadHunterAPI
from src.utils import VacanciesFilterSort



# Функция для взаимодействия с пользователем
def main():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    search_query = input('Введите поисковый запрос: ')

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)
    hh_vacancies = hh_api.get_vacancies()

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.write_file(hh_vacancies)


    # Обращение к пользователю. Сбор информации
    while True:
        try:
            top_n = int(input('Введите количество вакансий для вывода в топ N: '))
        except ValueError:
            print('Необходимо указать число вакансий для вывода в топ N ')
            continue
        filter_word = input('Введите ключевое слово для фильтрации вакансий: ')
        filter_city = input('Введите город: ')
        filter_salary = input('Введите диапазон зарплат. Например: 10000-15000: ').split('-')
        print(' ')

        read_vacs_from_json = json_saver.read_file()
        #print(read_vacs_from_json)

        # for i in read_vacs_from_json:
        #     print(i['salary_from'])

        # Создание экземпляра класса фильтрации и сортировки вакансий
        filtered_obj = VacanciesFilterSort(filter_word, filter_city, filter_salary, top_n)
        filtered_by_description = filtered_obj.filter_by_description(read_vacs_from_json)
        filtered_by_city = filtered_obj.filter_by_city(filtered_by_description)
        filtered_by_salary = filtered_obj.filter_by_salary(filtered_by_city)

        sorted_by_salary = filtered_obj.sort_vacancies_by_salary(filtered_by_salary)

        top_vacancies = filtered_obj.get_top_vacancies(sorted_by_salary)


        print(f'По заданным параметрам найдено вакансий: {len(sorted_by_salary)}')
        print(f'Статистика поиска:\n{len(filtered_by_description)} вакансий по описанию,\n{len(filtered_by_city)} вакансий по местоположению,\n{len(filtered_by_salary)} вакансий по зарплате\n')
        print(f'\n{top_vacancies}\n')

        break





if __name__ == '__main__':
    main()
