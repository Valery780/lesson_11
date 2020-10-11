from random import randint

class City:
    def __init__(self):
        self.streets = []

    def generate_streets(self):
        self.streets.append([House()] * randint(5, 20))

    def get_population(self):
        population = 0
        for street in self.streets:
            for house in street.houses:
                population += house.people
        return population

    def count_streets(self):
        return len(self.streets)


class House:
    def __init__(self):
        self.people = randint(1, 100)


class Street:
    def __init(self):
        self.houses = []
        self.generate_houses()

    def generate_houses(self):
        for i in range(randint(5, 20)):
            self.houses.append((House()))

city = City()
city.generate_streets()
print(city.count_streets())
print(city.get_population())

