def is_empty(s):
    if len(s) == 0:return True
    else:return False

def push(s,item):s.append(item);top=len(s)-1

def pop(s):
    if is_empty(s):print('UnderFlow')
    else:
        val = s.pop()
        if len(s) == 0:top = None
        else:top = len(s)-1
        return val
    
def peek(s):
    if is_empty(s):print('UnderFlow')
    else:top = len(s)-1;return s[top]
        
def show(s):
    if is_empty(s):print('Sorry,no elements in stack.')
    else:
        for i in range(len(s)):
            print(s[i])

s = []
top = None
while True:
    print('\n\n     ----------STACK-DEMONSTRATION----------\n')
    print('''    1. Push
    2. Pop 
    3. Peek 
    4. Show stack 
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:push(s,input('enter element to enter into stack:  '))
    elif ch == 2:
        val = pop(s)
        if val == 'UnderFlow':print('stack empty')
        else:print(f'the deleted value was : {val}')
    elif ch == 3:
        val = peek(s)
        if val == 'UnderFlow':print('stack empty')
        else:print(f'the top item is : {val}')
    elif ch == 4:show(s)
    else:print('please enter a valid choice\n')
