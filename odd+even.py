l = int(input('enter lower limit: '))
u = int(input('enter upper limit: '))

es = 0
os = 0

for i in range(l ,u+1):
    if i%2 == 0:
        es += i
    else:
        os += i
print('sum of all even numbers is:', es)
print('sum of all odd numbers is: ', os)
