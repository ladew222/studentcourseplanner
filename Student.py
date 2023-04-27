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

#I wanted to get a sorting algorithm in, even if it isn't the best.
def SwapStartTime(courses, i ,j):
    temp = courses.start_time[i]
    courses.start_time[i] = courses.start_time[j]
    courses.start_time[j] = temp

#Sorting classes by start time
def SelectionSortStartTime(courses):
    i = 0
    while i <len(courses) - 1:
        SmallestIndex = 1
        j + i + 1
        while j < len(courses):
                if courses.start_time[j] < courses.start_time[SmallestIndex]:
                    SmallestIndex = j
                j += 1
        if SmallestIndex != i:
            SwapStartTime(courses, SmallestIndex, i)
        i += 1 

def check_conflicts(self, course):
    conflicts = {course}
    if CourseSchedule.courses.start_time[0] or CourseSchedule.courses.end_time[0]:
        self.conflicts.append(conflicts)
        #I can't do == because a class could be from 10 to 11 and another could be from 10:30 to 11:30.
        #If I could subtract with base 60 and create a duration/interval variable that takes into acct each time within the start and end...
        #Does python even recoginize time?
        #
    #Implement a function to check if there are any conflicts between
    #classes that students have scheduled based on the times for the classes from the schedule.