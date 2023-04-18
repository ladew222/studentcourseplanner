class Person:
    def __init__(self, id, name):
        # Initialize a new Person object with a name, age, and address
        self.id = id
        self.name = name

class Student(Person):
    def __init__(self, id, name,plans):
        # Initialize a new Student object 
        super().__init__(id, name)
        self.plans = plans

class Teacher(Person):
    def __init__(self, name, age, address, teacher_id, subject):
        # Initialize a new Teacher object with a name, age, address, teacher ID, and subject
        super().__init__(name, age, address)
        self.teacher_id = teacher_id
        self.subject = subject
 