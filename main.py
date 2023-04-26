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

    # Loop through every student then course in schedule, store students that plan to take it in attendance
    attendance = {}
    for student in student_list:
        for course in course_schedule.courses:
            if attendance[course.course_id] == None:
                attendance[course.course_id] = {}
            attendance[course.course_id][course.year, course.semester, course.timeslot] = get_students_by_course(self, student, course)

def get_students_by_course(self, student, course):
    studentsList = []
    for plan in student.plans:
        for plannedCourse in plan.plannedCourses:
            if plannedCourse.course_id == course.course_id and plannedCourse.year == course.year and plannedCourse.semester == course.semester and plannedCourse.timeslot == course.timeslot:
                studentsList.append(student)
    return studentsList

if __name__ == '__main__':
    main()
    
def get_course_type(course_id):
    #getting the first four characters from course_id and slotting them into another variable
    course_type = course_id[0:4]
    return course_type