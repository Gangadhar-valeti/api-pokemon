f=open('object.py','r') #give file name with extensition and the mode
print(f.read())   #ctrl+space we get option to read the lines in the code

#here you have no file tillu it will first check folder it exists than write the data it not exist than create the file
f1=open('tillu','a')  # "a" means append already exist one data then another one you write then it aslo work
f1.write('i love pizza')

f2=open('tillu','w')  # the exist matter was remove the previous data in file means using "w"
f2.write('laptop')

#using loops
for data in f:
    print(data)

#printing the pic
f3=open('tillu.jpg','rb')#read binary=rb
f4=open('mypic.jpg','wb')
for i in f3:
    f1.write(i)

