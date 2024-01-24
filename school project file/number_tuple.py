numl = []
for i in range(int(input('how many elements are there in the tuple? : '))):
    numl.append(int(input('enter element: ')))

numtup = tuple(numl)
n = int(input('enter number to find occurence in the tuple : '))
ncount = 0

for i in numtup:
    if i == n:ncount+=1

if ncount == 0:print('Sorry, the number you are searching is not in the tuple')
else:print(f'the number {n} appeared in the tuple {ncount} times')