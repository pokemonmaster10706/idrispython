l1=[]
l2 = []
l3 = []

n = int(input('enter amount of strings you would like to add : '))
for i in range (n):
    a = input('enter element for list one: ')
    l1.append(a)
for i in l1:
    if len(i) not in l2:
        l2.append(len(i))
l2.sort()
for i in l2:
    for j in l1:
        if i == len(j):
            l3.append(j)
print(l3)
