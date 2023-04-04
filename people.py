class Person:
    def __init__(self, name, age, address):
        # Initialize a new Person object with a name, age, and address
        self.name = name
        self.age = age
        self.address = address

class Student(Person):
    def __init__(self, name, age, address, student_id, courses):
        # Initialize a new Student object with a name, age, address, student ID, and list of courses
        super().__init__(name, age, address)
        self.student_id = student_id
        self.courses = courses

class Teacher(Person):
    def __init__(self, name, age, address, teacher_id, subject):
        # Initialize a new Teacher object with a name, age, address, teacher ID, and subject
        super().__init__(name, age, address)
        self.teacher_id = teacher_id
        self.subject = subject
 