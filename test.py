from customtkinter import *
from PIL import Image,ImageTk
import mysql.connector as msconn

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'idris7', database = 'Hospital')

#set_appearance_mode('light')

def home_page():
    home_win = CTk()#fg_color='#2179bc')
    home_win.geometry("{0}x{1}+0+0".format(home_win.winfo_screenwidth(), home_win.winfo_screenheight()))
    home_win.title('Python Hospital')

    homeimg = ImageTk.PhotoImage(Image.open('untitled.png'))
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

    def spl_fn(spl_var):
        bgdocframe = CTkFrame(master=tab2,height=500,width=400)
        bgdocframe.place(relx=0.5,rely=0.5,anchor=CENTER)
        docframe = CTkScrollableFrame(master=bgdocframe,height=500,width=400,fg_color = '#333333')
        docframe.pack()
        def _bak():
            #docframe.destroy()
            bgdocframe.destroy()
            back_cat.destroy()

        back_cat = CTkButton(tab2,text = 'bak',command = lambda:_bak())
        back_cat.place(relx=0.1,rely=0.1)

        home_cur=sqlcon.cursor()
        home_cur.execute('select * from doctors where specialisation = "%s"'%(spl_var[0]))

        def doctors(doc_var):
            bgtimeframe = CTkFrame(master=tab2,height=500,width=400)
            bgtimeframe.place(relx=0.5,rely=0.5,anchor=CENTER)
            timeframe = CTkScrollableFrame(master=bgtimeframe,height=500,width=400,fg_color = '#333333')
            timeframe.place(relx=0.5,rely=0.5,anchor=CENTER)

            def _bak():
                bgtimeframe.destroy()
                back_cat.destroy()

            back_cat = CTkButton(tab2,text = 'bak',command = lambda:_bak())
            back_cat.place(relx=0.1,rely=0.1)

            
            home_cur.execute(f'select * from timings where doc_id = "{doc_var[0]}"')
            time=home_cur.fetchone()

            def doc_time(time_var):
                print(time_var)
                apptframe = CTkFrame(master=tab2,height=520,width=425,fg_color = '#333333')
                apptframe.place(relx=0.5,rely=0.5,anchor=CENTER)

                apptlabel = CTkLabel(master=apptframe, text=f"Appointment for {spl_var[0]} \n with Dr.{doc_var[1]} \nat {time_var}", font=('Dubai', 20), height = 0)
                apptlabel.pack(padx=100,pady=225)
                
                def appt():
                    home_cur.execute(f'update timings set {time_var} = "n" where doc_id = "{doc_var[0]}"')
                    home_cur.execute('')
                    sqlcon.commit()
                    
                    

                appt_button = CTkButton(apptframe,text = 'confirm appointment',command = lambda:appt())
                appt_button.place(relx=0.63,rely=0.9)

                def _bak():
                    apptframe.destroy()
                    back_cat.destroy()

                back_cat = CTkButton(tab2,text = 'bak',command = lambda:_bak())
                back_cat.place(relx=0.1,rely=0.1)


            def time_buttons():
                for i in range(1,len(time)):
                    if time[i] == 'y':
                        button_dict[i] = CTkButton(timeframe,image=docicon,width=380, text = str(5+i)+'AM',compound='left',anchor='w',command = lambda item =str(5+i)+'AM':doc_time(item))
                        button_dict[i].pack(pady=10)
            time_buttons()

        doc = home_cur.fetchall()    

        docicon=CTkImage(Image.open("docicon.jpg").resize((20,20), Image.Resampling.LANCZOS))
        button_dict = {}
        for i in range(0,len(doc)):
            button_dict[i] = CTkButton(docframe,image=docicon,width=380, text = doc[i][1],compound='left',anchor='w',command=lambda item=doc[i]:doctors(item))
            print(doc[i])
            button_dict[i].pack(pady=10)

        print(spl_var[0])


    for i in range(0,len(spl)):
        button_dict[i] = CTkButton(catframe,image=docicon,width=380, text = spl[i],compound='left',anchor='w',command=lambda item=spl[i]:spl_fn(item))
        button_dict[i].pack(pady=10)
    

    tabs.place(relx=0.5,rely=0.5,anchor=CENTER)
    home_win.mainloop() 
home_page()