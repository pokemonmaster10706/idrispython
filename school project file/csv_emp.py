import csv,tabulate

def csv_input():
    with open('csvfile.csv','a',newline = '') as csvf:
        mywriter = csv.writer(csvf)
        while True:
            mywriter.writerow([input('Enter Emp_no: '),input('Enter Employee name: '),input('Enter Job: '),input('enter Department: '),input('Enter salary: ')])
            if input('Do you want to add more?: ') != 'y':break

def display():
    with open('csvfile.csv','r') as csvf:
        myreader = csv.reader(csvf)
        print(tabulate.tabulate(myreader,headers=['Emp_no','Emp_Name','Job','Department','salary'],tablefmt = 'mixed_grid'))

def search():
    with open('csvfile.csv','r') as csvf:
        myreader = csv.reader(csvf)
        empno = input('Enter Emp number to search: ')
        for i in myreader:
            if i[0] == empno:
                print(tabulate.tabulate([i],headers=['Emp_no','Emp_Name','Job','Department','salary'],tablefmt = 'mixed_grid'))
                break
            else:pass
        else:print('Employee doesent exist.')

def modify():
    with open('csvfile.csv','r') as csvf:
        myreader = csv.reader(csvf)
        empno = input('Enter Emp number to modify: ')
        lrec = []
        for i in myreader:lrec.append(i)
        for i in range(len(lrec)):
            if lrec[i][0] == empno:
                del lrec[i]
                lrec.append([empno,input('Enter modified emp name: '),input('enter modified job: '),input('enter modified department: '),input('modified salary: ')])
                break
        else:print('Employee doesent exist.')
        with open('csvfile.csv','w',newline = '') as csvf2:
            mywriter = csv.writer(csvf2)
            mywriter.writerows(lrec)

def delete():
    with open('csvfile.csv','r') as csvf:
        myreader = csv.reader(csvf)
        empno = input('Enter Emp number to delete: ')
        lrec = []
        for i in myreader:lrec.append(i)
        for i in range(len(lrec)):
            if lrec[i][0] == empno:del lrec[i];break
        else:print('Employee doesent exist.')
        with open('csvfile.csv','w',newline = '') as csvf2:
            mywriter = csv.writer(csvf2)
            mywriter.writerows(lrec)

def count():
    with open('csvfile.csv','r') as csvf:
        myreader = csv.reader(csvf)
        lrec = []
        for i in myreader:lrec.append(i)
        print(f'total number of records is {len(lrec)}')

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Write data to the file 
    2. Display all records from the file 
    3. Search for a particular employee using employee number 
    4. Modify a record 
    5. Delete a record 
    6. Display total records in the file
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:csv_input()
    elif ch == 2:display()
    elif ch == 3:search()
    elif ch == 4:modify()
    elif ch == 5:delete()
    elif ch == 6:count()
    else:print('please enter a valid choice\n')
