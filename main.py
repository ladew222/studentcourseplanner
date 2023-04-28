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
    conflicts = find_conflicting_courses(student_list, all_schedules)
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


def find_conflicting_courses(student_list, all_schedules):
    conflicts = {}

    for student in student_list:
        for planned_course in student.plans:
            for scheduled_class in all_schedules.courses:
                if (planned_course.course.course_id == scheduled_class.course.course_id and
                    planned_course.year == scheduled_class.year and
                    planned_course.semester == scheduled_class.semester and
                    planned_course.course.timeslot == scheduled_class.timeslot):
                    if student.id not in conflicts:
                        conflicts[student.id] = set()
                    conflicts[student.id].add((planned_course, scheduled_class))

    return conflicts

def find_conflicting_courses_v2(student_list, all_schedules):
    conflicts = {}
    scheduled_classes_set = set(all_schedules.courses)

    for student in student_list:
        planned_classes_set = set()
        for plan in student.plans:
            for planned_course in plan.plans:
                scheduled_class = ScheduledClass(
                    planned_course.course,
                    None,  # Instructor not needed for the comparison
                    TimeSlot(planned_course.course.timeslot.days, planned_course.course.timeslot.time),
                    0,  # Capacity not needed for the comparison
                    planned_course.year,
                    0,  # Section not needed for the comparison
                    planned_course.semester
                )
                planned_classes_set.add(scheduled_class)

        intersection = planned_classes_set.intersection(scheduled_classes_set)

        if intersection:
            conflicts[student.id] = intersection

    return conflicts

