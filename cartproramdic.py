menu={"chips":20,
      "drinks":40,
      "popcorn":50,
      "dairymilk":100,
      "soap":25,
      "bisket":26.5
      }
cart=[]
total=0
print("----------MENU----------")
for keys,values in menu.items():
    print(f"{keys:10} :  {values:.2f}/-")
print("-----------------------")    

while True:
    food=input("enter which one you want(q to exit)= ").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total+= menu.get(food)
    print(food,end=" ")    

print()
print(f"total is: {total:.2f}")
print("THANK YOU !")
print("VISIT AGAIN")
