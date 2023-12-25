import pickle,tabulate

def add():
    with open('binarystudents.bat','ab') as bf:
        roll = int(input('enter student roll number : '))
        name = input('enter student name : ')
        gradiv = input('enter grade and division : ')
        pickle.dump([roll,name,gradiv],bf)

def search():
    with open('binarystudents.bat','rb') as bf:
        lrec=[]
        while True:
              try:lrec.append(pickle.load(bf))
              except:break
        roll = int(input('Enter roll number to search: '))
        for i in lrec:
            if i[0] == roll:
                print(f'the student was found \n{tabulate.tabulate([i],headers = ["roll","name","division"],tablefmt="pretty")}')
                break
        else:print('student not in database')

def display():
    with open('binarystudents.bat','rb') as bf:
        lrec=[]
        while True:
            try:lrec.append(pickle.load(bf))
            except:break
        print(tabulate.tabulate(lrec,headers = ["roll","name","division"],tablefmt = 'pretty'))

def modify():
    with open('binarystudents.bat','rb') as bf:
        lrec=[]
        while True:
              try:lrec.append(pickle.load(bf))
              except:break
        roll = int(input('Enter roll number to search: '))
        for i in lrec:
            if i[0] == roll:
                del lrec[lrec.index(i)]
                lrec.append([roll,input('new name: '),input('new class: ')])
                break
        else:print('student not in database')
    with open('binarystudents.bat','wb') as bf:
        for i in lrec:pickle.dump(i,bf)

def delete():
    with open('binarystudents.bat','rb') as bf:
        lrec=[]
        while True:
              try:lrec.append(pickle.load(bf))
              except:break
        roll = int(input('Enter roll number to delete: '))
        for i in lrec:
            if i[0] == roll:del lrec[lrec.index(i)];break
        else:print('student not in database')
    with open('binarystudents.bat','wb') as bf:
        for i in lrec:pickle.dump(i,bf)

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Search for a student using his roll number 
    2. Display all students in the file 
    3. Modify the details of a students 
    4. Delete a student from the file 
    5. Add a student
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:search()
    elif ch == 2:display()
    elif ch == 3:modify()
    elif ch == 4:delete()
    elif ch == 5:add()
    else:print('please enter a valid choice\n')