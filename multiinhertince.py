class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Prey(Animal):
    def praying(self):
        print("The animal is praying for living")

class Hunter(Animal):
    def hunt(self):
        print("It is living for hunting")

class Rabbit(Prey):
    pass

class Tiger(Hunter):
    pass

class Fish(Prey, Hunter):
    pass

# Create instances of each class
rabbit = Rabbit()
tiger = Tiger()
fish = Fish()

# Call methods on the instances
tiger.hunt()
fish.praying()
rabbit.sleep()

 



