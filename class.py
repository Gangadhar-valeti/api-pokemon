class student():
    count=0
    totalage=0
    def __init__(self,name,age): 
        self.name=name
        self.age=age
        student.count+= 1
        student.totalage+=age
    def get(self):
        return  f"{ self.name} is {self.age} old "
    @classmethod
    def number(cls):
        return f" the no of students are ={cls.count}"
    @classmethod
    def totalagee(cls):
        return f"the total age of the student is={cls.totalage}"
        if cls.totalage >21:
            return "good"
        else:
            return "bad"    
stu1=student("fog",12)
stu2=student("rockey",14)   
print(student.number()) 
print(student.totalagee())   