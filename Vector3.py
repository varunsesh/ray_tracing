import math


class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return(f"({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        result = Vector3()
        result.x = self.x + other.x
        result.y = self.y + other.y
        result.z = self.z + other.z
        return result

    def length(self):
        result = math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
        return result

    def __mul__(self, t):
        result = Vector3()
        result.x = self.x*t
        result.y = self.y*t
        result.z = self.z*t 
        return result

    def __truediv__(self, t):
        result = Vector3()
        result.x = self.x/t
        result.y = self.y/t
        result.z = self.z/t 
        return result

    def dot(self, other):
        result = self.x*other.x + self.y*other.y + self.z*other.z
        return result
        
    def unit_vec(self):
        result = Vector3()
        result.x, result.y, result.z = self.x/self.length(), self.y/self.length(), self.z/self.length()
        return result


        
