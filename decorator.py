def chaco(func):
    def wapper(*args,**kwargs):
        print("You add the chaco🍫")  # decorator function
        func(*args,**kwargs)
    return wapper  # Return the wrapper function without calling it

def icee(func):
    def wapper(*args,**kwargs):
        print("You add ice on the ice cream🧊")
        func(*args,**kwargs)
    return wapper  # Return the wrapper function without calling it

@chaco  # decorator function
@icee
def icecream(falour):
    print(f"I want {falour}✌🏼 ice cream 🍦 now")  # base function

icecream("vinella")  # Call the decorated function
