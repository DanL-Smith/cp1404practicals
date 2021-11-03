"""CP1404/CP5632 Practical - Programming language class"""


class ProgrammingLanguage(object):
    """Represent a programming language Object"""
    def __init__(self, name='', typing="", reflection="", year=0):
        """Initialize a programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if instance is dynamic"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, first appeared in {self.year}"
