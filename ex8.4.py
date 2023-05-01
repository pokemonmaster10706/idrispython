fname = input("Enter file name: ")
lst = list()
fh = open(fname)
for line in fh:
    line.rstrip()
    lam = line.split()
    for piece in lam :
        if piece in lst :
            continue
        else :
            lst.append(piece)
lst.sort()
print(lst)
