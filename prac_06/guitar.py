"""CP1404/CP5632 Practical - Guitar class"""
CURRENT_YEAR = 2021


class Guitar(object):
    """Represent a Guitar object"""
    def __init__(self, name='', year=0, cost=0):
        """Initialize a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """Get the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage (50 years or older)"""
        return True if self.get_age() >= 50 else False
