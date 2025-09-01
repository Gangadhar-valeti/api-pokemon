 #poly = many
# morphe= form
""" two ways to acieve the polymorphim
1. inheritane
2. duck type"""
from abc import ABC,abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2 
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2    
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width    
class triangle(shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base
    def area(self):
        return 0.5*self.height*self.base

class pizza(circle):
    def __init__(self,topped,radius):
        self.topped=topped
        self.radius=radius    
            
shapes=[circle(4),square(7),rectangle(7,3),triangle(3,8),pizza("spicy",15)]
for shape in shapes:
    print(f"{shape.area()}cm²") 