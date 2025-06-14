class Circle(object):
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        pi = 3.14
        return pi*( self.radius )**2

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self.radius == c.radius

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self.radius > c.radius:
            return self
        elif self.radius < c.radius:
            return c
        else:
            return ( self, c )

a = Circle(5)
b = Circle(5)
print(a)
print(type(a))
print(a.get_radius())
a.set_radius(6)
print(a.get_radius(), 'after set redius to 6')
print(a.get_area())
print(a.equal(b), f"radius of a is {a.get_radius()}, and radius of b is {b.get_radius()}")
print(a.bigger(b))
