class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(c.radius + self.radius)

    def __str__(self):
        """ A Circle's string representation is the radius """
        return  "<"+str(self.radius)+">"

a = Circle(6)
b = Circle(7)
print(a.get_radius())
c = a + b
print(c)
