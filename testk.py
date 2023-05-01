import random
from colorama import Fore
import tkinter as tk


tn = 0
score={}
l=[]
v = 'aeiou'

last='a'
round_init = 0
run=0
wordl = []
z = 0

def game():
    global word, v, last, round_init, run, wordl, r, z, n, frame
    z = 0

    word = textbox.get("1.0",'end-1c')
    textbox.delete("1.0",'end-1c')
    if word.isalpha():


        if word.startswith(last):


            if word not in wordl:
                wordl.append(word)

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
                strt = tk.Label(master=frame,text='\n\nnext player '+l[r]+ ' enter a word that starts with '+ last, font=('Berlin Sans FB',30))
                strt.pack(padx=20, pady=25)
                frame.place()
                #frame.after(100,update)

                run += 1
            else:
                print(Fore.RED + 'player',l[r],'loses ten points because',word,'has already been input please enter a word that has not already been used')
                score[l[r]] -= 10
        else:
            print(Fore.RED + 'player',l[r],'loses ten points because',word,'does not start with', last, 'please enter a word that starts with',last)
            score[l[r]] -= 10
    else :
        print(Fore.RED + 'please dont input anything other than alphabet')



def retrieve_word():
    global word
    word = textbox.get("1.0",'end-1c')
    textbox.delete("1.0",'end-1c')
    game_starts.after(100,close_game_starts)

def retrieve_round_number():
    global rounds_no
    rounds_no = textbox.get("1.0",'end-1c')
    print(Fore.YELLOW + 'number of rounds : ', rounds_no)
    round_number.after(100,close_round_number)

def retrieve_input_name():
    global name
    name = textbox.get("1.0",'end-1c')
    player_name.after(100,close_player_name)

def close_score_window():
    score_window.destroy()

def close_game_starts():
    game_starts.destroy()

def close_round_number():
    round_number.destroy()

def close_player_name():
    player_name.destroy()

def close_player_no():
    player_no.destroy()

def btn1_cmd():
    global n
    n = 2
    player_no.after(100, close_player_no)
    print(Fore.GREEN + 'number of players: ',n)

def btn2_cmd():
    global n
    n = 3
    player_no.after(100, close_player_no)
    print(Fore.GREEN + 'number of players: ',n)

def btn3_cmd():
    global n
    n = 4
    player_no.after(100, close_player_no)
    print(Fore.GREEN + 'number of players: ',n)

def btn4_cmd():
    global n
    n = 5
    player_no.after(100, close_player_no)
    print(Fore.GREEN + 'number of players: ',n)

player_no = tk.Tk()
player_no.geometry('600x600')
player_no.title('WORD GAME - by idris')
strt = tk.Label(master=player_no, text='how many people are playing?', font=('Berlin Sans FB',30))
strt.pack(padx=20, pady=25)

#textbox = tk.Text(player_no, height=1, font=('Arial',16))
#textbox.pack()

buttonframe = tk.Frame(player_no)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)

btn1= tk.Button(buttonframe, text='2', font=('Arial',18), command=btn1_cmd)
btn1.grid(row=0, column=0, sticky='news')

btn2= tk.Button(buttonframe, text='3', font=('Arial',18), command=btn2_cmd)
btn2.grid(row=0, column=1, sticky='news')

#btn3= tk.Button(buttonframe, text='4', font=('Arial',18))
#btn3.grid(row=0, column=2, sticky='news')

btn3= tk.Button(buttonframe, text='4', font=('Arial',18), command=btn3_cmd)
btn3.grid(row=1, column=0, sticky='news')

btn4= tk.Button(buttonframe, text='5', font=('Arial',18), command=btn4_cmd)
btn4.grid(row=1, column=1, sticky='news')

#btn6= tk.Button(buttonframe, text='7', font=('Arial',18))
#btn6.grid(row=1, column=2, sticky='news')

buttonframe.pack(fill='x')

player_no.mainloop()

