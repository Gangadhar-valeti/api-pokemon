'''import re
gmail=input("enter your mail=")
maillog="^[a-z][A-Z][0-9][@]gmail.com$"
if re.match(maillog, gmail):
    print("Valid Gmail")
else:
    print("Invalid Gmail")'''



import re
maillog = r"^[a-zA-Z0-9]+@gmail\.com$"
passkey = r"^[a-zA-Z0-9@]+$"
running = True
while running:
    gmail = input("Enter your email: ")
    if re.match(maillog, gmail):
        password = input("Enter your password: ")
        if re.match(passkey, password):
            print("Correct details")
            running = False  
        else:
            print("Not valid password")
    else:
        print("Invalid Gmail")