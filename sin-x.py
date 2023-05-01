x = int(input('enter number to find sin : '))
a = int(input('enter number of times to run : '))

n = 1
s = 0

for i in range(a):
    c = 1
    for j in range(1,n+1):
        c *= j
    if i % 2 == 0:
        s += x**n/c
#        print(s)
    else:
        s -= x**n/c
#        print(s)
    n += 2
print('sin x = ', s)
