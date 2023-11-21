from Model import Employee, Job, Assignment, Project
from db import session, engine
import datetime
from sqlalchemy import text
from datetime import datetime


'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''
# employees = session.query(Employee).first()
# print(employees.emp_lname)


# employees = session.query(Employee).filter(Employee.emp_num > 101).all()
# for employee in employees:
#     print(employee.emp_lname, employee.emp_fname, employee.emp_hiredate)


'''
Join employee with job
'''
# employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).all()
# for employee in employees:
#     print(employee.Employee.emp_lname, employee.Employee.emp_fname, employee.Job.job_description)

'''
Insert new employee record
'''
# employee = Employee(emp_num=999, emp_lname="Doe", emp_fname="John", emp_initial="D", emp_hiredate="2020-01-01")
# session.add(employee)
# session.commit()

'''
Update employee record

'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# employee.job_code = 510
# session.commit()

'''
Delete employee record
'''
# employee = session.query(Employee).filter(Employee.emp_num == 999).first()
# session.delete(employee)
# session.commit()

'''
Query assigment where assign_date is larger than 2010-01-01
'''

# import psycopg2
# from datetime import date

# # Connect to the database
# conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")

# # Create a cursor
# cursor = conn.cursor()

# # Define the values for the new employee record
# id = 168
# firstname = 'John'
# lastname = 'Doe'
# initials = 'JD'
# job = 'Programmer'
# hire_date = date.today()

# # Execute the SQL query
# query = f"INSERT INTO employee (id, firstname, lastname, initials, job, hire_date) VALUES ({id}, '{firstname}', '{lastname}', '{initials}', '{job}', '{hire_date}')"
# cursor.execute(query)

# # Commit the changes to the database
# conn.commit()

# # Close the cursor and the connection
# cursor.close()
# conn.close()

# today = datetime.now()

# employee = Employee(emp_num=168, emp_lname="Doe", emp_fname="John", emp_initial="D", job_code=500, emp_hiredate=today)
# session.add(employee)
# session.commit()


# employees = session.query(Employee, Job).filter(Employee.job_code == Job.job_code).filter(Employee.emp_num == 168).all()

# for employee in employees:
#     print(employee.Employee.emp_num, employee.Employee.emp_lname,
#         employee.Employee.emp_fname, employee.Employee.emp_initial,
#         employee.Employee.emp_hired)

# target_job = session.query(Job).filter(Job.job_description == 'Database Designer').first()
# print(target_job.job_code)

# employee = session.query(Employee).filter(Employee.emp_num == 168).first()
# employee.job_code = target_job.job_code
# session.commit()

# target_job = session.query(Job).filter(Job.job_description == 'Programmer').first()
# print(target_job.job_code)

# projects = session.query(Project, Employee).filter(Project.emp_num == Employee.emp_num).filter(Employee.job_code == target_job.job_code).all()
# for project in projects:
#     print(project.Project.proj_num, project.Project.proj_name, project.Employee.emp_fname, project.Employee.emp_lname)

# employee = session.query(Employee).filter(Employee.emp_num == 168).first()
# session.delete(employee)
# session.commit()

