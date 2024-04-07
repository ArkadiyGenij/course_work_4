import json

from src.model.json_abc import JSON_abc
from src.model.vacancy import Vacancy


class JSON(JSON_abc):

    def __init__(self):
        self.filename = "vacancies.json"

    def add_vacancies(self, vacancies):
        """
        Метод для добавления JSON объектов в файл
        :param vacancies: Список JSON объектов
        :return:
        """
        data = []

        for vacancy in vacancies:
            vacancies_data = {
                "name": vacancy["name"],
                "URL": vacancy["url"],
                "to_salary": vacancy["salary"]["to"],
                "from_salary": vacancy["salary"]["from"],
                "requirements": vacancy["snippet"]["requirement"],
                "responsibility": vacancy["snippet"]["responsibility"]
            }
            data.append(vacancies_data)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        """
        Метод для чтения JSON объектов из файла, и их парсинга в объекты класса Vacancy
        :return: Список объектов Vacancy
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            vacancies = []
            data = json.load(file)
            for vacancy in data:
                obj_vacancy = Vacancy(vacancy["name"],
                                      vacancy["url"],
                                      vacancy["to_salary"],
                                      vacancy["from_salary"],
                                      vacancy["requirements"],
                                      vacancy["responsibility"])
                vacancies.append(obj_vacancy)
            return vacancies
