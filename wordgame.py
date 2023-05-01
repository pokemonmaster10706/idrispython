import random
from colorama import Fore

tn = 0
score={}
l=[]
v = 'aeiou'
print(Fore.GREEN + 'how many people are playing?')
n = int(input(Fore.YELLOW + ''))
while True:
    print(Fore.BLUE + '\nenter player '+ str(tn+1) +' name')
    a = input(Fore.CYAN + '')
    if a in l:
        print(Fore.RED + '\n\nname has already been entered please use a different name\n')
        continue
    tn += 1
    score[a]=0
    l.append(a)
    if n == tn:
        break
print(Fore.CYAN + '\nenter how many rounds: ')
m = int(input(Fore.YELLOW + ''))
r = random.randint(1,n) - 1
print(Fore.MAGENTA +'\n  ', l[r],'starts')

last='a'
rounds = 0
run=0
wordl = []
print(Fore.BLUE + '\n\nfirst player',l[r], 'enter a word that starts with',last)
while True:
    z = 0
    word = input(Fore.CYAN + 'enter word: ')
    if word.isalpha():
        pass
    else :
        print(Fore.RED + 'please dont input anything other than alphabet')
        continue
    if word.startswith(last):
        pass
    else:
        print(Fore.RED + 'player',l[r],'loses ten points because',word,'does not start with', last, 'please enter a word that starts with',last)
        score[l[r]] -= 10
        continue
    if word not in wordl:
        wordl.append(word)
        pass
    else:
        print(Fore.RED + 'player',l[r],'loses ten points because',word,'has already been input please enter a word that has not already been used')
        score[l[r]] -= 10
        continue
    for i in word.lower():
        if i in v:
            score[l[r]] += 10
            z += 10
        else:
            score[l[r]] += 5
            z += 5
    print(Fore.GREEN + l[r],'gets',z,'points for the word',word)
    if r == n-1:
        r = 0
    else:
        r += 1
    last = word[-1]
    print(Fore.BLUE + '\n\nnext player',l[r], 'enter a word that starts with',last)
    run += 1
    if run == n:
        run = 0
        rounds += 1
    if rounds == m:
        print(Fore.YELLOW + 'all rounds have finished')
        break
min = score[l[0]]
max = score[l[0]]
#print(score)
for k,v in score.items():
    if v >= max:
        max = v
        win = k
    if v <= min:
        min = v
        lose = k
print(Fore.GREEN + '\n\nwinner is',win,'with',max,'points')
print(Fore.GREEN + 'CONGRATS!!')
print(Fore.RED + '\n\nloser is',lose,'with a total of',min,'points')
print(Fore.RED + 'sed lyfe ')
print(Fore.WHITE + '')
