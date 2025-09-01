#print("\u25CF \u250C \u2500 \u2501 )
'''
def happy(name):
    print(f"today is my birthday {name}")

happy("tillu")
happy("rockey")'''
    
def add(a,b):
   return a+b

print(add(1,3))    



n = int(input("Enter the number: "))
length = len(str(n))  # Convert n to string to get the length
sum = 0
temp = n  # Store the original number for comparison

# Iterate through each digit in the number
for i in str(n):
    sum += int(i) ** length  # Calculate the sum of each digit raised to the power of length

# Check if the sum is equal to the original number
if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
