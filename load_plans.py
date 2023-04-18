import os
import csv
from typing import List
from people import Person, Student, Teacher
from schedule import Course,PlannedCourse
from plans import StudentPlan

def load_student_plans(csv_path: str) -> List[Student]:
    students = {}
    courses = {}
    planed_courses = {}

    with open(csv_path, "r") as file:
        readCSV = csv.DictReader(file)
        
        for row in readCSV:
            student_id = int(row['student_id'])
            year = int(row['year'])
            semester = row['semester']
            course_id = row['course']
            
            if student_id not in students:
                students[student_id] = Student(student_id, f"Student {student_id}", [])
            
            if course_id not in courses:
                courses[course_id] = Course(course_id, f"Course {course_id}")
            
            PlannedCourse_id = course_id + str(year) + semester
            if PlannedCourse_id not in planed_courses:
                planed_courses[PlannedCourse_id] = PlannedCourse(courses[course_id], year, semester)
            
            plan = StudentPlan(students[student_id])
            students[student_id].add_plan(plan)

    return list(students.values())
