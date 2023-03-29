class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Student(Person):
    def __init__(self, name, age, address, student_id, courses):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = courses

class Teacher(Person):
    def __init__(self, name, age, address, teacher_id, subject):
        super().__init__(name, age, address)
        self.teacher_id = teacher_id
        self.subject = subject