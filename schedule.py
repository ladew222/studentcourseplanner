class Course:
    def __init__(self, course_name, course_id):
        # Initialize a new Couse with a name and id.
        # Variables for course are named as course_name and course_id.
        self.course_name = course_name
        self.course_id = course_id
        
class planned_course:
    def __init__(self,course_name, course_id, year, semester):
        # Initialize a new planned course object with a name, id, year and semester.
        # This object inherits the name and id from our course class.
        super().__init__(course_name, course_id)
        self.year = year
        self.semester = semester
    
class scheduled_class:
    def __init__():

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
