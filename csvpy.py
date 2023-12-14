import csv

headers = ['St_Id','Name','Game_Name','Result']

def Accept(file):
    with open(f'{file}','a',newline = '') as csvfile:
        st_id = int(input('Enter student id: '))
        st_name = input('Enter student name: ')
        game = input('Enter game name: ')
        result = input('Enter result: ')
        mywriter = csv.writer(csvfile)
        mywriter.writerow(headers)
        mywriter.writerow([st_id,st_name,game,result])
        print('Data Entered Successfully')

def WonCount(file):
    count = 0
    with open(f'{file}','r') as csvfile:
        myreader = csv.reader(csvfile)
        for i in myreader:
            if i[3] == 'WON':
                count+=1
                print(i[1])
    print(f'total number of winners is:{count}')

while True:
    Accept('Result.csv')
    if input('do you want to continue') == 'y':
        continue
    else:
        break
WonCount('Result.csv')