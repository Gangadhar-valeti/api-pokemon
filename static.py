# static method= a method the belong to a class rater then any object from that class
# (instance) usually used for general utility function
# instancr methods= best for opertion on instances o fthe class(objects)
# static method= best for utility function that do not need acess to class data 
class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def data(self):  
        return f"{self.name}={self.position}"
    
    def validposition(position):
        valid_position=["manager","clerck","cook","casher"]
        return position in valid_position
employee1=employee("tillu","manger")
employee2=employee("hemanth","ceo")
employee3=employee("rocky","cook")
employee4=employee("roy","casher")

print(employee.validposition("cook"))
print(employee1.data())
print(employee2.data())
print(employee3.data())
print(employee4.data())



