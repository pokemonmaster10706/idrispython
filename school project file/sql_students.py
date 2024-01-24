import mysql.connector as msconn
import tabulate

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'idris7', database = 'schoolproject')
mycur = sqlcon.cursor()

def add():
    sid = int(input('enter student id: '))
    sname = input('enter student name: ')
    age = int(input('enter age: '))
    date_of_birth = input('enter date of birth (yyyy/mm/dd): ')
    grd = input('enter class and section: ')
    clsteach = input('enter class teacher name: ')
    mycur.execute(f'insert into students values({sid},"{sname}",{age},"{date_of_birth}","{grd}","{clsteach}")')
    sqlcon.commit()
    print('\nstudent added successfully')

def display():
    mycur.execute('select * from students')
    rec = mycur.fetchall()
    print('\n',tabulate.tabulate(rec,headers = ['S_ID','S_NAME','AGE','DOB','CLASS','CLASS TEACHER']))

def delete():
    mycur.execute(f'delete from students where s_id = {int(input("enter student id to delete: "))}');sqlcon.commit()

def grade_count():
    grade = input("enter grade to count: ")
    mycur.execute(f'select * from students where grade = "{grade}"')
    rec = mycur.fetchall()
    print(f'number of students in grade {grade} is {len(rec)} ')
    print('\n',tabulate.tabulate(rec,headers = ['S_ID','S_NAME','AGE','DOB','CLASS','CLASS TEACHER']))

def modify():
    sid = int(input('enter student id to search: '))
    sname = input('enter modified student name: ')
    age = int(input('enter modified age: '))
    date_of_birth = input('enter modified date of birth (yyyy/mm/dd): ')
    grd = input('enter modified class and section: ')
    clsteach = input('enter modified class teacher name: ')
    mycur.execute(f'update students set s_name="{sname}",age={age},dob="{date_of_birth}",grade="{grd}",class_teacher="{clsteach}" where s_id={sid}')
    sqlcon.commit()
    print('\nstudent added successfully')

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Add student
    2. Display all students  
    3. remove a student
    4. Count and display number of students in a particular grade 
    5. modify student details
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:add()
    elif ch == 2:display()
    elif ch == 3:delete()
    elif ch == 4:grade_count()
    elif ch == 5:modify()
    else:print('please enter a valid choice\n')
