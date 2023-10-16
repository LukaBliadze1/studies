class Student:
    university = "University" 

    def __init__(self, name, grade, age):
        self.name = name 
        self.grade = grade  
        self.age = age  

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age) + ", Grade: " + str(self.grade)  

    @property
    def is_passing(self):
        return self.grade > 60  

    def increase_grade(self, amount):  
        self.grade += amount

student1 = Student("Nika", 50, 22)
student2 = Student("Luka", 61, 23 )

print(str(student1))
print(str(student2))

print(student1.name,'-', student1.is_passing) 
print(student2.name,'-', student2.is_passing)

student1.increase_grade(10)
student2.increase_grade(10)
print(student1.name,'-', student1.grade)
print(student2.name,'-', student2.grade)