

# 1. STUDENT MARKS

# marks = [45, 67, 82, 39, 91, 76, 55, 48, 88, 72]

# print("Student Marks:", marks)



 # 2. PASSED STUDENTS USING FOR LOOP


# passed_students = []

# for mark in marks:
#     if mark >= 50:
#         passed_students.append(mark)

# print("Passed Students:", passed_students)



 # 3. PASSED STUDENTS USING LIST COMPREHENSION


# passed_students_comprehension = [
#     mark for mark in marks if mark >= 50
# ]

# print("Passed Students using List Comprehension:",
#       passed_students_comprehension)



 # 4. DISTINCTION STUDENTS


# distinction_students = [
#     mark for mark in marks if mark >= 75
# ]

# print("Distinction Students:", distinction_students)


# 5. SQUARED VALUES OF PASSED MARKS


# squared_passed_marks = [
#     mark ** 2 for mark in passed_students
# ]

# print("Squared Passed Marks:", squared_passed_marks)



 # 6. ADDITION FUNCTION


# def add(a, b):
#     return a + b


# print("Addition:", add(10, 20))



 # 7. AVERAGE FUNCTION


# def calculate_average(marks):
#     return sum(marks) / len(marks)


# average = calculate_average(marks)

# print("Average:", average)



# 8. GRADE FUNCTION


# def assign_grade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 75:
#         return "B"
#     elif mark >= 50:
#         return "C"
#     else:
#         return "Fail"


# print("Grade:", assign_grade(82))



 # 9. POSITIONAL ARGUMENTS


# def student_details(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)


# student_details("Aslam", 22, "Data Analytics")


 # 10. KEYWORD ARGUMENTS


# student_details(
#     name="Aslam",
#     age=22,
#     course="Data Analytics"
# )



# 11. DEFAULT ARGUMENT


# def calculate_discount(price, discount=10):
#     final_price = price - (price * discount / 100)
#     return final_price


# print("Discounted Price:",
#       calculate_discount(1000))



# 12. *args


# def average_args(*marks):
#     return sum(marks) / len(marks)


# print("Average using *args:",
#       average_args(70, 80, 90, 60))


# 13. **kwargs


# def student_profile(**details):
#     for key, value in details.items():
#         print(key, ":", value)


# student_profile(
#     name="Aslam",
#     age=22,
#     course="Data Analytics",
#     city="Kottayam"
# )


 # 14. STUDENT CLASS USING INHERITANCE


# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_personal_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):

#     def __init__(self, name, age, student_id, marks):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.marks = marks

#     def display_student_info(self):
#         self.display_personal_details()
#         print("Student ID:", self.student_id)
#         print("Marks:", self.marks)

#     def has_passed(self):
#         return self.marks >= 50


 # 15. CREATE STUDENT OBJECT


# student1 = Student(
#     "Aslam",
#     22,
#     1001,
#     82
# )

# student1.display_student_info()

# print("Passed:", student1.has_passed())



# Employee Management System

class Employee:

    # Employee details
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    # Display employee details
    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Monthly Salary:", self.salary)

    # Calculate annual salary
    def annual_salary(self):
        return self.salary * 12

    # Check high earner
    def is_high_earner(self):
        return self.salary >= 50000


# Create employee object
employee1 = Employee(101, "Rahul", "IT", 60000)


# Display employee details
employee1.display_details()


# Display annual salary
print("Annual Salary:", employee1.annual_salary())


# Check high earner
print("High Earner:", employee1.is_high_earner())