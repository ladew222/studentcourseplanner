import csv
from typing import Dict
from schedule import Course, ScheduledClass, CourseSchedule, Time, TimeSlot
from people import Teacher, Student

def load_scheduled_classes(csv_path: str, course_schedule: CourseSchedule):
    instructors = {}
    courses = {}

    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            sec_name, title, sec_mthd, wks, sec_start, credits, days, time_start, time_end, room, instructor_id, capacity, semester, year = row
            
            # Create Instructor object if not already exists
            instructor_id = instructor_id
            if instructor_id not in instructors:
                instructors[instructor_id] = Teacher(instructor_id, f"Instructor {instructor_id}")
            
            # Create Course object if not already exists
            course_id = sec_name.split('-')[0]
            if course_id not in courses:
                courses[course_id] = Course(course_id, title)
            
            # Create Time and TimeSlot objects
            time = Time(time_start, time_end)
            timeslot = TimeSlot(days, time)
            
            # Create CourseClass object and add it to CourseSchedule
            section=1
            course_class = ScheduledClass(time, instructors[instructor_id], timeslot, int(capacity), int(year),section, semester)
            course_schedule.add_course(course_class)
    return course_schedule
