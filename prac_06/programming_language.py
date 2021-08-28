"""CP1404/CP5632 Practical - Programming language class"""


class ProgrammingLanguage(object):
    """Initialize a programming language instance"""
    def __init__(self, name='', typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if instance is dynamic"""
        return True if self.typing.lower() == "dyanmic" else False