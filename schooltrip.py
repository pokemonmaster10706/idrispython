coach_cost = 550
entryticket_cost = 30
while True:
    try:
        student_count = int(input('enter the number of student who wish to go to the school trip : '))
        if student_count > 45:
            print('max students allowed is 45')
            continue
    except:
        print('please enter a valid integer value')


total_cost = (entryticket_cost*student_count)-(student_count//10)+coach_cost
costper_student = (total_cost/student_count)+1
print(costper_student)
