# doctest --> find if REPL like things, execute them to see if they are working the way you want or not!
# match exception and reality

from math import hypot

# Class to represent 2-dimension vectors
# You can do this with complex type too
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__ is for debugging/programmer understanding
    # eval(repr(object)) --> debugging
    def __repr__(self):
        # return 'Vector(%r, %r)' % (self.x, self.y)
        # You can write it both ways
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        # hypot: Euclidean norm of an iterable of coordinates
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

"""
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 4)
>>> v1 + v2
Vector(4, 5)
"""

"""
>>> v = Vector(3, 4)
>>> abs(v)
5.0
"""

"""
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0
"""
if __name__=='__main__':
    import doctest
    doctest.testmod()
    # If you get nothing printed when you execute this code, it means everything works fine the way you want
    # No massage shown = Exception == reality
