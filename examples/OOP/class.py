from datetime import date

class Car:
    # constructor
    def __init__(self, name="BMW", model="X1", year=2019):
        self.name = name
        self.model = model
        self.year = year
    def average_mileage(self, average_by_year=10000):
        return (date.today().year - self.year) * average_by_year

car1 = Car("Hyundai","IX35",2013)
print(car1.name)
print(car1.model)
print(car1.year)
print(car1.average_mileage(5000))

car2 = Car()
print(car2.name)
print(car2.model)
print(car2.year)
print(car2.average_mileage())

