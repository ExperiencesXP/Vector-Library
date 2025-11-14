from math import acos,pi
class Vector:
    def  __init__(self,x,y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    def __str__(self):
        return f"{self.__x},{self.__y}"
    def __add__(self,vec:'Vector'):
        return Vector((self.__x + vec.__x),(self.__y + vec.__y))
    def __sub__(self,vec:'Vector'):
        return Vector((self.__x - vec.__x),(self.__y - vec.__y))
    def __mul__(self, k):
        return Vector(self.__x * k, self.__y * k)
    def __truediv__(self, k):
        try:
            return self * (1/k)
        except:
            raise ValueError
    
    def length(self):
        return (self.__x**2 + self.__y**2)**0.5
    def distance(self,vec:'Vector'):
        return (self-vec).length()
    def normalize(self):
        try:
            return self / self.length()
        except:
            raise ValueError
    def dotProduct(self,vec:'Vector'):
        return self.__x*vec.__x + self.__y*vec.__y
    def limit(self,tallimit):
        if not self.length() > tallimit:
            return self
        return self.normalize() * tallimit
    def angleBetween(self,vec:'Vector',useDegrees:bool=False):
        if useDegrees:
            return acos(self.dotProduct(vec)/(self.length() * vec.length()))*(180/pi)
        else:
            return acos(self.dotProduct(vec)/(self.length() * vec.length()))
