fname = input('enter file name :')
handle = open(fname)
y=0
x = list()
for line in handle :
    words = line.split()
    y=y+len(words)
    print(words)

print(y)
