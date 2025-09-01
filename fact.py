a,b=0,1  #factorial
n=7
for i in  range (n):
    print(a,end=" ")
    a,b=b,a+b
print("",end=" ",)

print("finding prime numbers")
num=int(input("enter the number="))
for i in range(2,num):
    if num%i==0:
        print(" not a prime number")
        break
    else:
        print(" prime number")    
    print(" ",end=" ")        


print("arm strong")

n=int(input("enter the nuber="))
length=len(str(n))
sum=0
for i in  (str(n)):
    sum +=int(i)**length
if sum==n:
        print("arm strong number")
else:
        print("not a arm strong")  


print("palindrome of number")
n=int(input("enter the number="))
originalnum=n
reversenum=0
while n>0:
     digit=n%10
     reversenum=reversenum*10+digit
     n=n//10
     
if originalnum==reversenum:
          print("palindrome")
else:
          print("not palindrome")     

          
          



    