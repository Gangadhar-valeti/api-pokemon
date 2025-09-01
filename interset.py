
import math


while p<0:
    print('enter the valid ammount')
p = int(input("Enter the initial amount: "))    


r = float(input("Enter the rate of interest (as a decimal): "))


t = float(input("Enter the time period (in years): "))
n = float(input("How many times is the interest compounded per year? "))

# Calculate total amount using the compound interest formula
total_amount = p * math.pow((1 + r / n), n * t)

# Output the result
print(f"The total amount is: {total_amount:.2f}")