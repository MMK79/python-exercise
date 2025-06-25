class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom, Vroom!")
        else:
            print("Car is broken! :(")

# Create instance of a class
my_car = Car()
print(f"My car runs: {my_car.runs}")
my_car.start()
# Change runs value
my_car.runs = False
print(f"My car runs: {my_car.runs}")
my_car.start()

# Other instance of a class
my_other_car = Car()
print(f"My other car runs: {my_other_car.runs}")
my_other_car.start()
