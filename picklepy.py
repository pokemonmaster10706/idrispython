import pickle,tabulate

def enter(file):
    with open(f'{file}','rb') as bf:
        try:rec = pickle.load(bf)
        except: rec=[]
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
        print(tabulate.tabulate(rec,headers=['id','name','salary']))
        print('\n')

enter('picklefile.bat')
display('picklefile.bat')