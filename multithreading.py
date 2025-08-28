#multithreading=uesd to perform multiple tasks concurrently(multitasking)
#               good for i/0 bound tasks like reading files files  or fetching data from APIs
#               threading 
#               Thread(target=my_function)
import threading
import time

def iswalking(name):
    time.sleep(4) 
    print(f" {name} is walking on the road")

def getmail():
    time.sleep(2)
    print(" the mail will get in 2 sec")

def getsleep(times):
    time.sleep(3)
    print(f"you are going to sleep at {times}")    
 #it is same as the chore methos  but chore method we are using the threading concept 
chore1=threading.Thread(target=getmail)
chore1.start()
chore2=threading.Thread(target=iswalking,args=("raju",))
chore2.start()
chore3=threading.Thread(target=getsleep,args=("10 pm",))
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print(" all the tasks are completed")