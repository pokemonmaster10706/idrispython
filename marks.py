name = input('enter name:')
eng = int(input('enter eng marks:'))
math = int(input('enter math marks:'))
phy = int(input('enter physics marks:'))
chem = int(input('enter chemistry marks:'))
comp = int(input('enter computer marks:'))

total = eng+math+phy+chem+comp
per = total/5

s = str(per)
c = int(s.split('.')[1])
if c > 0:
    per = float(per)
else:
    per = int(per)

print(name)
print('total marks =',total)
print('percentage =', per)
