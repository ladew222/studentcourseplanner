import os
import csv
from typing import List
from people import Person, Student, Teacher
from schedule import Course,PlannedCourse
from plans import StudentPlan

import os
import csv
from typing import List
from people import Person, Student, Teacher
from schedule import Course, PlannedCourse
from plans import StudentPlan

def load_student_plans(csv_path: str) -> List[Student]:
    student_plans = {}
    courses = {}
    students = {}

    with open(csv_path, "r") as file:
        readCSV = csv.DictReader(file)
        
        for row in readCSV:
            student_id = int(row['student_id'])
            year = int(row['year'])
            semester = row['semester']
            course_id = row['course']
            
            if student_id not in student_plans:
                student = Student(student_id, f"Student {student_id}",[])
                student.add_plan(StudentPlan(student))
                student_plans[student_id] = student

            if course_id not in courses:
                courses[course_id] = Course(course_id, f"Course {course_id}")
            
            planned_class = PlannedCourse(courses[course_id], year, semester)

            # Add the planned class to the student's plan
            student_plans[student_id].plans[0].add_planned_class(planned_class)

    return [s for s in students.values()]
