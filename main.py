from people import Person, Student, Teacher
from schedule import CourseSchedule
from load_plans import load_student_plans
import os
import csv
import time
def main():
    # Load student plans
    file = os.path.join("data","student_plans.csv")
    student_list = load_student_plans(file)
    
    # Load scheduled classes
 ##   course_schedule = CourseSchedule()
 ##   file = os.path.join("studentcourseplanner", "data", "scheduled_classes.csv")
 ##   load_scheduled_classes(file, course_schedule)

        
if __name__ == '__main__':
    main()