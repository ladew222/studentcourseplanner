from people import Person, Student, Teacher
from schedule import CourseSchedule
from load_plans import load_student_plans
from Student import load_scheduled_classes
import os
import csv
import time




def get_course_type(course_id):
    #getting the first four characters from course_id and slotting them into another variable
    course_type = course_id[0:4]
    return course_type

# Get list and number of students in a (not necessarily scheduled) planned class
def get_planned_attendance(student_list, all_schedules):
    plannedAttendance = {}
    for student in student_list:
        for plan in student.plans:
            for plannedCourse in plan.plans:
                if plannedCourse.course_id not in plannedAttendance:
                    plannedAttendance[plannedCourse.course_id] = {}
                if plannedCourse.year not in plannedAttendance[plannedCourse.course_id]:
                    plannedAttendance[plannedCourse.course_id][plannedCourse.year] = {}
                if plannedCourse.semester not in plannedAttendance[plannedCourse.course_id][plannedCourse.year]:
                    plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester] = {}

                if "Student List" not in plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]:
                    plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]["Student List"] = []
                    plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]["Student Count"] = 0
                plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]["Student List"].append(student)
                plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]["Student Count"] += 1
    return plannedAttendance

# Get list and number of students in a scheduled class
def get_scheduled_attendance(plannedAttendance, all_schedules):
    scheduledAttendance = {}
    for plannedCourseId in plannedAttendance:
        for course in all_schedules.courses:
            if plannedCourseId == course.course_id and not (not plannedAttendance[plannedCourseId][course.year]) and not (not plannedAttendance[plannedCourseId][course.year][course.semester]):
                if course.course_id not in scheduledAttendance:
                    scheduledAttendance[course.course_id] = {}
                if course.year not in scheduledAttendance[course.course_id]:
                    scheduledAttendance[course.course_id][course.year] = {}
                if course.semester not in scheduledAttendance[course.course_id][course.year]:
                    scheduledAttendance[course.course_id][course.year][course.semester] = {}

                scheduledAttendance[course.course_id][course.year][course.semester]["Student List"] = plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]["Student List"]
                scheduledAttendance[course.course_id][course.year][course.semester]["Student Count"] = plannedAttendance[plannedCourse.course_id][plannedCourse.year][plannedCourse.semester]["Student Count"]
    return scheduledAttendance



def find_conflicting_courses(student_list, all_schedules):
    conflicts = {}

    for student in student_list:
        matched_scheduled_classes = []
        # Match PlannedCourse objects to their corresponding ScheduledClass objects
        for plan in student.plans:
            for planned_course in plan.plans:
                for scheduled_class in all_schedules.courses:
                    if (planned_course.course_id == scheduled_class.course_id and
                        planned_course.year == scheduled_class.year and
                        planned_course.semester == scheduled_class.semester):
                        matched_scheduled_classes.append(scheduled_class)

        # Check for conflicts in matched ScheduledClass objects
        for i, class1 in enumerate(matched_scheduled_classes):
            for j in range(i + 1, len(matched_scheduled_classes)):
                class2 = matched_scheduled_classes[j]
                if (class1.semester == class2.semester and
                    class1.year == class2.year and
                    class1.timeslot == class2.timeslot):
                    if student.id not in conflicts:
                        conflicts[student.id] = (student, set())
                    conflicts[student.id][1].add((class1, class2))

    return conflicts




# Check for courses planned for in a given year/semester, make sure they are actually offered in the schedule. If not -> add to list 
def find_missing_courses(student_list, all_schedules):
    # Create and populate scheduled_ids in order to compare with planned courses
    scheduled_ids = {}
    for scheduled_course in all_schedules.courses:
        if (scheduled_course.year, scheduled_course.semester) not in scheduled_ids:
            scheduled_ids[(scheduled_course.year, scheduled_course.semester)] = []
        scheduled_ids[(scheduled_course.year, scheduled_course.semester)].append(scheduled_course.course_id)

    missing_courses = {}
    for student in student_list:
        for plan in student.plans:
            for planned_course in plan.plans:
                if planned_course.course_id not in scheduled_ids[(planned_course.year, planned_course.semester)]:
                    if planned_course not in missing_courses:
                        missing_courses.append(planned_course)
    return missing_courses



'''Main function'''
def main():
    # Load student plans
    file = os.path.join("data", "student_plans.csv")
    student_list = load_student_plans(file)

    # Load scheduled classes
    course_schedule = CourseSchedule()
    file = os.path.join("data", "scheduled_classes.csv")
    all_schedules = load_scheduled_classes(file, course_schedule)

    plannedAttendance = get_planned_attendance(student_list, all_schedules)
    scheduledAttendance = get_scheduled_attendance(student_list, all_schedules)

    conflicts = find_conflicting_courses(student_list, all_schedules)
    print("Conflicting courses:")
    print(conflicts)

    # Load list of PlannedCourse objects that are planned but not on the schedule
    missing_courses = find_missing_courses(student_list, all_schedules)


if __name__ == '__main__':
    main()
    


