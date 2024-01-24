paswrd = input("Enter PASSWORD: ")
length_check = False

nmbr_check = False

spl = '`~!@#$%^&*()_-+={[:;\\\'\"<>,.?/]}'
spl_check = False

upper_check = False

if len(paswrd) > 7:
    length_check = True
    print('1')
for i in paswrd:
    if i.isdigit():
        print('2')
        nmbr_check = True
        continue
    else:
        if i in spl:
            print('3')
            spl_check = True
            continue
        else:
            if i.isupper():
                print('4')
                upper_check = True
                continue
            else:
                print('5')
                continue
print('6')
if length_check == spl_check == nmbr_check == upper_check == True :
    print('Valid')
else:
    print('invalid')
