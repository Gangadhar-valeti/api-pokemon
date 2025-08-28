import datetime
try:
    date=datetime.date(2001,4,6)
    today=datetime.date.today() #today means get the todays date
    print(date)
    print(today)
    time=datetime.time(12,54,32)
    print(f"time={time}")
    now=datetime.datetime.now() # now means get the todays time  we use date time then we get the date&time
    print(now)
except ValueError:
    print("some thing went wrong")    