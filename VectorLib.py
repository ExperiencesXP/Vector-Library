from typing import TypeAlias

from math import acos, pi, sqrt, isclose

Scalar: TypeAlias = int | float


class Vector:
    def __init__(self, x: Scalar, y: Scalar):
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> Scalar:
        return self.__x
    
    @x.setter
    def x(self, comp: Scalar) -> None:
        self.__x = comp
    
    @property
    def y(self) -> Scalar:
        return self.__y
    
    @y.setter
    def y(self, comp: Scalar) -> None:
        self.__y = comp
    
    def __repr__(self):
        return f"Vector({self.__x!r}, {self.__y!r})"
    
    def __str__(self):
        return f"{self.__x}, {self.__y}"
    
    def __add__(self, vec: 'Vector') -> 'Vector':
        return Vector((self.__x + vec.__x),(self.__y + vec.__y))
    
    def __sub__(self, vec: 'Vector') -> 'Vector':
        return Vector((self.__x - vec.__x),(self.__y - vec.__y))
    
    def __mul__(self, k: Scalar) -> 'Vector':
        return Vector(self.__x * k, self.__y * k)
    
    def __truediv__(self, k: Scalar) -> 'Vector':
        try:
            return self * (1/k)
        except:
            raise ValueError

    def __eq__(self,other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.__x == other.__x and self.__y == other.__y
    
    def almost_equal(self, other: 'Vector', abs_tol: float = 1e-9, rel_tol: float = 1e-9):
        if not isinstance(other, Vector):
            return NotImplemented
        return (isclose(self.__x, other.__x, rel_tol=rel_tol, abs_tol=abs_tol) and isclose(self.__y, other.__y, rel_tol=rel_tol, abs_tol=abs_tol))

    def length(self) -> float:
        return sqrt(self.__x**2 + self.__y**2)
    
    def distance(self, vec: 'Vector') -> float:
        return (self-vec).length()
    
    def normalize(self) -> 'Vector':
        try:
            return self / self.length()
        except:
            raise ValueError
        
    def dotProduct(self, vec: 'Vector') -> float:
        return float(self.__x)*float(vec.__x) + float(self.__y)*float(vec.__y)
    
    def limit(self, tallimit: Scalar) -> 'Vector':
        if not self.length() > tallimit:
            return self
        return self.normalize() * tallimit
    
    def angleBetween(self, vec: 'Vector', useDegrees: bool = False) -> float:
        if useDegrees:
            return acos(self.dotProduct(vec)/(self.length() * vec.length()))*(180/pi)
        else:
            return acos(self.dotProduct(vec)/(self.length() * vec.length()))
