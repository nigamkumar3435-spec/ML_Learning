#python code to create dictionary

emp={
    'EmpName' : ['Nigam','Aakash','Anand','Krishna','Priya','Aakash'],
    'DeptName': ['CSE','IT','IOT','AIML','CSE','Mechanical'],
    'Salary'  : [51000,12000,8000,35000,45000,23000]
}
print(emp)
print(emp['EmpName'])
# for i in emp['EmpName']:
#     # print(i)
# print(emp.keys())
# print(emp.values())
# print(emp.items())

#a.To print name and deptname of employee who get maximum salary.

# maxsal=max(emp['Salary'])
# print(maxsal)
# for i in emp['Salary']:
#   if i==maxsal:
#     name=emp['EmpName'][emp['Salary'].index(i)]
#     dept=emp['DeptName'][emp['Salary'].index(i)]
# print(name,dept)

#b.To print name of employee who work in CSE dept.

for i in emp['DeptName']:
  if i=='CSE':
    name=emp['EmpName'][emp['DeptName'].index(i)]
    print(name)
