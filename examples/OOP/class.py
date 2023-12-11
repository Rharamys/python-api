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

# hierarchy (SportCar extends Car)
class SportCar(Car):
    def __init__(self, name, model, year, wheels_size, turbo):
        Car.__init__(self, name, model, year)
        self.wheels_size = wheels_size
        self.turbo = turbo
    def getName(self):
        return f'''Car model {self.name}/{self.model} with wheels size {self.wheels_size}'''

class EletricCar(Car):
    def __init__(self, name="BMW", model="X1", year=2019):
        # using super() doesnt need to provide the self parameter
        super().__init__(name, model, year)
    def average_mileage(self):
        battery_health = 100 - ((date.today().year - self.year) * 10)
        return f'''Battery health {battery_health}%'''
        
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

car3 = SportCar("BMW", "M3", 2019, 22, True)
print(car3.name)
print(car3.model)
print(car3.year)
print(car3.wheels_size)
print(car3.turbo)
print(car3.average_mileage())
print(car3.getName())

car4 = EletricCar("BMW", "i8", 2020)
print(car4.name)
print(car4.model)
print(car4.year)
print(car4.average_mileage())
