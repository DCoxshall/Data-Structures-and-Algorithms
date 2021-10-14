from math import sqrt

#Demonstration of operator overriding in Python. This is a simple 3d Vector class

class Vector:
    def __init__(self, *args):
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        else:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def mag(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        return f"Vector<{self.x}, {self.y}, {self.z}>"

    def dot(self, other):
        return sum([self.x  * other.x, self.y * other.y, self.z * other.z])

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __lt__(self, other):
        return self.mag() < other.mag()

    def __le__(self, other):
        return self.mag() <= other.mag()

    def __gt__(self, other):
        return self.mag() > other.mag()

    def __ge__(self, other):
        return self.mag() >= other.mag()

if __name__ == "__main__":
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)

    print(v1 < v2)
