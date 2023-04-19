# Import necessary libraries and modules
import os
import csv
from typing import List
from people import Person, Student, Teacher
from schedule import Course, PlannedCourse
from plans import StudentPlan

# Define a function to load student plans from a CSV file
def load_student_plans(csv_path: str) -> List[Student]:
    # Initialize dictionaries to store student plans, courses, and students
    student_plans = {}
    courses = {}
    students = {}

    # Open the CSV file for reading
    with open(csv_path, "r") as file:
        # Create a CSV DictReader object
        readCSV = csv.DictReader(file)
        
        # Loop through the rows in the CSV file
        for row in readCSV:
            # Get student_id, year, semester, and course_id from the row
            student_id = int(row['student_id'])
            year = int(row['year'])
            semester = row['semester']
            course_id = row['course']
            
            # Check if the student already exists in the student_plans dictionary
            # If not, create a new Student object with an associated StudentPlan and add it to the dictionaries
            if student_id not in student_plans:
                student = Student(student_id, f"Student {student_id}", [])
                student.add_plan(StudentPlan(student))
                student_plans[student_id] = student
                students[student_id] = student

            # Check if the course already exists in the courses dictionary
            # If not, create a new Course object and add it to the dictionary
            if course_id not in courses:
                courses[course_id] = Course(course_id, f"Course {course_id}")
            
            # Create a PlannedCourse object with the course, year, and semester
            planned_class = PlannedCourse(courses[course_id], year, semester)

            # Add the planned class to the student's plan
            student_plans[student_id].plans[0].add_planned_class(planned_class)

    # Return a list of Student objects
    return [s for s in students.values()]
