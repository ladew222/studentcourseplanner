from people import Student

class StudentPlan:
    def __init__(self,Student):
        # Initialize a new Person object 
        self.plans = []
        self.student = Student
    def add_planned_class(self, planned_class):
        # Add a planned class to the student's plan
        self.plans.append(planned_class)

        
    