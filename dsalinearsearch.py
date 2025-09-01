"""def search(list,key):
    for i in range (list):
        if key==list[i]:
            print(f"the {key} is found in list")
            break
        else:
            print(f"the {key} value is not found in the list")
    list=[3,1,5,83,4,5,6,7]
    key=int(input("enter the key value"))
    search(list,key)"""


def search(lst, key):
    found = False
    for i in range(len(lst)):
        if key == lst[i]:
            print(f"The {key} is found in the list.",i)
            found = True
            break
    if not found:
        print(f"The {key} value is not found in the list.")

# Define the list and get the key from user input
lst = [3, 1, 5, 6, 83, 4, 5, 6, 7]
key = int(input("Enter the key value: "))
search(lst, key)

