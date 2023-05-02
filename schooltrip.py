coach_cost = 550
entryticket_cost = 30
student_dict = {}
accepted = []
rejected = []
run_time = 0

def cost(num):
    global total_cost
    total_cost = (entryticket_cost*num)-(num//10)+coach_cost
    costper_student = (total_cost/num)+1
    return costper_student

def profit():
    collected = costper_student*len(accepted)
    difference = collected - total_cost
    if collected > total_cost:
        print('we gain a profit of',difference)
    elif difference == 0 :
        print('no profit no loss')
    else:
        print('a loss of',-difference,'is found')

def main():
    global run_time, costper_student
    while True:
        try:
            student_count = int(input('enter the number of student who wish to go to the school trip : '))
            if student_count > 45:
                print('max students allowed is 45')
                continue
            else:
                break
        except:
            print('please enter a valid integer value')
            continue
    costper_student = cost(student_count)
    print('each student must pay a total of ',costper_student)
    while True:
        name = input('enter student '+str(run_time+1)+' name:  ')
        if name in student_dict:
            print(name,'has already been entered, please enter next student')
            continue
        else:
            run_time += 1
            pay_status=input('has this student payed for the trip(y/n)?   \n\n')
            if pay_status == 'y':
                pay = 'paid'
                accepted.append(name)
            else:
                pay = 'pending'
                rejected.append(name)
            student_dict[name]=pay
            if run_time == student_count:
                break
    for k in student_dict:
        print('student name:',k,'\npayement status:',student_dict[k],'\n')


    print('the students who have paid and will be going to the trip are : ')
    for i in accepted:
        print(i)
    else:
        print('-'*100)
    print('the students who havent paid yet are :')
    for i in rejected:
        print(i)
    else:
        print('-'*100)

    profit()



main()
