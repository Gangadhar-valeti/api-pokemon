import math
shape = input("which shape do you wish to calculate for?: ")
if shape == "rectangle":
    print(f"To calculate the area of a {shape},")
    length = float(input("What is the length?: "))
    breadth = float(input("What is the breadth?: "))
    print(f"The area of the rectangle is {round(length * breadth,2)}")
elif shape == "circle":
    print(f"To calculate the area of a {shape},")
    radius = float(input("what is your radius?: "))
    area = math.pi * pow(radius,2)
    print(f"The area of the circle is {round(area,2)}cm²")
elif shape == "square":
    print(f"To calculate the area of a {shape},")
    length = float(input("What is your length?: "))
    print(f"The area of the {shape} is {round(length**2,2)}")
elif shape == "cylinder":
    print(f"To calculate the area of a {shape},")
    radius = float(input("what is your radius?: "))
    length = float(input("What is the length?: "))
    area = math.pi * pow(radius,2) * length
    print(f"The area of the {shape} is {round(area,2)}cm²")
elif shape == "trapezium":
    print(f"To calculate the area of a {shape},")
    a = float(input("what is your a?: "))
    b = float(input("what is your b?: "))
    height = float(input("what is your height?: "))
    area = a + b
    area = area * height / 2
    print(f"The area of the {shape} is {round(area,2)}cm²")
elif shape == "triangle":
    print(f"To calculate the area of a {shape},")
    base_area = float(input("what is your base_area?: "))
    height = float(input("what is your height?: "))
    area = 1/2 * base_area * height
    print(f"The area of the {shape} is {round(area,2)}cm²")
else:
    print("we are coming to that!")