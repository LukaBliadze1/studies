class Person:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self.name = name

class DisplayDetailsMixin:
    def display_details(self):
        return f"Student ID: {self._student_id}, Name: {self.name}, Average Grade: {self.average_grade:.2f}"

class AverageGradeMixin:
    @property
    def average_grade(self):
        total_grade = 0
        total_subjects = 0
        for grades in self._grades.values():
            total_grade += sum(grades)
            total_subjects += len(grades)
        if total_subjects == 0:
            return 0
        return total_grade / total_subjects

class StudentManagementMixin:
    def add_student(self, student):
        if student._student_id not in self.students:
            self.students[student._student_id] = student
        else:
            print("Student ID already exists. Cannot add the same student again.")

    def show_student_details(self, student_id):
        if student_id in self.students:
            return self.students[student_id].display_details()
        else:
            return "Student not found."

    def show_student_average_grade(self, student_id):
        if student_id in self.students:
            return f"Average Grade for Student ID {student_id}: {self.students[student_id].average_grade:.2f}"
        else:
            return "Student not found."

class Student(Person, DisplayDetailsMixin, AverageGradeMixin):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self._grades = {}

    def add_grade(self, subject, grade):
        if subject not in self._grades:
            self._grades[subject] = []
        self._grades[subject].append(grade)

class StudentManagementSystem(StudentManagementMixin):
    def __init__(self):
        self.students = {}

sms = StudentManagementSystem()
student1 = Student(1, "Alice")
student2 = Student(2, "Bob")
sms.add_student(student1)
sms.add_student(student2)
student1.add_grade("Math", 90)
student1.add_grade("Science", 85)
student2.add_grade("Math", 78)
student2.add_grade("Science", 92)
print(sms.show_student_details(1))
print(sms.show_student_details(2))
print(sms.show_student_average_grade(1))
print(sms.show_student_average_grade(2))
