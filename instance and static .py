class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        return f"{self.name} is barkin like bow bow"
    
mydog=dog("tillu",3)
print(mydog.name)
print(mydog.age)
print(mydog.bark())