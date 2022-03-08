
import math


class Circle:

    def __init__(self, radius=1):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return math.pi * math.pow(self._radius, 2)

    def __repr__(self):
        return f"Circle({self._radius})"

