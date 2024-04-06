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
        return (f"=====================================================\n"
                f"Название: {self.name}\n"
                f"URL: {self.url}\n"
                f"Зарплата: от {self.from_salary} до {self.to_salary}\n"
                f"Требования: {self.requirements}\n"
                f"Обязанности: {self.responsibility}\n"
                f"=====================================================")

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
