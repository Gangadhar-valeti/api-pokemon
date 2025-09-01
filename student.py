class student:
    clasyear=2025
    numstudents=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.numstudents+=1
student1=student("tillu",20) 
student2=student("hemanth",18)
student3=student("manu",65)
print(student2.name)
print(student1.age)       