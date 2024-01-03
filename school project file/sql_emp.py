import mysql.connector as msconn
import tabulate

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'idris7', database = 'schoolproject')
mycur = sqlcon.cursor()

def add():
    empno = int(input('enter emp no: '))
    empname = input('enter employee name: ')
    des = input('enter designation: ')
    dept = input('enter department: ')
    sal = int(input('enter salary: '))
    mycur.execute(f'insert into employee values({empno},"{empname}","{des}","{dept}",{sal})')
    sqlcon.commit()
    print('\nemployee added to the table successfully')

def display():
    mycur.execute('select * from employee')
    rec = mycur.fetchall()
    print('\n',tabulate.tabulate(rec,headers = ['Emp_no','Emp_name','Designation','Department','Salary']))

def search():
    mycur.execute(f'select * from employee where emp_no = {int(input("enter emp no to search: "))}')
    print('\n',tabulate.tabulate(mycur.fetchall(),headers = ['Emp_no','Emp_name','Designation','Department','Salary']))

def delete():
    try:mycur.execute(f'delete from employee where emp_no = {int(input('enter emp no to delete: '))}');sqlcon.commit()
    except:print('employee not found')

def modify():
    empno = int(input('enter emp no to modify: '))
    empname = input('enter modified employee name: ')
    des = input('enter modified designation: ')
    dept = input('enter modified department: ')
    sal = int(input('enter modified salary: '))
    mycur.execute(f'update employee set emp_name="{empname}",designation="{des}",department="{dept}",salary={sal} where emp_no = {empno}')
    sqlcon.commit()

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Add employee
    2. Display all employees  
    3. Delete an employee from the table
    4. Search for an employee 
    5. modify details of an employee
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:add()
    elif ch == 2:display()
    elif ch == 3:delete()
    elif ch == 4:search()
    elif ch == 5:modify()
    else:print('please enter a valid choice\n')
