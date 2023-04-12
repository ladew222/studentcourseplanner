from people import Person, Student, Teacher
from schedule import CourseSchedule, Time, Timeslot
def main():
    # Create instances of the classes
    p = Person("John", 30, "123 Main St.")
    s = Student("Jane", 20, "456 Maple Ave.", "S1234", ["Math", "Science"])
    t = Teacher("Dr. Smith", 45, "789 Oak St.", "T5678", "English")
    # Create instances of Time, Instructor, and Timeslot
    time1 = Time("9:00am", "10:30am")
    timeslot1 = Timeslot("Monday", "9:00am - 10:30am")

    # Print out the attributes of the instances
    print("Person:", p.name, p.age, p.address)
    print("Student:", s.name, s.age, s.address, s.student_id, s.courses)
    print("Teacher:", t.name, t.age, t.address, t.teacher_id, t.subject)

if __name__ == '__main__':
    main()
