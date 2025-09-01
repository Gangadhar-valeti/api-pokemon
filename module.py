#import math
'''import math as m

print(m.pi)'''


#enclosed scope
def fun1():
   x=1

   def fun2():
      print(x)
      fun2() 
        
fun1()
