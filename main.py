from people import Person, Student, Teacher

def main():
    # Create instances of the classes
    p = Person("John", 30, "123 Main St.")
    s = Student("Jane", 20, "456 Maple Ave.", "S1234", ["Math", "Science"])
    t = Teacher("Dr. Smith", 45, "789 Oak St.", "T5678", "English")

    # Print out the attributes of the instances
    print("Person:", p.name, p.age, p.address)
    print("Student:", s.name, s.age, s.address, s.student_id, s.courses)
    print("Teacher:", t.name, t.age, t.address, t.teacher_id, t.subject)

if __name__ == '__main__':
    main()
