import csv
#put import csv at top of document
#make ScheduledClass class
with open("scheduled_classes.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        #Time, Instructor, Timeslot, Capacity, Year, Section, Semester
        row[0] = ScheduledClass(Time, Instructor, Timeslot, row[11], row[13], Section, row[12])
        CourseSchedule.add_course(row[0])