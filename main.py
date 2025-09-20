# Seyed Tahmoores Khoshnoud Moghadam

from data import countries_and_capitals
from country import Country
import random

def main():
    """
    :return:
        - Creates a list of Country objects with random populations between 1 million and 1 billion.
        - Handles any ValueError exceptions by printing "oops" along with the error message.
        - Prints details of each country.
        - Increases the population of each country by 1 and prints details again.
        - Decreases the population of each country by 1 and prints details again.
        - Handles population decrease due to disaster and prints details again.
    """

    all_countries = []
    try:
        for country, capital in countries_and_capitals:
            population = random.randint(1000000, 1000000000)
            new_country = Country(country, capital, population)
            all_countries.append(new_country)
    except ValueError as v:
        print("OOPS")
        print(v)

    for country in all_countries:
        country.print_details()

    print("\nAFTER BIRTHS:")
    for country in all_countries:
        country.birth()
        country.print_details()

    print("\nAFTER DEATHS:")
    for country in all_countries:
        country.death()
        country.print_details()

    print("\nAFTER DISASTERS:")
    for country in all_countries:
        country.disaster()
        country.print_details()


if __name__ == "__main__":
    main()
