import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='idris7',database='school')

def main():
    while True:
        print('\n\tMENU DRIVEN PROGRAM\n\
        1. Display all Records\n\
        2. Search for an Entry\n\
        3. Insert an Entry\n\
        4. Modify an Entry\n\
        5. Delete an Entry\n\
        6. Exit\n')

        choice = int(input('Enter Choice: '))
        if choice == 1:
            display()
        elif choice == 2:
            search()
        elif choice == 3:
            insert()
        elif choice == 4:
            modify()
        elif choice == 5:
            delete()
        else :
            break

def display():
    dis_cur =  mycon.cursor()
    dis_cur.execute('select * from employee1')
    mydata = dis_cur.fetchall()
    rec_count = dis_cur.rowcount
    print('The Total records are',rec_count)
    for row in mydata:
        print('|',row,'|')
    print('\n')

def search():
    nameid = input('Search by Name or ID Number (n/i): ')
    if nameid == 'n':
        search_name = input('Enter Name: ')
        cur_search = mycon.cursor()
        cur_search.execute('select * from employee1 where name = "'+search_name+'"')
        mydata = cur_search.fetchall()
        for row in mydata:
            print('\nthe employee1 you are looking for is\n|',row,'|')

    else:
        search_num = input('Enter ID: ')
        cur_search = mycon.cursor()
        cur_search.execute('select * from employee1 where empno = "'+str(search_num)+'"')
        mydata = cur_search.fetchall()
        cur_search.close()
        print('\nthe employee1 you are looking for is\n|',mydata,'|')
    print('\n')

def insert():
    empno = input('enter employee ID: ')
    ename = input('enter employee name: ')
    job = input('enter job: ')
    mgr = input('enter manager ID: ')
    hiredate = input('enter hire date in the format (yyyy-mm-dd) : ')
    sal = input('enter salary earned: ')
    comm = input('enter commision: ')
    deptno = input('enter department number: ')
    cur_insert = mycon.cursor()
    cur_insert.execute('insert into employee1 values('+empno+',"'+ename+'","'+job+'",'+mgr+',"'+hiredate+'",'+sal+','+comm+','+deptno+')')
    cur_insert.execute('select * from employee1 where empno ='+empno)
    cur_insert.close()
def modify():
    pass

def delete():
    del_id = input('enter Employee ID to Delete: ')
    cur_del = mycon.cursor()
    cur_del.execute('select ename from employee1 where empno = '+del_id)
    del_name = cur_del.fetchall()
    cur_del.execute('delete from employee1 where empno = '+del_id)
    cur_del.close()
    print('deleted employee ',del_name)

if __name__ == '__main__':
    main()
