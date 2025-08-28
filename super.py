# super= functionn used in the child class methods from a parent class.
'''class shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
class square(shape):
    def __init__(self,color,is_filled,side):
        super().__init__(color,is_filled)
        self.side=side
    
class triangle(shape):
    def __init__(self,color,is_filled,side,height):
        self.color=color
        super().__init__(color,is_filled)
        self.height=height
Circle=circle("blue",True,3) '''   
import math
class shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        return  math.pi*self.radius*self.radius

class square(shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

class triangle(shape):  # Corrected the class name
    def __init__(self, color, is_filled, side, height):
        super().__init__(color, is_filled)  # Call to super() should be first
        self.side = side
        self.height = height

# Example of creating a circle object
Circle = circle("blue", True, 3)
print(Circle.color)
print(Circle.radius)
print(Circle.area())

