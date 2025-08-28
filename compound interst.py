principal=0
time=0
rate=0

while principal <= 0:
    principal=float(input("enter the principal ammount="))
    if principal <=0:
        print("princial ammount not negative ")

while rate <= 0:
    rate=float(input("enter the rate ammount="))
    if rate <=0:
        print("rate ammount not negative ")

while time <= 0:
    time=int(input("enter the time ammount="))
    if time <=0:
        print(" time not negative ")        

print(f"your principal ammount is={principal}")    
print(f"your rate of ammount is={rate}")
print(f"your time is={time}")

ammount=principal*pow(1+rate/100,time)
print(f"your compound interset is{ammount}")

           
       
