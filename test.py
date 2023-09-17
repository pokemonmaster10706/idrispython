from customtkinter import *
from PIL import Image,ImageTk

home_win = CTk()
home_win.geometry("{0}x{1}+0+0".format(home_win.winfo_screenwidth(), home_win.winfo_screenheight()))
home_win.title('Python Hospital')

homeimg = ImageTk.PhotoImage(Image.open('home-bg.png'))
homebg = CTkLabel(master=home_win, image=homeimg)
homebg.pack()

tabs = CTkTabview(master=homebg, width=750, height=790)

tab1 = tabs.add('about us')
tab2 = tabs.add('book an appointment')
tabs.set('book an appointment')

desclabel = CTkLabel(master=tab1, text="test label", font=('Dubai', 14), height = 0)
desclabel.pack(padx=5)

booklabel = CTkLabel(master=tab2, text="What specialisation are you looking for?", font=('Dubai', 20), height = 0)
booklabel.pack(pady=50)

catframe = CTkScrollableFrame(master=tab2,height=500,width=400)
catframe.place(relx=0.5,rely=0.5,anchor=CENTER)


docicon=CTkImage(Image.open("docicon.jpg").resize((20,20), Image.Resampling.LANCZOS))
button_dict = {}
cmd_dict = {}
spl = ['orthopedic       ortho doctor','general       general practician','pediatric       child doctor','test','test2','test3','test4','test4','test4','test4','test4','test4','test4','test4','test4','test4','test4','test4','test4']

def spl_fn(a):
    print(a)


for i in spl:
    button_dict[i] = CTkButton(catframe,image=docicon,width=380, text = i,compound='left',anchor='w',command=lambda item=i:spl_fn(item))
    button_dict[i].pack(pady=10)

tabs.place(relx=0.5,rely=0.5,anchor=CENTER)
home_win.mainloop()
