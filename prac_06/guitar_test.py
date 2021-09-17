"""CP1404/CP5632 Practical - Guitar Class Test Program"""
from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 2567.20)
print(f"{guitar1.name} get_age() - expected 99. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - expected 8. Got {guitar2.get_age()}")
print(f"{guitar1.name} is_vintage() - expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - expected False. Got {guitar2.is_vintage()}")
