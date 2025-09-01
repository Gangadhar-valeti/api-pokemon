'''class animal:
    def __init__(self,name):
        self.name=name
        self.is_living=True
        self.is_sleep=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def living(self):
        print(f"{self.name} is livingin the world")         
            
class dog(animal):
    pass
class cat(animal):
    pass
class cow(animal):
    pass  

dog=dog("rockey")
cat=cat("meow")
cow=cow("pinky")

print(dog.name)
print(cow.is_living)
print(cat.is_sleep)

cow.eat()
cow.living()
dog.sleep()
cat.living()


'''
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_living = True
        self.is_sleeping = False

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        self.is_sleeping = True
        print(f"{self.name} is sleeping")

    def living(self):
        print(f"{self.name} is living in the world")


class Dog(Animal):
    def speck(self):
        print("bow bow")


class Cat(Animal):
    pass


class Cow(Animal):
    pass


# Creating instances of each animal
dog = Dog("Rockey")
cat = Cat("Meow")
cow = Cow("Pinky")

# Accessing attributes
print(dog.name)  # Output: Rockey
print(cow.is_living)  # Output: True
print(cat.is_sleeping)  # Output: False

# Calling methods
cow.eat()  # Output: Pinky is eating
cow.living()  # Output: Pinky is living in the world
dog.sleep()  # Output: Rockey is sleeping
cat.living()  # Output: Meow is living in the world
dog.speck()