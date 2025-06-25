class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

# Inheritance
class Car(Vehicle):
    def __init__(self, make, model, fuel="gas"):
        # use super to use the parent class method
        super().__init__(make, model, fuel)
