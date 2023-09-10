from customtkinter import *
from PIL import Image,ImageTk

home_win = CTk()
home_win.geometry("{0}x{1}+0+0".format(home_win.winfo_screenwidth(), home_win.winfo_screenheight()))
home_win.title('Python Hospital')

homeimg = ImageTk.PhotoImage(Image.open('home-bg.png'))
homebg = CTkLabel(master=home_win, image=homeimg)
homebg.pack()

tabs = CTkTabview(master=home_win, width=750, height=790)

tab1 = tabs.add('tab1')
tab2 = tabs.add('tab2')
tabs.set('tab2')


#homeframe = CTkFrame(master=homebg, width=750, height=790, corner_radius=15)
#homeframe.place(relx=0.5,rely=0.5,anchor=CENTER)

tabs.pack(fill=BOTH)

home_win.mainloop()