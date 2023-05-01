name = input("Enter file:")
handle = open(name)
count = dict()
for line in handle :
    if line.startswith("From ") :
        words = line.split()
    else :
        continue
    word = words[5]
    time = word.split(":")
    hour = time[0]
    count[hour] = count.get(hour,0) + 1
lst = list()
for key,val in count.items() :
    newtup = (key,val)
    lst.append(newtup)
lst = sorted(lst)
for key,val in lst :
#    print(val,key)
    print(key,val)
