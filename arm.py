num = input("Enter the number: ")
num_length = len(num)
sum_of_powers = 0
for i in num:
    sum_of_powers += int(i) ** num_length
if sum_of_powers == int(num):
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")