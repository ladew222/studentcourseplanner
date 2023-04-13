from people import Person, Student, Teacher
from schedule import CourseSchedule
import os
import csv
import time
def main():
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
        
if __name__ == '__main__':
    main()