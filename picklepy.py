import pickle

def enter(file):
    with open(f'{file}','rb') as bf:
        rec = pickle.load(bf)
    with open(f'{file}','wb') as bf:
        id = int(input('enter employee id: '))
        name = input('enter employee name: ')
        sal = int(input('enter salary: '))
        rec.append([id,name,sal])
        pickle.dump(rec,bf)
        print(rec)

def display(file):
    with open(f'{file}','rb') as bf:
        rec = pickle.load(bf)
        for i in rec:
            for j in i:
                print(j,end=' ')
            print('\n')

enter('picklefile.bat')
display('picklefile.bat')