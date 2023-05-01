student_response = list()
student_ID_list = list()
student_A = 0
student_B = 0
student_C = 0
student_D = 0
student_E = 0

student_A_ = list()
student_B_ = list()
student_C_ = list()
student_D_ = list()
student_E_ = list()

staff_response = list()
staff_ID_list = list()
staff_A = 0
staff_B = 0
staff_C = 0
staff_D = 0
staff_E = 0

staff_A_ = list()
staff_B_ = list()
staff_C_ = list()
staff_D_ = list()
staff_E_ = list()

print('\n\t\tBELL TIMING PROPOSAL')
print('\nWe would like to allow students and staff to show their preference on the start and finish time of the school days.')

while True:
    position = input('\n\nAre you a Student? (y/n)\t')
    if position == 'Y' or position == 'y':
        while True:
            id = input('Please Enter your Unique ID Number :\t')
            if id in student_ID_list:
                print('\nID has been used already. Please Try Again\n')
                continue
            else:
                student_ID_list.append(id)
                break

        print('\nOptions:\n\
            Option A | Start: 08:00 - Finish: 15:00\n\
            Option B | Start: 08:20 - Finish: 15:20\n\
            Option C | Start: 08:40 - Finish: 15:40\n\
            Option D | Start: 09:00 - Finish: 16:00\n\
            Option E | Start: 09:30 - Finish: 16:30\n\n')

        print('Please Rate each of them from 1 - 5: \n\
              1: Strongly Agree \n\
              2: Agree \n\
              3: Neutral \n\
              4: Disagree \n\
              5: Strongly Disagree\n\n')

        while True:
            print('Option A | Start: 08:00 - Finish: 15:00')
            a = int(input('Please Rate this Option: '))
            if a<1 or a>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                student_A += a
                student_A_.append(a)
                break

        while True:
            print('\nOption B | Start: 08:20 - Finish: 15:20')
            b = int(input('Please Rate this Option: '))
            if b<1 or b>5:
                print('\nINVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                student_B += b
                student_B_.append(b)
                break

        while True:
            print('\nOption C | Start: 08:40 - Finish: 15:40')
            c = int(input('Please Rate this Option: '))
            if c<1 or c>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                student_C += c
                student_C_.append(c)
                break

        while True:
            print('\nOption D | Start: 09:00 - Finish: 16:00')
            d = int(input('Please Rate this Option: '))
            if d<1 or d>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                student_D += d
                student_D_.append(d)
                break

        while True:
            print('\nOption E | Start: 09:30 - Finish: 16:30')
            e = int(input('Please Rate this Option: '))
            if e<1 or e>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                student_E += e
                student_E_.append(e)
                break
        student_response.append({id:{'A':a,'B':b,'C':c,'D':d,'E':e}})

    elif position == 'N' or position == 'n':
        while True:
            id = input('Please Enter your Unique ID Number : ')
            if id in staff_ID_list:
                print('ID has been used already. Please Try Again')
                continue
            else:
                staff_ID_list.append(id)
                break
        print('\nThese are the 5 Options:\n\
            Option A | Start: 08:00 - Finish: 15:00\n\
            Option B | Start: 08:20 - Finish: 15:20\n\
            Option C | Start: 08:40 - Finish: 15:40\n\
            Option D | Start: 09:00 - Finish: 16:00\n\
            Option E | Start: 09:30 - Finish: 16:30\n\n')
        print('Please Rate each of them from 1 - 5 \n\
              1: Strongly Agree \n\
              2: Agree \n\
              3: Neutral \n\
              4: Disagree \n\
              5: Strongly Disagree\n\n')

        while True:
            print('Option A | Start: 08:00 - Finish: 15:00')
            a = int(input('Please Rate this Option: '))
            if a<1 or a>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                staff_A += a
                staff_A_.append(a)
                break

        while True:
            print('\nOption B | Start: 08:20 - Finish: 15:20')
            b = int(input('Please Rate this Option: '))
            if b<1 or b>5:
                print('\nINVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                staff_B += b
                staff_B_.append(b)
                break

        while True:
            print('\nOption C | Start: 08:40 - Finish: 15:40')
            c = int(input('Please Rate this Option: '))
            if c<1 or c>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                staff_C += c
                staff_C_.append(c)
                break

        while True:
            print('\nOption D | Start: 09:00 - Finish: 16:00')
            d = int(input('Please Rate this Option: '))
            if d<1 or d>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                staff_D += d
                staff_D_.append(d)
                break

        while True:
            print('\nOption E | Start: 09:30 - Finish: 16:30')
            e = int(input('Please Rate this Option: '))
            if e<1 or e>5:
                print('INVALID INPUT. Please enter values from 1 - 5.\n')
                continue
            else:
                staff_E += e
                staff_E_.append(e)
                break
        staff_response.append({id:{'A':a,'B':b,'C':c,'D':d,'E':e}})
    print('\n\nThank Youu for your Response.')
    cont = input('\nDo you want to Enter another Response? (y/n): ')
    if cont == 'Y' or cont == 'y':
        continue
    else:
        break

print('\n\nRESULTS')

print('\nStudent Response Results:')
print('Option A |',student_A)
print('Option B |',student_B)
print('Option C |',student_C)
print('Option D |',student_D)
print('Option E |',student_E)

print('\nStaff Response Results:')
print('Option A |',staff_A)
print('Option B |',staff_B)
print('Option C |',staff_C)
print('Option D |',staff_D)
print('Option E |',staff_E)

print('\nTotal Response Results:')
print('Option A |',student_A+staff_A)
print('Option B |',student_B+staff_B)
print('Option C |',student_C+staff_C)
print('Option D |',student_D+staff_D)
print('Option E |',student_E+staff_E)


print('\n\nNumber of times the preference 1 (Strongly Agree) was chosen by Students for:')
print('Option A |',student_A_.count(1))
print('Option B |',student_B_.count(1))
print('Option C |',student_C_.count(1))
print('Option D |',student_D_.count(1))
print('Option E |',student_E_.count(1))

print('\nNumber of times the preference 1 (Strongly Agree) was chosen by Staffs:')
print('Option A |',staff_A_.count(1))
print('Option B |',staff_B_.count(1))
print('Option C |',staff_C_.count(1))
print('Option D |',staff_D_.count(1))
print('Option E |',staff_E_.count(1))

print('\nNumber of times the preference 1 (Strongly Agree):')
print('Option A |',student_A_.count(1)+staff_A_.count(1))
print('Option B |',student_B_.count(1)+staff_B_.count(1))
print('Option C |',student_C_.count(1)+staff_C_.count(1))
print('Option D |',student_D_.count(1)+staff_D_.count(1))
print('Option E |',student_E_.count(1)+staff_E_.count(1))






print('\n\n\n\nCHECK\n')
print(student_response,student_ID_list,student_A,student_B,student_C,student_D,student_E,'\n\n')
print(staff_response,staff_ID_list,staff_A,staff_B,staff_C,staff_D,staff_E,'\n\n')
print(student_A_,student_B_,student_C_,student_D_,student_E_,'\t',staff_A_,staff_B_,staff_C_,staff_D_,staff_E_,'\n\n\n')
