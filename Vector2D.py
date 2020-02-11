import math


class Vector2D:
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return str(self.v)

    def __getitem__(self, item):
        return self.v[item]

    def __setitem__(self, key, value):
        self.v.__setitem__(key, value)

    # basic vector operations
    def __add__(self, other):
        return Vector2D([self.v[0] + other.v[0], self.v[1] + other.v[1]])

    def __sub__(self, other):
        return Vector2D([self.v[0] - other.v[0], self.v[1] - other.v[1]])

    # scalar multiplication
    def __mul__(self, other):
        return Vector2D([self.v[0] * other, self.v[1] * other])

    # dot product of two vectors
    def dot_product(self, other):
        return self.v[0] * other.v[0] + self.v[1] * other.v[1]

    # projection of vector v on a unit vector n
    def projection(self, n):
        d = self.dot_product(n)
        return n * d

    # rejection of vector v on a unit vector n
    def rejection(self, n):
        return self - self.projection(n)

    def norm(self):
        return math.sqrt(self.v[0] ** 2 + self.v[1] ** 2)
