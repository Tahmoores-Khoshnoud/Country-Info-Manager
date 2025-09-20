# Seyed Tahmoores Khoshnoud Moghadam

class Country:
    """
    Represents a country with its name, capital, and population.
    print_details: Prints details of the country.
    birth: Increases the population of the country by 1.
    death: Decreases the population of the country by 1.
    disaster: Handles population decrease due to disaster.
    """

    def __init__(self, country_name, capital_name, population):
        self.country_name = country_name
        self.capital_name = capital_name
        if population < 2000000:
            raise ValueError(f"Population {population} is too low")
        else:
            self.population = population

    def print_details(self):
        print(f"The capital of {self.country_name} (pop. {self.population}) is {self.capital_name}")

    def birth(self):
        self.population += 1

    def death(self):
        self.population -= 1

    def disaster(self):
        if self.population >= 100000000:
            self.population -= 100000000
        else:
            self.population = 0

