def file_input():
    with open('textfile.txt','a',newline = '') as file:
        file. write('/n',input('enter something to put in the file: \n'))

def file_output():
    with open('textfile.txt','r') as file:
        content = file.read()
        print(content)

def file_count():
    with open('textfile.txt','r') as file:
        content = file.read()
        vcount ,ccount ,lowcount ,uppcount =0,0,0,0
        for i in content:
            if i.lower() in 'aeiou':vcount += 1
            elif i.isalpha():ccount += 1
            if i.islower():lowcount += 1
            elif i.isupper():uppcount += 1
    print(f'''The total number of characters in the file are : {len(content)}
The number of vowels are : {vcount}
The number of consonants are : {ccount}
The number of lowercase letters are: {lowcount}
The number of uppercase letters are : {uppcount}''')


while True:
    print('\n\n     ----------MENU-DRIVEN-PROGRAM----------\n')
    print('''    1. Input some contents into a file. 
    2. Output the contents from the file. 
    3. Count and display number of vowels, consonants, lowercase and uppercase characters in the file. 
    0. Quit''')
    while True:
        try:ch = int(input('enter your choice: '));break
        except:print('please enter only valid numbers\n\n')
    if ch == 0:break
    elif ch == 1:file_input()
    elif ch == 2:file_output()
    elif ch == 3:file_count()
    else:print('please enter a valid choice\n')
