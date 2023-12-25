import tabulate

def create():
    global d
    d = {}
    dl = []
    for i in range(int(input('how many elements do you want to add in the dictionary: '))):
        element = input(f'enter word #{i+1} to add: ')
        if element[0] not in dl:d[element[0]] = element;dl.append(element[0])
        else:print('an element with this letter has already been added to the dictionary.')

def display():print(tabulate.tabulate([list( d.values())],headers=list( d),tablefmt = 'pretty'))

def search():
    k = input('enter key to search : ')
    if k in  d:print(tabulate.tabulate([[k, d[k]]],headers = ['key','value'],tablefmt='pretty'))
    else:print('element doesent exist in dictionary')

def modify():
    k = input('enter key to modify : ')
    if k in  d:v = input('enter modified value : '); d[k] = v
    else:print('element doesent exist in dictionary')

def delete():
    k = input('enter key to search : ')
    if k in  d:del  d[k];print('element deleted')
    else:print('element doesent exist in dictionary')

while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Create a dictionary with a character as key 
       and a word starting with that letter as value. 
    2. Display all key value pairs in the dictionary. 
    3. Search for a particular key and print its value. 
    4. Modify the value of a particular key. 
    5. Delete a key value pair from the dictionary 
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:create()
    elif ch == 2:display()
    elif ch == 3:search()
    elif ch == 4:modify()
    elif ch == 5:delete()
    else:print('please enter a valid choice\n')
