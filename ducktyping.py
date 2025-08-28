'''duck typing=another way to achhive polymorphism besides 
                inheritance object must have the minimum necessary TTRIBUTES/mthods 
'''
class animal:
  alive=True
class dog(animal):
  def speak(self):
    print("bark" )
class cat(animal):
  def speak(self):
    print("meow")

class car:

  alive=False
  def speak  (self):
    print("poie poie")


animals=[dog(),cat(),car()]
for animal in animals:
  animal.speak()  
  print(animal.alive)
