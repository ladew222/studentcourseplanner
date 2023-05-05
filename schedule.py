from datetime import datetime
from plans import StudentPlan

class Course:
    def __init__(self, course_id, course_name):
        # Initialize a new Course with a name and id.
        # Variables for course are named as course_name and course_id.
        self.course_name = course_name
        self.course_id = course_id
        
class PlannedCourse(Course):
    def __init__(self,course, year, semester):
        # Initialize a new planned course object with a name, id, year and semester.
        # This object inherits the name and id from our course class.
        super().__init__(course.course_id, course.course_name)
        self.year = year
        self.semester = semester
    
class ScheduledClass(Course):
    def __init__(self, course, time, instructor, timeslot, capacity, year, section, semester):
        # Initialize a new scheduled class object with a time, instructor, timeslot, capacity, year, section and semester.
        super().__init__(course.course_id, course.course_name)
        self.time = time
        self.instructor = instructor
        self.timeslot = timeslot
        self.capacity = capacity
        self.year = year
        self.section = section
        self.semester = semester

class CourseSchedule:
    def __init__(self):
        # Initialize an empty list to store courses in the schedule
        self.courses = []
    
    def add_course(self, course):
        # Add a course to the schedule
        self.courses.append(course)
    
    def remove_course(self, course):
        # Remove a course from the schedule
        if course in self.courses:
            self.courses.remove(course)
    
    def get_courses_by_student(self, student):
        # Get a list of courses that a given student is enrolled in
        return[course for course in self.courses if student in course.students]

    def get_courses_by_teacher(self, teacher):
        # Get a list of courses that a given teacher is teaching
        return [course for course in self.courses if teacher == course.teacher]
    
    def check_schedule(self, StudentPlan):
        if self.courses != StudentPlan.plans:
            current_plan = StudentPlan.plans[0]
            for PlannedCourse in current_plan:
                for current_plan in self.courses:
                    if current_plan.course_id == PlannedCourse.course_id:
                        return True
        print("A discrepency was detected between a planned course and the schedule.")
        return False
    #Implement a function to assess whether a student's planned class is not on the schedule and give an alert
    
class Time:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time
    def __eq__(self, other):
        if isinstance(other, Time):
            return self.start_time == other.start_time and self.end_time == other.end_time
        return False

class TimeSlot:
    def __init__(self, days: str, time: Time):
        self.days = days
        self.time = time
        
    def __eq__(self, other):
        if isinstance(other, TimeSlot):
            return self.days == other.days and self.time == other.time
        return False

