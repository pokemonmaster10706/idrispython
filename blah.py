l = []
n = int(input('enter how many numbers you would like to enter : '))
for i in range(n):
    a = int(input('enter number :'))
    l.append(a)

print(l)

for j in l :
    if j % 10 == 0:
        m = j
        s=0
        while j > 0 :
            r = j % 10
            s = s * 10 + r
            j = j // 10
        l.remove(m)
        l.append(s)
print(l)
