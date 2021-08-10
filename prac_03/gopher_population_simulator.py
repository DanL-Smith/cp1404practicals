"""
CP1404/CP5632 - Practical
A program that simulates a population of gophers over a ten-year period and displays population size
"""
import random

MIN_INCREASE = 0.1
MAX_INCREASE = 0.2
MIN_DECREASE = 0.05
MAX_DECREASE = 0.25
INITIAL_POPULATION = 1000


def main():
    year = 1
    current_population = 1000

    print('Welcome to the Gopher Population Simulator!')
    print(f"Starting population: {INITIAL_POPULATION}")
    print(f"Year {year}\n")

    for i in range(99):
        year += 1
        gopher_births = determine_population_change(current_population, MIN_INCREASE, MAX_INCREASE)
        gopher_deaths = determine_population_change(current_population, MIN_DECREASE, MAX_DECREASE)
        current_population = (current_population + gopher_births) - gopher_deaths
        print(f"""{gopher_births:.0f} gophers were born. {gopher_deaths:.0f} gophers died.
Population: {current_population:.0f}
Year {year}\n""")


def determine_population_change(total, min, max):
    """Determines the change in population within a range of percent"""
    change = total * random.uniform(min, max)
    return change


main()
