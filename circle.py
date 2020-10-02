import math


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
        self.diameter = diameter

    @property
    def area(self):
        return self.radius**2*math.pi

