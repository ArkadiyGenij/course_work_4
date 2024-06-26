class Vacancy:
    name: str
    url: str
    to_salary: int
    from_salary: int
    requirements: str
    responsibility: str

    def __init__(self, name, url, to_salary, from_salary, requirements, responsibility):
        self.name = name
        self.url = url
        self.to_salary = to_salary
        self.from_salary = from_salary
        self.requirements = requirements
        self.responsibility = responsibility

    def __str__(self):
        return (f"=====================================\n"
                f"Название: {self.name}\n"
                f"URL: {self.url}\n"
                f"Зарплата: от {self.from_salary} до {self.to_salary}\n"
                f"Требования: {self.requirements}\n"
                f"Обязанности: {self.responsibility}\n"
                f"=====================================")

    def __lt__(self, other):
        """Метод сравнения вакансий: меньше"""
        if self.to_salary is None or other.to_salary is None:
            return False
        return self.to_salary < other.to_salary

    def __gt__(self, other):
        """Метод сравнения вакансий: больше"""
        if self.to_salary is None or other.to_salary is None:
            return False
        return self.to_salary > other.to_salary

    def __eq__(self, other):
        """Метод сравнения вакансий: равно"""
        if self.to_salary is None or other.to_salary is None:
            return False
        return self.to_salary == other.to_salary

    @staticmethod
    def filter_by_salary(salary_range, vacancies):
        """
        Метод для фильтрации вакансий по зарплате
        :param vacancies: список вакансий
        :param salary_range: диапазон зарплат
        :return: список отфильтрованных вакансий
        """
        from_salary_str, to_salary_str = salary_range.split("-")
        from_salary = int(from_salary_str)
        to_salary = int(to_salary_str)

        filtered_vacancies = []

        for vacancy in vacancies:
            if vacancy.from_salary is not None and vacancy.to_salary is not None:
                if from_salary <= vacancy.from_salary <= to_salary or \
                        from_salary <= vacancy.to_salary <= to_salary:
                    filtered_vacancies.append(vacancy)
            elif vacancy.from_salary is not None:
                if from_salary <= vacancy.from_salary <= to_salary:
                    filtered_vacancies.append(vacancy)
            elif vacancy.to_salary is not None:
                if from_salary <= vacancy.to_salary <= to_salary:
                    filtered_vacancies.append(vacancy)

        return filtered_vacancies

    @staticmethod
    def cast_to_object(data):
        """
        Метод для преобразования списка JSON объектов в список объектов класса Vacancy
        :param data: Список JSON объектов
        :return: Список объектов Vacancy
        """
        vacancies = []

        for vacancy in data:
            obj_vacancy = Vacancy(vacancy["name"],
                                  vacancy["URL"],
                                  vacancy["to_salary"],
                                  vacancy["from_salary"],
                                  vacancy["requirements"],
                                  vacancy["responsibility"])
            vacancies.append(obj_vacancy)

        return vacancies
