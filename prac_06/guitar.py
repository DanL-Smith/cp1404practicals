CURRENT_YEAR = 2021


class Guitar(object):
    def __init__(self, name = '', year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return True if Guitar.get_age(self) >= 50 else False
