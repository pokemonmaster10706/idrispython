import time

d = {}


while True:

    print(' menu driven programme \n 0. exit menu driven programme \n 1. enter student details \n 2. display all students \n 3. search for a student \n 4. modify student details \n 5. remove a student ')
    ch = int(input('\n\n what do you want to do? (0/1/2/3/4/5): \n'))

    if ch == 0:
        print('       thank you for using this menu driven programme \n                           good bye')
        break

    elif ch == 1:
        l = []
        rol = int(input('\n enter student roll number : '))
        nam = input('\n enter student name : ')
        grd = int(input('\n enter student grade : '))
        div = input('\n enter student division : ')
        d[rol] = [nam,grd,div]
        print('\n\n student successfully added to database')
        time.sleep(1)

    elif ch == 2:
        for i in d:
            print('\n',i,   d[i][0],   d[i][1],   d[i][2])
        print('\n end of student data base \n\n')
        time.sleep(1)

    elif ch == 3:
        er = int(input('enter student roll number : '))
        for i in d:
            if i == er:
                print('\n',i,   d[i][0],   d[i][1],   d[i][2],'\n')
        time.sleep(1)

    elif ch == 4:
        chr = int(input('enter student roll number : '))
        for i in d:
            if i == chr:
                l=[]
                nam1 = input('\n enter modified student name : ')
                grd1 = int(input('\n enter modified student grade : '))
                div1 = input('\n enter modified student division : ')
                d[i] = [nam1,grd1,div1]
                print('\n',i,   d[i][0],   d[i][1],   d[i][2])
                print('\n student details modified successfully')
        time.sleep(1)

    elif ch == 5:
        shr = int(input('enter student roll number : '))
        del d[shr]
        print('student removed from data base successfuly')

        time.sleep(1)
