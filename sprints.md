Sprint 1:

Create a UML diagram for the application.
Design the Plan class with its attributes and methods, including the check_conflicts() method.
Design the Student class that inherits from the Person class, with attributes such as name and id.
Design the Instructor class that also inherits from the Person class and has a get_classes() method.
Design the Courses class with its attributes, including the id and name.
Create a new file for the UML diagram and class structures.
Sprint 2:

Implement the loading of the student plans and people from CSV files.
Implement the loading of the courses from the course schedule file.
Implement the planned_course class with its semester and year variables.
Implement the scheduled_class class with attributes such as time, instructor, timeslot, capacity, year, section, and semester variables.
Implement the Course_schedule class with its list of scheduled_class objects, and add_class(), check_schedule(), and check_missing() methods.
Sprint 3:

Implement a function to grab all prefixes from the file such that CSCI-160 is CSCI.
Implement a function to assess whether a student's planned class is not on the schedule and give an alert.
Implement a function to check if there are any conflicts between classes that students have scheduled based on the times for the classes from the schedule.
Test the code for these functionalities and make necessary changes.
Sprint 4:

Implement a function to create a list of students that plan to take a given class in the schedule.
Implement a function to identify students who have planned a class that is not on the schedule and give the prefixes that exist in the schedule.
Implement a function to identify any students that have scheduled classes that conflict with one another based on this schedule.
Test the code for these functionalities and make necessary changes.
Sprint 5:

Create a main function to orchestrate the flow of the code.
Implement the planned sequence for the code, which is to load the plans and people from CSV files, load the courses from the course schedule file, check for class conflicts, check for missing classes, and assess attendance, then display results.
Test the entire code with different scenarios and make necessary changes.