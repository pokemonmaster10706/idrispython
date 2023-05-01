import random
import tkinter as tk

def close_window():
    root.destroy()

def yes_clicked():
    label = tk.Label(master=root, text="I knew it. :3", font=('Berlin Sans FB',45), width=300, height=300)
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.after(5000, close_window)

def no_clicked():
    x = random.randint(150,260)
    y = random.randint(120,220)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.geometry("300x240")
root.title("Are you Dumb?")

qn = tk.Label(master=root, text="Are you dumb?", font=('Berlin Sans FB',30), width=300, height=150)
qn.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

yes_button = tk.Button(root, text="Yes", height=2, width=7, command=yes_clicked)
yes_button.place(x=75, y=160)

no_button = tk.Button(root, text="No", width=7, height=2,  command=no_clicked)
no_button.place(x=170, y=160)

root.mainloop()
