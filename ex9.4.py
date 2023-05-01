name = input("Enter file: ")
handle = open(name)
dict = dict()
for line in handle :
    if line.startswith("From ") :
        ls = line.split()
        key = ls[1]
        dict[key] = dict.get(key , 0) + 1
    else :
        continue
bigcount = None
bigword = None
for k,v in dict.items() :
    if bigcount is None or v > bigcount :
        bigword = k
        bigcount = v
print(bigword,bigcount)
