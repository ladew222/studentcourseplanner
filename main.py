from people import Person, Student, Teacher
from schedule import CourseSchedule
from load_plans import load_student_plans
from Student import load_scheduled_classes
import os
import csv
import time



def main():
    # Load student plans
    file = os.path.join("data", "student_plans.csv")
    student_list = load_student_plans(file)

    # Load scheduled classes
    course_schedule = CourseSchedule()
    file = os.path.join("data", "scheduled_classes.csv")
    all_schedules = load_scheduled_classes(file, course_schedule)

    attendance = get_students_by_course(student_list, all_schedules)
    conflicts = find_conflicting_courses(attendance)
    print("Conflicting courses:")
    print(conflicts)

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


def get_students_by_course(student_list, all_schedules):
    attendance = {}
    for student in student_list:
        for course in all_schedules.courses:
            for plan in student.plans:
                for plannedCourse in plan.plans:
                    if plannedCourse.course.course_id == course.course_id and plannedCourse.year == course.year and plannedCourse.semester == course.semester and plannedCourse.course.timeslot == course.timeslot:
                        if course.course_id not in attendance:
                            attendance[course.course_id] = {}
                        if (course.year, course.semester, course.timeslot) not in attendance[course.course_id]:
                            attendance[course.course_id][(course.year, course.semester, course.timeslot)] = []
                        attendance[course.course_id][(course.year, course.semester, course.timeslot)].append(student)
    return attendance


def find_conflicting_courses(attendance):
    conflicts = {}
    for course_id, course_data in attendance.items():
        for time_key, students in course_data.items():
            if len(students) > 1:
                for student in students:
                    if student.id not in conflicts:
                        conflicts[student.id] = []
                    conflicts[student.id].append((course_id, time_key))
    return conflicts