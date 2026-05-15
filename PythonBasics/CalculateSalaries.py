import numpy as np
# Step 1: Create a NumPy array representing the monthly salaries of 6 employees.
# The rows represent employees, and the columns represent the months (January, February, March, April)
salaries = np.array([[4500, 4700, 4900, 5000], # Employee 0
                     [5500, 5600, 5800, 5900], # Employee 1
                     [4700, 4800, 6900, 5100], # Employee 2
                     [4000, 6200, 4300, 4500], # Employee 3
                     [6000, 4200, 4300, 5500], # Employee 4
                     [5200, 5300, 5400, 5600]])# Employee 5

total_salaries = np.sum(salaries, axis=1) # Sum across rows (employees)
print("Total salary earned by each employee:", total_salaries)

average_salaries = np.mean(salaries, axis=0) # Mean across columns (months)
print("Average salary earned by each employee:", average_salaries)

max_salaries = np.max(salaries, axis=1) # Max across rows (employees)
print("Maximum salary earned by each employee:", max_salaries)

min_salaries = np.min(salaries, axis=1) # Min across rows (employees)
print("Minimum salary earned by each employee:", min_salaries)

highest_salary_in_jan = np.argmax(salaries[:, 0]) # Find max salary in January(column 0)
highest_salary_in_feb = np.argmax(salaries[:, 1]) # Find max salary in February(column 1)
highest_salary_in_mar = np.argmax(salaries[:, 2]) # Find max salary in March(column 2)
highest_salary_in_apr = np.argmax(salaries[:, 3]) # Find max salary in April (column3)

print(f"Employee with highest salary in January: Employee {highest_salary_in_jan }")
print(f"Employee with highest salary in February:Employee {highest_salary_in_feb}")
print(f"Employee with highest salary in March: Employee {highest_salary_in_mar}")
print(f"Employee with highest salary in April: Employee {highest_salary_in_apr}")

# Step 5: Identify employees who earned above 5000 in all months.
# We create a boolean array where True means the employee earned more than 5000 in all months.
employees_above_5000 = np.all(salaries > 5000, axis=1) # Check if all salary values for an employee are > 5000
num_employees_above_5000 = np.sum(employees_above_5000) # Count the number of True values
print(f"Number of employees who earned above 5000 in all months:{num_employees_above_5000}")

# Step 6: Determine the month with the highest average salary across all employees.
month_with_highest_avg_salary = np.argmax(average_salaries) # Find the month with max avg salary
#print(&quot;Month with highest average salary across all employees:&quot;month_with_highest_avg_salary)
months = ["January", "February", "March"," April"]

print(f"The month with the highest average salary is:{months[month_with_highest_avg_salary]}")
