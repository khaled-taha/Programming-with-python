from abc import ABC, abstractmethod
import math
# Create a class
"""
ABC is a class from the abc module in Python.

If we extend any class with ABC and include any abstraction methods,
then the classes inherited from this class will have to mandatorily implement those abstract methods.

When we annotate any method with an abstractmethod keyword,
then it is an abstract method in Python (it won’t have any method implementation).

If the parent class has abstractmethod and not inherited from an abstract class,
then it is optional to implement the abstractmethod
"""
class Shape(ABC):

    # Class Attribute or Static member: static value for all objects
    system_name = 'Shape System'

    def __init__(self, color, isfilled):
        self.__color = color
        self.__isfilled = isfilled
        """
        Access Modifier:
            1 - Public (color)
            2 - private (__color)
            3 - protected (_color)
        """
    
    # getters and setters
    def setColor(self, color):
        self.__color = color
    
    def setFilled(self, isfilled):
        self.__isfilled = isfilled

    def getColor(self):
        return self.__color
    
    def getFilled(self):
        return self.__isfilled

    @abstractmethod    
    def getArea(self):
        pass
    
    # Overriding
    def printDetails(self):
        print('System Name: ', self.system_name)
        print('Color: ', self.getColor())
        print('Is Filled: ', self.getFilled())


class Circle(Shape):
    def __init__(self, color, isfilled, radius):
        super().__init__(color, isfilled)
        self.__radius = radius
    
    def setRadius(self, radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__isfilled
    
    
    def getArea(self):
        return self.__radius * self.__radius * math.pi
    
    # Overriding
    def printDetails(self):
        super().printDetails()
        print('Radius: ', self.__radius)


class Rectangle(Shape):
    def __init__(self, color, isfilled, length, width):
        super().__init__(color, isfilled)
        self.__length = length
        self.__width = width

    def setLength(self, length):
        self.__length = length
    
    def getLength(self, length):
        self.__width = length
    
    def setWidth(self, width):
        self.__length = width
    
    def getWidth(self, width):
        self.__width = width

    def getArea(self):
        return (self.__length + self.__width) * 2
    
    # Overriding
    def printDetails(self):
        super().printDetails()
        print('Length: ', self.__length)
        print('Width: ', self.__width)
    

circle = Circle('RED', False, 2)
# We can add an attribute to this object only and set this attribute with value from this point
circle.radius_point = (0, 0)

rectangle = Rectangle('RED', False, 2, 3)

print('Area: ', circle.getArea())
circle.printDetails()
print(circle.radius_point)

print('====================================')

print('Area: ', rectangle.getArea())
rectangle.printDetails()
# =========================================================
