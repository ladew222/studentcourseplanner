from people import Person, Student, Teacher
from schedule import CourseSchedule
from load_plans import load_student_plans
from Student import load_scheduled_classes
import os
import csv
import time
def main():
    course_schedule = CourseSchedule()
    # Load student plans
    file = os.path.join("data","student_plans.csv")
    student_list = load_student_plans(file)
    
    # Load scheduled classes
    course_schedule = CourseSchedule()
    file = os.path.join( "data", "scheduled_classes.csv")
    all_schedules = load_scheduled_classes(file, course_schedule)
    print("Course Schedule")

        
if __name__ == '__main__':
    main()