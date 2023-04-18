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
    def add_plan(self, plan):
        self.plans.append(plan)

class Teacher(Person):
    def __init__(self, teacher_id, name):
        # Initialize a new Teacher object with a name, age, address, teacher ID, and subject
        super().__init__(id,name)
        self.teacher_id = teacher_id
 