class employee:
    empcount = 0

    def __init__(self,name,sal):
        self.name = name
        self.email = f'{name}@gmail.com'
        self.sal = sal
        employee.empcount += 1
        l.append(self)


# emp1 = employee('idris',12000)
# emp2 = employee('ahsdj',12000)
# emp3 = employee('dhays',12000)
l = []
for x in range( 9):
    globals()[f'emp{x}'] = employee(f'idris{x}',12000)


for i in range(len(l)):
    print(globals()[f'emp{i}'].email)

print(employee.empcount)