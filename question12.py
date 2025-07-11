students = {}

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name of student " + str(i + 1) + ": ")
    marks = []
    for j in range(3):
        score = int(input("Enter mark for subject " + str(j + 1) + ": "))
        marks.append(score)
    students[name] = marks

def display_averages(data):
    print("\nAverage marks of each student:")
    for name in data:
        avg = sum(data[name]) / 3
        print(name + ": " + str(avg))

def find_topper(data):
    topper = ""
    highest_avg = -1
    for name in data:
        avg = sum(data[name]) / 3
        if avg > highest_avg:
            highest_avg = avg
            topper = name
    print("\nTopper is:", topper, "with average marks of", highest_avg)

def update_marks(data):
    name = input("\nEnter the name of the student to update marks: ")
    if name in data:
        new_marks = []
        for i in range(3):
            mark = int(input("Enter new mark for subject " + str(i + 1) + ": "))
            new_marks.append(mark)
        data[name] = new_marks
        print("Marks updated for", name)
    else:
        print("Student not found.")

display_averages(students)
find_topper(students)
update_marks(students)

display_averages(students)
find_topper(students)
