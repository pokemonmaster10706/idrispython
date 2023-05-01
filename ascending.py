print('\n\n')

a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))

print('\n\n')

t = False
u = False
v = False

k = False
l = False
m = False

if a == b:
    print('a=b')
    t = True
if b == c:
    print('b=c')
    u = True
if c == a:
    print('c=a')
    v = True

if t is False :
    if a > b :
        if v is False :
            if a > c :
                print('the first number is',a)
                k = True
            else:
                print('the first number is',c)
                m = True
    elif b > a :
        if u is False :
            if b > c :
                print('the first number is',b)
                l = True
            else:
                print('the first number is',c)
                m = True

if k is True :
    if b > c :
        print('the second number is',b)
        print('the third number is',c)
    else:
        print('the second number is',c)
        print('the third number is',b)
elif l is True :
    if a > c :
        print('the second number is',a)
        print('the third number is',c)
    else:
        print('the second number is',c)
        print('the third number is',a)
elif m is True :
    if b > a :
        print('the second number is',b)
        print('the third number is',a)
    else:
        print('the second number is',a)
        print('the third number is',b)
