


l = []
for i in range(int(input('how many elements in the list? '))):
    l.append(int(input('enter value for list: ')))

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Sum of elements in the list 
    2. Sum of elements at even positions 
    3. Sum of elements at odd positions  
    0. Quit''')
    while True:
        try:
            ch = int(input('enter your choice: '))
            break
        except:
            print('please enter only valid numbers\n\n')
        
    if ch == 0:
        break

    elif ch == 1:

        print(sum(l))
    
    elif ch == 2:
        s=0
        for i in range(0,len(l)+1,2):
            s+=l[i]
        print(s)
        
    
    elif ch == 3:
        s=0
        for i in range(1,len(l)+1,2):
            s+=l[i]
        print(s)
            
    else:
        print('please enter a valid choice\n')
