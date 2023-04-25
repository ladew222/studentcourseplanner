# Import necessary libraries and modules
import csv
from typing import Dict
from schedule import Course, ScheduledClass, CourseSchedule, Time, TimeSlot
from people import Teacher, Student

# Define a function to load scheduled classes from a CSV file
def load_scheduled_classes(csv_path: str, course_schedule: CourseSchedule):
    # Initialize dictionaries to store instructors and courses
    instructors = {}
    courses = {}

    # Open the CSV file for reading
    with open(csv_path, "r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Read and discard the header row
        header = next(reader)
        
        # Loop through the remaining rows in the CSV file
        for row in reader:
            # Unpack the row into individual variables
            sec_name, title, sec_mthd, wks, sec_start, credits, days, time_start, time_end, room, instructor_id, capacity, semester, year = row
            
            # Check if the instructor already exists in the instructors dictionary
            # If not, create a new Teacher object and add it to the dictionary
            if instructor_id not in instructors:
                instructors[instructor_id] = Teacher(instructor_id, f"Instructor {instructor_id}")
            
            # Check if the course already exists in the courses dictionary
            # If not, create a new Course object and add it to the dictionary
            course_id = sec_name.split('-')[0]
            if course_id not in courses:
                courses[course_id] = Course(course_id, title)
            
            # Create Time and TimeSlot objects using the start and end times and days
            time = Time(time_start, time_end)
            timeslot = TimeSlot(days, time)
            
            # Create a ScheduledClass object with the necessary information
            section = 1
            course_class = ScheduledClass(time, instructors[instructor_id], timeslot, int(capacity), int(year), section, semester)
            
            # Add the ScheduledClass object to the CourseSchedule
            course_schedule.add_course(course_class)
    
    # Return the updated CourseSchedule object
    return course_schedule

def check_conflicts(self):
    conflicts = {}
    if CourseSchedule.courses.timeslot[0]:
        #I have to sort the classes by timeslot.
        self.conflicts.append(courses)
    #Implement a function to check if there are any conflicts between
    #classes that students have scheduled based on the times for the classes from the schedule.