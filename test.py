from customtkinter import *
from PIL import ImageTk, Image

def det_check():
    pass

def detailspage():
    detail_win = CTk()
    detail_win.geometry("{0}x{1}+0+0".format(detail_win.winfo_screenwidth(), detail_win.winfo_screenheight()))
    detail_win.title('Python Hospital')

    logimg = ImageTk.PhotoImage(Image.open('1155052.jpg'))
    logbg = CTkLabel(master=detail_win, image=logimg)
    logbg.pack()

    user = 'test'

    detailframe = CTkFrame(master=logbg, width=650, height=750, corner_radius=15)
    detailframe.place(relx=0.5,rely=0.5,anchor=CENTER)

    detail_label = CTkLabel(master=detailframe, text="Hello "+user+'!!,', font=('Dubai', 18), height = 1)
    detail_label.place(x=30,y=20)

    detail_label = CTkLabel(master=detailframe, text="Please enter the following details to make easier for you to book an appointment in the future!", font=('Dubai', 14), height = 0)
    detail_label.place(x=30,y=45)

    name_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Full name")
    name_entry.place(x=75, y=100)

    Address_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Address")
    Address_entry.place(x=75, y=200)

    insurance_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Insurance")
    insurance_entry.place(x=75, y=300)

    allergy_entry=CTkEntry (master=detailframe, width=400, placeholder_text="Allergies (if any)")
    allergy_entry.place(x=75, y=400)

    switchbutton=CTkButton(master=signframe, width=220, text="proceed ——>", corner_radius=6, compound='right', command=lambda:det_check())
    switchbutton.place(x=50,y=410)

    detail_win.mainloop()

    detailspage()
