def factorial():
    n = int(input('Please enter a number to find its factorial: '))
    f = 1
    for i in range(1,n+1): f *= i
    print(f'The factorial of the number {n} is {f}')

def even_odd():
    n = int(input('Please enter a number to chech wether its even or odd: '))
    while True:
        if str(n).isdigit():
            if n%2 == 0:print('number is even')
            else:print('number is odd')
            break
        else:print('please enter a valid number')

def sum_of_digits():
    n = int(input('Please enter a number to find sum of digits: '))
    s = 0
    while n>0:
        s += n%10
        n//=10
    print('sum of all the digits of the number is: ',s)

def reverse():
    n = int(input('Please enter a number to reverse: '))
    rev = 0
    on = n
    while n > 0:
        rev = rev*10+n%10
        n//=10
    print(f'reverse of {on} is {rev}')

def palindrome():
    n = int(input('Please enter a number to check for palindrome: '))
    rev = 0
    on = n
    while n > 0:
        rev = rev*10+n%10
        n//=10
    if rev == on:print(f'yes the number {on} is a palindrome')
    else:print(f'the number {on} is not a palindrome')

def armstrong():
    n = int(input('Please enter a number to check for armstrong: '))
    degree = len(str(n))
    on = n
    s = 0
    while n>0:
        s += (n%10)**degree
        n//=10
    if s == on :print(f'the number {on} is an armstrong')
    else:print(f'the number {on} is not an armstrong')

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Factorial of a number
    2. Check the number is even or odd 
    3. Find the sum of digits of a number 
    4. Reverse the number 
    5. Check whether the number is Palindrome or not 
    6. Check the number is Armstrong or not 
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:factorial()
    elif ch == 2:even_odd()
    elif ch == 3:sum_of_digits()
    elif ch == 4:reverse() 
    elif ch == 5:palindrome()
    elif ch == 6:armstrong()
    else:print('please enter a valid choice\n')

