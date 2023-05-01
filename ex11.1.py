import re
file = input("Enter file name: ")
handle = open(file)
nums = list()
sums = list()
for line in handle :
    line = line.rstrip()
    num = re.findall("[0-9]+" ,line)
    nums = nums + num
for n in nums :
    n = int(n)
    #print(n)
    sums.append(n)
print(sum(sums))
