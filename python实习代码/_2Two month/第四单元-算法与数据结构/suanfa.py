# for x in range(1001):
#     for y in range(1001):
#         for z in range(1001):
#             if (x+y+z==1000) and x**2+y**2==z**2:
#                 print(x,y,z)

# 执行时间会有很久

# import time
# print(time.time())
#
# for x in range(1001):
#     for y in range(1001):
#         c=1000-x-y
#         if x**2+y**2==c**2:
#             print(x,y,c)

# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

