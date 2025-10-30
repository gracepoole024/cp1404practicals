class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __get_age__(self):
        self.age = 2025 - self.year

    def __is_vintage__(self):
        return self.age >= 50

    def __str__(self, age):
        return f"{self.name} ({age}) : ${self.cost}"
