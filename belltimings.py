import colorama #install colorama module for Python
from colorama import Fore

d_T_res = []
d_S_res = []

S_response = []
T_response = []
ID_list = []

A_sum_T = 0
B_sum_T = 0
C_sum_T = 0
D_sum_T = 0
E_sum_T = 0
A_sum_S = 0
B_sum_S = 0
C_sum_S = 0
D_sum_S = 0
E_sum_S = 0


#the below variables are for the tally marks

#tally for the teachers
TA1=0
TB1=0
TC1=0
TD1=0
TE1=0
#tally for the students
SA1=0
SB1=0
SC1=0
SD1=0
SE1=0

print(Fore.GREEN + 'PYTHON SCHOOL BELL TIMINGS PROPOSAL \n\nThe school has been given options for bell timings proposed by the staff and other members \nWe would like to know what your opinions are on this matter')
print(Fore.YELLOW + '\n\nGiven are five options, please rate all of them from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
print(Fore.GREEN + '\n\nYou will be asked to enter your four digit ID number given to you by the school, \nStaff ID starting with T and student ID starting with S')

while True:
    id = input(Fore.MAGENTA + 'Please enter your four digit ID number : ')
    if id in ID_list:
        print(Fore.RED + 'Sorry, that ID has already been used \nPlease check if you have mistyped it or enter another ID.')
        continue
    elif len(id) != 4:
        print(Fore.RED + 'sorry invalid ID, please enter again.')
        continue
    else:
        ID_list.append(id)

    if id.startswith('T') or id.startswith('t'):
        while True:
            print(Fore.CYAN + 'the first option is : ',Fore.BLUE + '\n|A Start time: 08:00- End time: 15:00|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                A = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if A>5 or A<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if A == 1:
                    TA1 += 1
                A_sum_T += A
                break
        while True:
            print(Fore.CYAN + 'the second option is :',Fore.BLUE + ' \n|B Start time: 08:20-End time: 15:20|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                B = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if B>5 or B<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if B == 1:
                    TB1 += 1
                B_sum_T += B
                break
        while True:
            print(Fore.CYAN + 'the third option is : ',Fore.BLUE + '\n|C Start time: 08:40-End time: 15:40|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                C = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if C>5 or C<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if C == 1:
                    TC1 += 1
                C_sum_T += C
                break
        while True:
            print(Fore.CYAN + 'the fourth option is : ',Fore.BLUE + '\n|D Start time: 09:00- End time: 16:00|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                D = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if D>5 or D<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if D == 1:
                    TD1 += 1
                D_sum_T += D
                break
        while True:
            print(Fore.CYAN + 'the final option is : ',Fore.BLUE + '\n|E Start time: 09:30-End time: 16:30|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                E = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if E>5 or E<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if E == 1:
                    TE1 += 1
                E_sum_T += E
                break

        d_T_res = {id:{'A': A ,'B':B,'C':C,'D':D,'E':E}}
        T_response.append(d_T_res)

    elif id.startswith('S') or id.startswith('s'):

        while True:
            print(Fore.CYAN + 'the first option is : ',Fore.BLUE + '\n|A Start time: 08:00- End time: 15:00|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                A = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if A>5 or A<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if A == 1:
                    SA1 += 1
                A_sum_S += A
                break
        while True:
            print(Fore.CYAN + 'the second option is :',Fore.BLUE + ' \n|B Start time: 08:20-End time: 15:20|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                B = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if B>5 or B<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if B == 1:
                    SB1 += 1
                B_sum_S += B
                break
        while True:
            print(Fore.CYAN + 'the third option is : ',Fore.BLUE + '\n|C Start time: 08:40-End time: 15:40|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                C = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if C>5 or C<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if C == 1:
                    SC1 += 1
                C_sum_S += C
                break
        while True:
            print(Fore.CYAN + 'the fourth option is : ',Fore.BLUE + '\n|D Start time: 09:00- End time: 16:00|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                D = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if D>5 or D<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if D == 1:
                    SD1 += 1
                D_sum_S += D
                break
        while True:
            print(Fore.CYAN + 'the final option is : ',Fore.BLUE + '\n|E Start time: 09:30-End time: 16:30|',Fore.CYAN + '\nrate this from 1 - 5 :')
            try:
                E = int(input(Fore.GREEN + ''))
            except:
                print(Fore.RED + 'please enter a valid option')
                continue
            if E>5 or E<1:
                print(Fore.RED + 'Invalid value, Please enter correct value')
                print(Fore.YELLOW + '\n\nplease rate this proposal from 1 - 5 :  \n1 ---- strongly agree \n2 ---- agree \n3 ---- neutral \n4 ---- disagree \n5 ---- strongly disagree')
                continue
            else:
                if E == 1:
                    SE1 += 1
                E_sum_S += E
                break
        d_S_res = {id:{'A': A ,'B': B ,'C': C ,'D': D ,'E': E }}
        S_response.append(d_S_res)

    else:
        print(Fore.RED + 'invalid ID \nPlease check if you have mistyped it or enter another ID')
        continue
    print(Fore.MAGENTA + 'would you like to enter another response?(y/n): ')
    cont=input(Fore.YELLOW + '')
    if cont.lower() == 'y':
        continue
    else:
        Tally_T = [TA1,TB1,TC1,TD1,TE1]
        Tally_S = [SA1,SB1,SC1,SD1,SE1]
        total_S = [A_sum_S ,B_sum_S ,C_sum_S ,D_sum_S ,E_sum_S]
        total_T = [A_sum_T ,B_sum_T ,C_sum_T ,D_sum_T ,E_sum_T]
        break

#the totalling results

print(Fore.CYAN + '\nThank you for your response, the results are given below.')
if len(d_T_res) < 1:
    print(Fore.CYAN + '\n\n-------------------------------------------------------------------------------------------')
    print(Fore.RED + 'No responses were given by teachers.....')
    print(Fore.RED + '-------------------------------------------------------------------------------------------')
else:
    print(Fore.CYAN + '\n\n-------------------------------------------------------------------------------------------')
    print(Fore.BLUE + 'Teacher response results : \nResults for option A - Start time: 08:00- End time: 15:00 :',total_T[0])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',TA1,'times by teachers')
    print(Fore.BLUE + '\nResults for option B - Start time: 08:20- End time: 15:20 :',total_T[1])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',TB1,'times by teachers')
    print(Fore.BLUE + '\nResults for option C - Start time: 08:40- End time: 15:40 :',total_T[2])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',TC1,'times by teachers')
    print(Fore.BLUE + '\nResults for option D - Start time: 09:00- End time: 16:00 :',total_T[3])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',TD1,'times by teachers')
    print(Fore.BLUE + '\nResults for option E - Start time: 09:20- End time: 16:20 :',total_T[4])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',TE1,'times by teachers')
    print(Fore.CYAN + '-------------------------------------------------------------------------------------------')

if len(d_S_res) < 1:
    print(Fore.CYAN + '\n\n-------------------------------------------------------------------------------------------')
    print(Fore.RED + 'No responses were given by students.....')
    print(Fore.RED + '-------------------------------------------------------------------------------------------')
else:
    print(Fore.CYAN + '\n\n-------------------------------------------------------------------------------------------')
    print(Fore.GREEN + '\n\nStudent response results : \nResults for option A - Start time: 08:00- End time: 15:00 :',total_S[0])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SA1,'times by students')
    print(Fore.GREEN + '\nResults for option B - Start time: 08:20- End time: 15:20 :',total_S[1])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SB1,'times by students')
    print(Fore.GREEN + '\nResults for option C - Start time: 08:40- End time: 15:40 :',total_S[2])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SC1,'times by students')
    print(Fore.GREEN + '\nResults for option D - Start time: 09:00- End time: 16:00 :',total_S[3])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SD1,'times by students')
    print(Fore.GREEN + '\nResults for option E - Start time: 09:20- End time: 16:20 :',total_S[4])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SE1,'times by students')
    print(Fore.CYAN + '-------------------------------------------------------------------------------------------')

if len(d_S_res)+len(d_T_res) > 0:
    print(Fore.CYAN + '\n\n-------------------------------------------------------------------------------------------')
    print(Fore.CYAN + '\n\nTotal response results :','\nResults for option A - Start time: 08:00- End time: 15:00 :',total_S[0] + total_T[0])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SA1 + TA1,'times by both teachers and students')
    print(Fore.CYAN + '\nResults for option B - Start time: 08:20- End time: 15:20 :',total_S[1] + total_T[1])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SB1 + TB1,'times by both teachers and students')
    print(Fore.CYAN + '\nResults for option C - Start time: 08:40- End time: 15:40 :',total_S[2] + total_T[2])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SC1 + TC1,'times by both teachers and students')
    print(Fore.CYAN + '\nResults for option D - Start time: 09:00- End time: 16:00 :',total_S[3] + total_T[3])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SD1 + TD1,'times by both teachers and students')
    print(Fore.CYAN + '\nResults for option E - Start time: 09:20- End time: 16:20 :',total_S[4] + total_T[4])
    print(Fore.YELLOW + 'This option was ranked strongly agree :',SE1 + TE1,'times by both teachers and students/n/n')
    print(Fore.CYAN + '-------------------------------------------------------------------------------------------')
else:
    print(Fore.CYAN + '\n\n-------------------------------------------------------------------------------------------')
    print(Fore.RED + 'sorry there were no responses..../n/n')
    print(Fore.RED + '-------------------------------------------------------------------------------------------')

print(Fore.BLUE + '\n\nthat is the end of the results, Thank you!!')
print(Fore.WHITE + '')
