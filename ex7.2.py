fname = input("Enter file name: ")
fh = open(fname)
count = 0
xar = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        pos = line.find(" ")
        var = line[pos + 1 : ]
        fvar = float(var)
        xar = xar + fvar
print("Average spam confidence:", xar/count)
