from data.json_saver import JSON
from src.model.hh import HH
from src.model.vacancy import Vacancy


def user_interaction():
    hh_api = HH()
    json_connector = JSON()

    search_query = input("Введите поисковый запрос: ")
    salary_range = input("Введите диапазон зарплат: ")

    hh_vacancies = hh_api.loading_vacancies(search_query)
    json_connector.add_vacancies(hh_vacancies)
    vacancies = json_connector.get_vacancies()

    filtered_vacancies_by_salary = Vacancy.filter_by_salary(salary_range, vacancies)

    for vacancy in filtered_vacancies_by_salary:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
