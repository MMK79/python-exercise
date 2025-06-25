class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started, Vroom Vroom!")
        else:
            print("Car is broken, :(")

# my_car = Car()
# print(f"Cars have {Car.get_number_of_wheels()} wheels.")
#
# my_car.number_of_wheels = 6
# print(f"Cars have {my_car.number_of_wheels} wheels.")
# print(f"Cars have {my_car.get_number_of_wheels()} wheels.")

class Imp_Car(object):
    number_of_wheels = 4

    @classmethod # whithout it we just get a warning
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def __str__(self):
        return self.name+"ba "+str(self.wheels)+" ta charkh"

    def get_name(self):
        return self.name

    def get_wheels(self):
        return self.wheels

    def set_name(self, new_car):
        self.name = new_car

    def set_wheels(self, new_wheels):
        self.wheels = new_wheels

my_imp_car = Imp_Car("Dena", 4)
print(my_imp_car)
print(f"my car is {my_imp_car.get_name()} with {my_imp_car.get_wheels()}")
my_imp_car.set_name("Shahing")
my_imp_car.set_wheels(6)
print(f"my car is {my_imp_car.get_name()} with {my_imp_car.get_wheels()}")
print(my_imp_car.get_number_of_wheels())

print(isinstance(my_imp_car, Car))
print(isinstance(my_imp_car, Imp_Car))
print(issubclass(bool, int))

# __str__ and __repr__ method usecase
import datetime
now = datetime.datetime.now()
# __str__ for end user use
print(f"string version {str(now)}")
# __repr__ for debuggin, under the hood, programmer use
print(f"repr version {repr(now)}")
