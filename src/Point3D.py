import math


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def Distance(self, Other):
        xPow = math.pow(Other.x - self.x, 2)
        yPow = math.pow(Other.y - self.y, 2)
        zPow = math.pow(Other.z - self.z, 2)
        return math.sqrt(xPow+yPow+zPow)
