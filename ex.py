class student():
    count = 0
    totalage = 0
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        student.count += 1
        student.totalage += age
    
    def get(self):
        return f"{self.name} is {self.age} years old"
    
    @classmethod
    def number(cls):
        return f"The number of students is {cls.count}"
    
    @classmethod
    def totalagee(cls):
        total_age_message = f"The total age of the students is {cls.totalage}"
        if cls.totalage > 21:
            return total_age_message + " - good"
        else:
            return total_age_message + " - bad"

# Creating student instances
stu1 = student("Fog", 12)
stu2 = student("Rockey", 14)

# Printing the number of students and total age
print(student.number()) 
print(student.totalagee())
