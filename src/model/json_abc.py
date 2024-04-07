from abc import ABC, abstractmethod


class JSON_abc(ABC):
    @abstractmethod
    def add_vacancies(self, vacancies):
        """
        Метод для добавления вакансий в файл
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """
        Метод для получения вакансий из файла
        """
        pass
