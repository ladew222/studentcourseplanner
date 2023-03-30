class Course:
    def __init__(self):

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
        return [course for course in self.courses if student in course.students]
    
    def get_courses_by_teacher(self, teacher):
        # Get a list of courses that a given teacher is teaching
        return [course for course in self.courses if teacher == course.teacher]
