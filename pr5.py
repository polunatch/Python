# Завдання 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        sounds = {
            "cat": "Meow",
            "dog": "Woof",
            "cow": "Moo",
            "bird": "Chirp"
        }
        print(sounds.get(self.species.lower(), "Some sound"))

a1 = Animal("Murka", "cat", 3)
a2 = Animal("Buddy", "dog", 5)
a1.make_sound()
a2.make_sound()

# Завдання 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

r1 = Rectangle(4, 5)
r2 = Rectangle(7, 3)
print(r1.calculate_area())
print(r2.calculate_area())
# Завдання 1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    def start_engine(self):
        print(f"{self.make} {self.model} заводить двигун.")

    def display_info(self):
        print(f"Авто: {self.make} {self.model} ({self.year}), тип палива: {self.fuel_type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity
    def display_info(self):
        print(f"Мотоцикл: {self.make} {self.model} ({self.year}), об'єм двигуна: {self.engine_capacity} см³")
class Bicycle(Vehicle):
    def __init__(self, make, model, year, type_bike):
        super().__init__(make, model, year)
        self.type_bike = type_bike
    def display_info(self):
        print(f"Велосипед: {self.make} {self.model} ({self.year}), тип: {self.type_bike}")
car1 = Car("Toyota", "Corolla", 2020, "бензин")
bike1 = Motorcycle("Honda", "CBR500R", 2019, 500)
bicycle1 = Bicycle("Giant", "Escape 3", 2021, "міський")
# Завдання 2
vehicles = [car1, bike1, bicycle1]
for v in vehicles:
    v.display_info()
