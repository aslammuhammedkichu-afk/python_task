import pandas as pd
import numpy as np

df = pd.read_csv("employee_data-1.csv")

print(df.head())
print(df.columns)

# NumPy Performance Analysis

performance = np.array([65, 78, 82, 90, 55, 72, 88, 95])

print("Performance Scores:")
print(performance)


# Access First and Last Values

print("First Score:", performance[0])
print("Last Score:", performance[-1])


# Add Bonus Marks

bonus = 5

performance_bonus = performance + bonus

print("Scores After Bonus:")
print(performance_bonus)


# Statistical Analysis

print("Mean:", np.mean(performance))
print("Median:", np.median(performance))
print("Standard Deviation:", np.std(performance))
print("Highest Score:", np.max(performance))
print("Lowest Score:", np.min(performance))


# Reshape Performance Array

reshaped = performance.reshape(2, 4)

print("Reshaped Array:")
print(reshaped)


# Element-wise Operation

bonus_array = np.array([2, 3, 4, 5, 1, 2, 3, 4])

new_scores = performance + bonus_array

print("Scores After Element-wise Bonus:")
print(new_scores)


# Create Pandas Salary Series

salary = pd.Series(
    [30000, 45000, 55000, 65000, 40000],
    index=["Rahul", "Anu", "Arun", "Meera", "John"]
)

print("Salary Series:")
print(salary)


# Retrieve Specific Employee Salary

print("Arun Salary:", salary["Arun"])


# Increase Salary by 10 Percent

increased_salary = salary * 1.10

print("Salary After 10% Increase:")
print(increased_salary)


# Average Salary

print("Average Salary:", salary.mean())


# Highest Salary

print("Highest Salary:", salary.max())


# Filter Employees Above 50000

high_salary = salary[salary > 50000]

print("Employees Earning Above 50000:")
print(high_salary)


# Load Employee CSV File

df = pd.read_csv("employee_data-1.csv")

print("Employee Dataset:")
print(df)


# Display First Records

print("First Five Records:")
print(df.head())


# Display Column Names

print("Column Names:")
print(df.columns)


# Select Specific Columns

selected_columns = df[["Name", "Department", "Salary"]]

print("Selected Columns:")
print(selected_columns)


# Filter Employees Based on Salary

salary_filter = df[df["Salary"] > 50000]

print("Employees With Salary Above 50000:")
print(salary_filter)


# Filter Employees Based on Department

department_filter = df[df["Department"] == "IT"]

print("IT Department Employees:")
print(department_filter)


# Filter Using Salary and Department

combined_filter = df[
    (df["Salary"] > 50000) &
    (df["Department"] == "IT")
]

print("IT Employees With Salary Above 50000:")
print(combined_filter)


# Create Annual Salary Column

df["Annual_Salary"] = df["Salary"] * 12

print("Dataset With Annual Salary:")
print(df)


# Handle Missing Bonus Values

df["Bonus"] = df["Bonus"].fillna(0)

print("Dataset After Handling Missing Bonus:")
print(df)


# Remove Unnecessary Column

df = df.drop(columns=["Employee_ID"])

print("Dataset After Removing Employee ID:")
print(df)


# Filter High Earning Employees

high_earners = df[df["Annual_Salary"] > 600000]

print("High Earning Employees:")
print(high_earners)


# Create Department Dataset

department_data = pd.DataFrame({
    "Department": ["IT", "HR", "Finance", "Sales"],
    "Manager": ["Rahul", "Anu", "Arun", "Meera"]
})

print("Department Dataset:")
print(department_data)


# Merge Employee and Department Data

final_report = pd.merge(
    df,
    department_data,
    on="Department",
    how="left"
)


# Final Structured Report

print("Final Employee Report:")
print(final_report)