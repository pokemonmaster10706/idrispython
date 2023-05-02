coach_cost = 550
entryticket_cost = 30
student_dict = {}

while True:
    try:
        student_count = int(input('enter the number of student who wish to go to the school trip : '))
        if student_count > 45:
            print('max students allowed is 45')
            continue
    except:
        print('please enter a valid integer value')

for i in range(student_count):
    name = input('enter student '+str(i+1)+' name:  ')
    if name in student_dict:
        print(name,'has already been entered, please enter next student')
        continue
    else:
        pay_status=input('has this student payed for the trip(y/n)?   \n\n')
        if pay_status == 'y':
            pay = 'paid'
        else:
            pay = 'pending'
        student_dict[name]=pay



total_cost = (entryticket_cost*student_count)-(student_count//10)+coach_cost
costper_student = (total_cost/student_count)+1
print(costper_student)