while True:
    player_name = tk.Tk()
    player_name.geometry('600x600')
    player_name.title('WORD GAME - by idris')
    strt = tk.Label(master=player_name,text='enter player '+ str(tn+1) +' name', font=('Berlin Sans FB',30))
    strt.pack(padx=20, pady=25)

    textbox = tk.Text(player_name,height=1,font=('Arial',16))
    textbox.pack(padx=10,pady=10)

    btn = tk.Button(player_name, text='enter',font=('Arial', 18),command=retrieve_input_name)
    btn.pack(padx=10, pady=10)
    player_name.mainloop()
#    time.sleep(2)
#    print('l')
    if name in l:
        print(Fore.RED + '\n\nname has already been entered please use a different name\n')
        continue
    tn += 1
    score[name]=0
    l.append(name)
    print(Fore.GREEN + 'player',tn,'is',name)
    if n == tn:
        break

round_number = tk.Tk()
round_number.geometry('600x600')
round_number.title('WORD GAME - by idris')
strt = tk.Label(master=round_number,text='enter how many rounds: ', font=('Berlin Sans FB',30))
strt.pack(padx=20, pady=25)

textbox = tk.Text(round_number,height=1,font=('Arial',16))
textbox.pack(padx=10,pady=10)

btn = tk.Button(round_number, text='enter',font=('Arial', 18),command=retrieve_round_number)
btn.pack(padx=10, pady=10)
round_number.mainloop()


game_starts = tk.Tk()
game_starts.geometry('1200x600')
game_starts.title('WORD GAME - by idris')

r = random.randint(1,n) - 1
frame = tk.Frame(game_starts)


strt = tk.Label(master=frame,text=l[r]+' starts\n\nfirst player ' +l[r]+ ' enter a word that starts with '+last, font=('Berlin Sans FB',30))
strt.pack(padx=20, pady=25)

btn = tk.Button(frame, text='enter',font=('Arial', 18),command=game)
btn.pack(padx=10, pady=10)

strt = tk.Label(master=frame,text=l[r]+ ' enter word: ', font=('Berlin Sans FB',30))
strt.pack(padx=20, pady=25)

textbox = tk.Text(frame,height=1,font=('Arial',16))
textbox.pack(padx=10,pady=10)

frame.pack()

game_starts.mainloop()
'''

game_starts = tk.Tk()
game_starts.geometry('1200x600')
game_starts.title('WORD GAME - by idris')
'''

while True:
    z = 0

#    btn = tk.Button(game_starts, text='enter',font=('Arial', 18),command=game)
#    btn.pack(padx=10, pady=10)

    if run == n:
        run = 0
        round_init += 1
        if int(round_init) == int(rounds_no):
            print(Fore.YELLOW + 'all rounds have finished')
            game_starts.after(100,close_game_starts)
            break
    frame = tk.Frame(game_starts)
    strt = tk.Label(master=frame,text='\n\nnext player '+l[r]+ ' enter a word that starts with '+ last, font=('Berlin Sans FB',30))
    strt.pack(padx=20, pady=25)

    strt1 = tk.Label(master=frame,text=l[r]+' enter word: ', font=('Berlin Sans FB',30))
    strt1.pack(padx=20, pady=25)

    textbox = tk.Text(frame,height=1,font=('Arial',16))
    textbox.pack(padx=10,pady=10)

    btn = tk.Button(frame, text='enter',font=('Arial', 18),command=game)
    btn.pack(padx=10, pady=10)

    frame.place()

game_starts.mainloop()


score_window = tk.Tk()
score_window.geometry('800x600')
score_window.title('WORD GAME - by idris')

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

strt = tk.Label(master=score_window,text='winner is '+win+' with '+str(max)+' points \n \n CONGRATS!!', font=('Berlin Sans FB',30))
strt.pack(padx=20, pady=25)

strt1 = tk.Label(master=score_window,text='\nloser is '+lose+' with a total of '+str(min)+' points\n\n sed lyfe', font=('Berlin Sans FB',30))
strt1.pack(padx=20, pady=25)

btn = tk.Button(score_window, text='close',font=('Arial', 18),command=close_score_window)
btn.pack(padx=10, pady=10)


print(Fore.GREEN + '\n\nwinner is',win,'with',max,'points')

print(Fore.RED + '\n\nloser is',lose,'with a total of',min,'points')

print(Fore.WHITE + '')

score_window.mainloop()
