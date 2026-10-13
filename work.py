#Take input from user
name = input("Enter full name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
employment_status = input("Enter employment status (Employed/Unemployed): ")
stipend = float(input("Enter monthly stipend: "))


# STEP 2: String operations on name
print("\n--- Name Analysis ---")
print("First 3 letters:", name[:3])
print("Uppercase name:", name.upper())


# step 3: tuple
student_details = (name, age, course, employment_status, stipend)

print("\n--- Student Tuple ---")
print(student_details)
print("Data type:", type(student_details))


# STEP 4: List of marks
marks = [85, 90, 75, 90, 60]

print("\n--- Marks List ---")
print("Original marks:", marks)

# Add mark
marks.append(88)
print("After adding mark:", marks)

# Remove mark
marks.remove(75)
print("After removing mark:", marks)

# Sort marks
marks.sort()
print("Sorted marks:", marks)

# Remove duplicates
marks = list(set(marks))
print("After removing duplicates:", marks)


# step 5:
subject_marks = {
    "Math": 85,
    "Science": 90,
    "English": 75
}

print("\n--- Subject Marks ---")
print(subject_marks)

# Update marks
subject_marks["Math"] = 95

# Add new subject
subject_marks["Computer"] = 88

print("Updated subject marks:", subject_marks)
print("Data type:", type(subject_marks))


# step 6:
subjects = frozenset(["Math", "Science", "English"])

print("\n--- Frozenset ---")
print(subjects)
print("Data type:", type(subjects))


# step 7: Set operations 
online_students = {"Aslam", "Rahul", "Aman"}
offline_students = {"Aman", "John", "David"}

print("\n--- Set Operations ---")

# Common students
print("Common students:", online_students & offline_students)

# All students
print("All students:", online_students | offline_students)

# Only online students
print("Only online students:", online_students - offline_students)


# STEP 8: Calculate average and grade
average = sum(marks) / len(marks)

print("\n--- Result ---")
print(f"Average Marks: {average:.2f}")

# Grade calculation
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")


# STEP 9: Final formatted output
print("--- Final Student Profile ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Employment Status: {employment_status}")
print(f"Stipend: ₹{stipend}")