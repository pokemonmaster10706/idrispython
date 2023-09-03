from customtkinter import *
from PIL import ImageTk, Image



def detailspage():
    detail_win = CTk()
    detail_win.geometry("{0}x{1}+0+0".format(detail_win.winfo_screenwidth(), detail_win.winfo_screenheight()))
    detail_win.title('Python Hospital')

    logimg = ImageTk.PhotoImage(Image.open('1155052.png'))
    logbg = CTkLabel(master=detail_win, image=logimg)
    logbg.pack()

    user = 'test'

    detailframe = CTkFrame(master=logbg, width=750, height=790, corner_radius=15)
    detailframe.place(relx=0.5,rely=0.5,anchor=CENTER)

    detail_label = CTkLabel(master=detailframe, text="Hello "+user, font=('Dubai', 20), height = 1)
    detail_label.place(x=75,y=20)

    detail_label = CTkLabel(master=detailframe, text="\nPlease enter the following details to make easier for you to book an appointment in the future!", font=('Dubai', 20), height = 0)
    detail_label.place(x=75,y=30)

    name_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Full name")
    name_entry.place(x=75, y=90)

    detail_win.mainloop()

detailspage()
