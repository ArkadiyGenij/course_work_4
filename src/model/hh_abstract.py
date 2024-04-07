from abc import ABC, abstractmethod


class HH_abstract(ABC):
    @abstractmethod
    def loading_vacancies(self, keywords):
        """
        Метод для получения JSON объектов с API https://api.hh.ru/vacancies
        :return: Список объектов JSON
        """
        pass
