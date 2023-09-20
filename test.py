from customtkinter import *
from PIL import Image,ImageTk
import mysql.connector as msconn

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'idris7', database = 'Hospital')

def home_page():
    home_win = CTk()
    home_win.geometry("{0}x{1}+0+0".format(home_win.winfo_screenwidth(), home_win.winfo_screenheight()))
    home_win.title('Python Hospital')

    homeimg = ImageTk.PhotoImage(Image.open('pxfuel.jpg'))
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

    home_cur=sqlcon.cursor()
    home_cur.execute('select * from specialisations')

    spl = home_cur.fetchall()

    def spl_fn(a):
        docframe = CTkScrollableFrame(master=tab2,height=500,width=400)
        docframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        home_cur=sqlcon.cursor()
        home_cur.execute('select * from doctors where specialisation = "%s"'%(a[0]))

        doc = home_cur.fetchall()    

        docicon=CTkImage(Image.open("docicon.jpg").resize((20,20), Image.Resampling.LANCZOS))
        button_dict = {}
        for i in range(0,len(doc)):
            button_dict[i] = CTkButton(docframe,image=docicon,width=380, text = doc[i][1],compound='left',anchor='w')
            button_dict[i].pack(pady=10)

        print(a[0])

    def category():
        for i in range(0,len(spl)):
            button_dict[i] = CTkButton(catframe,image=docicon,width=380, text = spl[i],compound='left',anchor='w',command=lambda item=spl[i]:spl_fn(item))
            button_dict[i].pack(pady=10)
    category()

    tabs.place(relx=0.5,rely=0.5,anchor=CENTER)
    home_win.mainloop() 
home_page()