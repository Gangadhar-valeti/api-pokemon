try:
    n=int(input("enter the number="))
    print(1/n)
except ZeroDivisionError:   # any thing has a zerodivision error
        print("we cannot divide by zero ")
except ValueError:         # any thing has a value error
      print("enter only the number") 
except Exception:          # other than the two errors is exception
      print("something went wrong")    
finally:
      print("do some clean up here")                   