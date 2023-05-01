import time

d = {}


while True:

    print(' menu driven programme \n 0. exit menu driven programme \n 1. enter teacher details \n 2. display all teachers \n 3. search for a teacher \n 4. modify teacher details \n 5. remove a teacher ')
    ch = int(input('\n\n what do you want to do? (0/1/2/3/4/5): \n'))

    if ch == 0:
        print('       thank you for using this menu driven programme \n                           good bye')
        break

    elif ch == 1:
        l = []
        T_ID = int(input('\n enter teacher  ID : '))
        nam = input('\n enter teacher name : ')
        sub = input('\n enter teacher subject : ')
        d[T_ID] = [nam,sub]
        print('\n\n teacher successfully added to database')
        time.sleep(1)

    elif ch == 2:
        for i in d:
            print('\n',i,   d[i][0],   d[i][1])
        print('\n end of teacher data base \n\n')
        time.sleep(1)

    elif ch == 3:
        t = False
        v = input('would you like to search using ID or name? (ID/name)')
        if v == 'ID':
            er = int(input('enter teacher  ID : '))
            for i in d:
                if i == er:
                    print('\n',i,   d[i][0],   d[i][1],'\n')
                    t = True
        elif v == 'name':
            g = input('enter teacher name : ')
            for i in d:
                if d[i][0] == g:
                    print('\n',i,   d[i][0],   d[i][1],'\n')
                    t = True
        if t is False:
            print('teacher not found in database')
        time.sleep(1)

    elif ch == 4:
        chr = int(input('enter teacher  ID : '))
        for i in d:
            if i == chr:
                l=[]
                nam1 = input('\n enter modified teacher name : ')
                sub1 = input('\n enter modified teacher subject : ')
                d[i] = [nam1,sub1]
                print('\n',i,   d[i][0],   d[i][1])
                print('\n teacher details modified successfully')
        time.sleep(1)

    elif ch == 5:
        shr = int(input('enter teacher  ID : '))
        del d[shr]
        print('teacher removed from data base successfuly')

        time.sleep(1)
