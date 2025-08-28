n=5
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print("*",end=" ")
    print()        

#new one

n=5
for rows in range(1,n+1):
    for colns in range(n-rows+1):
        print("*",end=" ")
    print()       


#3
n=5 
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print(rows,end=" ")
    print()   

#4
n=5
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print(colns,end=" ")
    print()  


#5
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range(1,rows+1):
         print("*",end=" ")  
    print()    


print("6 th onre")
n=5
for rows in range(1,n+1):
    for spped in range(1,rows):
        print(" ",end=" ")
    for colns in range(1,n-rows+2):
        print('*',end=" ")
    print()  


print("7th pattern") 
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range(1,2*rows-1+1):
        print("*",end=" ")
    print()                 

print("8th pattern")
n=5
for rows in range(1,n+1):
    for space in range(1,rows+1):
        print(" ",end=" ")
    for coln in range(1,(n-rows)*2):
        print("*",end=" ")
    print()           

print("9th pattern ")
n=5
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print("*",end=" ")
    print()  
for rows in range(1,n):
    for colns in range(1,n-rows+1):
        print("*",end=" ")
    print() 

print("10th pattern")
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range (1,rows+1):
        print("*",end=" ")
    print()
for rows in range(1,n):
    for space in range(1,rows+1):
        print(" ",end=" ")
    for colns in range (1,n-rows+1):
        print("*",end=" ")
    print()   

print("11 pattern")
n=5
for rows in range(1,n+1):
    for spaces in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range(1,2*rows):
        print("*",end=" ")
    print()  
for rows in range(1,n+1):
    for spaces in range(1,rows+1):
        print(" ",end=" ")
    for colns in range(1,(n-rows)*2):
        print("*",end=" ")
    print() 

print("12 pattern")
for rows in range(1,n+1):
    
     for colns in range (1,n+1):
        if rows==1 or rows==n or colns==1 or colns==n:
         print("*",end=" ")
        else:
            print(" ",end=" ") 
     print()    


print(" 13 th programm")
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range(1,rows+1):
        if rows==n or colns==1  or colns==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
 
print("14 th programm")
n=5
for rows in range(1, n + 1):  
    for space in range(n-rows+1):  
        print(" ", end=" ")
    for colns in range(1, 2 * rows):
        if colns== 1 or colns == 2 * rows - 1 or rows == n:  
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()    

print('15 th programm')
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range(1,2*rows):
        if   colns==1 or colns==2*rows-1:
         print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()       
for rows in range(1,n):
    for space in range(1,rows+1):
        print(" ",end=" ")
    for colns in range(1,(n-rows)*2):
        if colns==1 or colns==(n-rows)*2-1:
         print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()  

print("16 th pattern")
n=5
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print(chr(rows+64),end=" ")
    print( ) 

print("17 th pattern")
n=5
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print(chr(colns+rows+63),end=" ")
    print( ) 

print("18 th patttern" )
n=5
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print("*",end=" ")
    for space in range(1,(n-rows)*2):
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print("*",end=" ")
    print()  
for rows in range(n,0,-1):
    for colns in range(1,rows+1):
        print("*",end=" ")
    for space in range(1,(n-rows)*2):
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print("*",end=" ")
    print()          

print("19 th pattern ")
n=5
for rows in range(1,n+1):
    for colns in range(1,n+1):
        if ((colns+rows)%2)==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()            


print("20 pattern ")


n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1):
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print(colns,end=" ")
    for  colns in range(rows-1,0,-1): # own logic bulid
        print(colns,end=" ")
    print()           

print("21 pattern")
n=5
for rows in range(1,n+1):
    for space in range(1,n-rows+1) :
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print(colns ,end=" ")
    for colns in range(rows-1,0,-1):
        print(colns,end=" ")
    print()       
for rows in range(n-1,0,-1):
    for space in range(1,n-rows+1) :
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print(colns ,end=" ")
    for colns in range(rows-1,0,-1):
        print(colns,end=" ")
    print()  
print("22 pattern")
n=5    
for rows in range(1,n+1):
    for space in range(1,n-rows+1) :
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print(chr(colns+64) ,end=" ")
    for colns in range(rows-1,0,-1):
        print(chr(colns+64),end=" ")
    print()       
for rows in range(n-1,0,-1):
    for space in range(1,n-rows+1) :
        print(" ",end=" ")
    for colns in range(1,rows+1):
        print(chr(colns+64) ,end=" ")
    for colns in range(rows-1,0,-1):
        print(chr(colns+64),end=" ")
    print()

print("23 pattern")
n=5
num=1
for rows in range(1,n+1):
    for colns in range(1,rows+1):
       print(num,end=" ")
       num +=1
    print() 

print("24 pattern")
n=5
num=15
for rows in range(1,n+1):
    for colns in range(1,rows+1):
        print(num,end=" ")
        num-=1
    print()



print("25 pattern")
n = 5
for rows in range(1,n+1 ):  # Outer loop for rows
    num = 1
    for space in range(1,n-rows+1):  # Inner loop for spaces
        print(" ", end=" ")
    for colns in range(1,rows + 1):  # Inner loop for numbers
        print(num, end="   ")
        num = num * (rows - colns) // colns   # Calculate Pascal's number
    print()  
      
def print_pascal_triangle(n):
    for rows in range(1, n + 1):
        num = 1
        for colns in range(1, n - rows + 1):
            print(" ", end=" ")
        for colns in range(1, rows + 1):
            print(num, end="   ")
            num = num * (rows - colns) // colns
        print()

n = 5
print_pascal_triangle(n)


print("26 pattern")
n = 8
for rows in range(1, n + 1):
    for colns in range(1, rows + 1):
        # multiplication current column and row
        print(rows*colns, end='  ')
    print()


print("27 pattern ")
n=5
for rows in range(1,n+1):
    for colns in range(1,n+1):
        if rows==colns or rows+colns==n+1:
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()     


print("28 pattern ")
n=5
for rows in range(1,n+1):
    for colns in range(1,n+1):
        if  rows == n  // 2 + 1 or colns == n  // 2 + 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   


print("ducking typing")
class animal():
    alive=True
class dog(animal):
    def speak(self):
        print("boww")
class cat (animal):
    def speak(self):
        print("meowww")
class car:
    alive=False
    def speak(self):
        print("poie poie")

animals=[dog(),car(),cat()]        
for animal in animals:
    animal.speak()  
    print(animal.alive) 




                   





   