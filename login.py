user_count = input('enter the number of users who will be loging in this time?\n\n')

check = 1
while True:
    username = input('user '+check+' enter your username :  ')
    if username in details:
        print('the user name',username,'is already in use, please enter a different one.')
        continue
    password = input('enter a password for '+username+' \npassword must contain more than 8 characters,a capital and a lowercase alphabet, a number, and a special character :')
