from math import sqrt

# A simple n-dimensional vector class.


class Vector:
    def __init__(self, *argv):
        if len(argv) == 1:
            self.dimensions = argv[0]
        else:
            self.dimensions = [i for i in argv]

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

    def __str__(self):
        vecString = 'Vector<'
        for i in self.dimensions:
            vecString += str(i) + ', '
        vecString = vecString[:-2]
        vecString += '>'
        return vecString


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)
