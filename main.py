from people import Person, Student, Teacher
from schedule import CourseSchedule
import os
import csv
def main():
    # Create instances of the classes
    p = Person("John", 30, "123 Main St.")
    s = Student("Jane", 20, "456 Maple Ave.", "S1234", ["Math", "Science"])
    t = Teacher("Dr. Smith", 45, "789 Oak St.", "T5678", "English")
    # Create instances of Time, Instructor, and Timeslot
    time1 = Time("9:00am", "10:30am")
    timeslot1 = Timeslot("Monday", "9:00am - 10:30am")

    # Print out the attributes of the instances
    print("Person:", p.name, p.age, p.address)
    print("Student:", s.name, s.age, s.address, s.student_id, s.courses)
    print("Teacher:", t.name, t.age, t.address, t.teacher_id, t.subject)

if __name__ == '__main__':
    main()

student_plans = []
file = os.path.join("studentcourseplanner\data", "student_plans.csv")
with open(file, "r") as file:
    readCSV = csv.DictReader(file)
    next(readCSV)
    # assigns each row to a variable
    for row in readCSV:
        student_id = int(row['student_id'])
        year = int(row['year'])
        semester = row['semester']
        course = row['course']
        
        # creates a dictionary
        plans = {'year': year,'semester': semester, 'course': course}
        index = None
        for i, plan in enumerate(student_plans):
            if plan['student_id'] == student_id:
                index = i
                break
        if index is not None:
            student_plans[index]['student_plan'].append(plans)
        else:
            new_student = {'student_id': student_id, 'student_plan': [plans]}
            student_plans.append(new_student)
print(student_plans) 