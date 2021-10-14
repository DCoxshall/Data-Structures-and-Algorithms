from math import sqrt

# A simple n-dimensional vector class.


class Vector:
    def __init__(self, *argv):
        if len(argv) == 1:
            self.dimensions = argv[0]
        else:
            self.dimensions = [i for i in argv]

    def __eq__(self, other):
        if len(self.dimensions) != len(other.dimensions):
            raise(Exception("Vectors are not of the same order: cannot test equality"))
        for i in range(len(self.dimensions)):
            if self.dimensions[i] != other.dimensions[i]:
                return False
        return True

    def __lt__(self, other):
        if self.magnitude() < other.magnitude():
            return True
        return False

    def __le__(self, other):
        if self.magnitude() <= other.magnitude():
            return True
        return False

    def __gt__(self, other):
        if self.magnitude() > other.magnitude():
            return True
        return False

    def __ge__(self, other):
        if self.magnitude() >= other.magnitude():
            return True
        return False

    def __add__(self, other):
        newDimensions = []
        selfDims = self.dimensions
        otherDims = other.dimensions
        while (selfDims != [] and otherDims != []):
            newDimensions.append(selfDims[0] + otherDims[0])
            selfDims = selfDims[1:]
            otherDims = otherDims[1:]
        newDimensions += selfDims + otherDims
        return Vector(newDimensions)

    def __sub__(self, other):
        newDimensions = []
        selfDims = self.dimensions
        otherDims = other.dimensions
        while (selfDims != [] and otherDims != []):
            newDimensions.append(selfDims[0] - otherDims[0])
            selfDims = selfDims[1:]
            otherDims = otherDims[1:]
        newDimensions += selfDims + otherDims
        return Vector(newDimensions)

    def magnitude(self):
        return sqrt(sum([i ** 2 for i in self.dimensions]))

    def dot(self, other):
        if len(self.dimensions) != len(other.dimensions):
            raise(
                Exception("Vectors are not of the same order: dot product is undefined"))
        return(sum([self.dimensions[i] * other.dimensions[i] for i in range(len(self.dimensions))]))

    def cross(self, other):
        if len(self.dimensions) != len(other.dimensions):
            raise(
                Exception("Vectors are not of the same order, cross product is undefined"))
        if len(self.dimensions) > 3:
            raise(Exception("Cross product is not defined for vectors of order > 3."))
        newDims = []
        newDims.append(
            self.dimensions[1] * other.dimensions[2] - self.dimensions[2] * other.dimensions[1])
        newDims.append(
            self.dimensions[2] * other.dimensions[0] - self.dimensions[0] * other.dimensions[2])
        newDims.append(
            self.dimensions[0] * other.dimensions[1] - self.dimensions[1] * other.dimensions[0])
        return Vector(newDims)

    def __str__(self):
        vecString = 'Vector<'
        for i in self.dimensions:
            vecString += str(i) + ', '
        vecString = vecString[:-2]
        vecString += '>'
        return vecString
