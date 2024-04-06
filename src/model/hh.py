import json

import requests

from src.model.hh_abstract import HH_abstract


class HH(HH_abstract):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def loading_vacancies(self):
        """
        Реализация метода для загрузки вакансий с API
        :return: Список объектов JSON
        """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        vacancies = response.json()["items"]
        return vacancies
