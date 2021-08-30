"""CP1404/CP5632 Practical - language Program"""
from prac_06.programming_language import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
programming_languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
[print(language.name) if language.is_dynamic() else "" for language in programming_languages]
