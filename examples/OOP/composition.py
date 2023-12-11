from datetime import date

class Car:
    # constructor
    def __init__(self, name="BMW", model="X1", year=2019):
        self.name = name
        self.model = model
        self.year = year
    # class method
    def average_mileage(self, average_by_year=10000):
        return (date.today().year - self.year) * average_by_year

class Garage:
    def __init__(self, *cars):
        self.cars = cars

    def print_all_cars(self):
        for car in self.cars:
            print("**************")
            print(f'Car {car.name}/{car.model}, year: {car.year}')

bmw = Car("BMW","m3", 2020)
mercedes = Car("Mercedes","c180", 2016)
garage = Garage(bmw,mercedes)
garage.print_all_cars()