class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class AttributeFormatterMixin:
    def format_attributes(self):
        return f"name: {self.name}, surname: {self.surname}, age: {self.age}"

class Student(Person, AttributeFormatterMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

    def formatted_info(self):
        return self.format_attributes() + f", university: {self.university}"
    
person = Person("Jordan", "Peterson", 30)
student = Student("Joe", "Rogan", 25, "JRE University")

print(person.name, person.surname, person.age)
print(student.name, student.surname, student.age, student.university)
print(student.formatted_info())