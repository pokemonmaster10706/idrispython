n = int(input('enter value: '))
a = 0
s = 0
b = 1
print(a, b, end=' ')
for i in range(n):
    s = a + b
    print(s, end=' ')
    a = b
    b = s
