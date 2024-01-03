from customtkinter import *
from PIL import Image,ImageTk
import mysql.connector as msconn

username = 'Pillow-123'

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
    tab3 = tabs.add('feedback')
    #tab4 = tabs.add('profile')
    tabs.set('feedback')

    descframe = CTkFrame(master=tab1,height=500,width=360)
    descframe.place(relx=0.25,rely=0.5,anchor='center')

    details = '''                             PYTHON HOSPITAL\n
Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n 
Donec sed urna hendrerit,aliquam diam quis,vulputate erat.\n 
Orci varius natoque penatibus et magnis dis parturient\n
montes, nascetur ridiculus mus. Donec hendrerit lorem et\n
vestibulum interdum.Aliquam porta maximus sem.Sed viverra,\n
ante ut gravida pretium, augue sapien viverra lectus,non\n
cursus lectus nibh in dui. Cras mauris mi, congue non \n
orci et,blandit commodo,nisi.Suspendisse sed bibendum dui.\n
Quisque quis lectus eget nulla semper facilisis vitae \n
sit amet ante. Aliquam sit amet imperdiet risus, in \n
auctor nibh. Proin vitae nulla mi. Maecenas nisi mauris,\n
volutpat vitae tortor at, fermentum lobortis metus.\n
Praesent eget volutpat est, sit amet mattis mauris.\n
Nullacommodo lorem acurnadictum,sit amet aliqut porta.\n
Nam odio lectus,tristique at a,ultrices sit amet nisi.\n
Ut feugiat nunc nec eros ultrices aliquet.'''

    picframe = CTkFrame(master=tab1,height=500,width=360)
    picframe.place(relx=0.75,rely=0.5,anchor='center')

    hosimg = CTkImage(Image.open("darkhos.png"),size=(500,500))
    hosbg = CTkLabel(master=picframe,text='', image=hosimg)
    hosbg.place(relx=0.5,rely=0.5,anchor='center')

    desclabel = CTkLabel(master=descframe, text=details, font=('Dubai', 14), height = 0,justify = 'left')
    desclabel.place(x=15,y=0)

    feedlabel = CTkLabel(master=tab3, text='We value your feedback. \nPlease tell us what you think!!', font=('Dubai', 50), height = 0)
    feedlabel.place(x=20,y=20)

    feedbox=CTkTextbox (master=tab3, width=700, height = 300, font=('Dubai', 20))
    feedbox.place(x=20, y=250)

    def feedback():
        feed = feedbox.get('0.0','end')
        feedcur = sqlcon.cursor()
        print(len(feed))
        if len(feed)>1:
            feedcur.execute(f'insert into feedback values("{username}","{feed.strip()}")')
            sqlcon.commit()
            feedbox.delete('0.0','end')

    submitbut = CTkButton(master=tab3,text='submit!', font=('Dubai', 18),command=lambda:feedback())
    submitbut.place(relx=0.4,y=600)

    booklabel = CTkLabel(master=tab2, text="Book your appointment.", font=('Dubai', 20), height = 0)
    booklabel.pack(pady=50)

    catframe = CTkScrollableFrame(master=tab2,height=500,width=400,fg_color = '#333333')
    catframe.place(relx=0.5,rely=0.5,anchor='center')

    docicon=CTkImage(Image.open("docicon.jpg").resize((20,20), Image.Resampling.LANCZOS))
    button_dict = {}

    home_cur=sqlcon.cursor()
    home_cur.execute('select * from specialisations')

    spl = home_cur.fetchall()

    def spl_fn(spl_var):
        bgdocframe = CTkFrame(master=tab2,height=500,width=400)
        bgdocframe.place(relx=0.5,rely=0.5,anchor='center')
        docframe = CTkScrollableFrame(master=bgdocframe,height=500,width=400)
        docframe.pack()
        def _bak():
            bgdocframe.destroy()
            back_cat.destroy()

        back_cat = CTkButton(tab2,text = 'bak',command = lambda:_bak())
        back_cat.place(relx=0.1,rely=0.1)

        home_cur=sqlcon.cursor()
        home_cur.execute(f'select * from doctors where specialisation = "{spl_var[0]}"')

        def doctors(doc_var):
            bgtimeframe = CTkFrame(master=tab2,height=500,width=400)
            bgtimeframe.place(relx=0.5,rely=0.5,anchor='center')
            timeframe = CTkScrollableFrame(master=bgtimeframe,height=500,width=400)
            timeframe.place(relx=0.5,rely=0.5,anchor='center')

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
                apptframe.place(relx=0.5,rely=0.5,anchor='center')

                apptlabel = CTkLabel(master=apptframe, text=f"Appointment for {spl_var[0]} \n with Dr.{doc_var[1]} \nat {time_var}", font=('Dubai', 20), height = 0)
                apptlabel.pack(padx=100,pady=225)
                
                def accepted():
                    accframe = CTkFrame(master=tab2,height=520,width=425,fg_color = '#333333')
                    accframe.place(relx=0.5,rely=0.5,anchor='center')

                    acclabel = CTkLabel(master=accframe, text="Appointment confirmed !", font=('Dubai', 20), height = 0)
                    acclabel.pack(padx=100,pady=225)

                    def _bak():
                        accframe.destroy()
                        back_cat.destroy()

                    back_cat = CTkButton(tab2,text = 'bak',command = lambda:_bak())
                    back_cat.place(relx=0.1,rely=0.1)
                
                def appt():
                    home_cur.execute(f'update timings set {time_var} = "n" where doc_id = "{doc_var[0]}"')
                    sqlcon.commit()
                    accepted()
                    
                appt_button = CTkButton(apptframe,text = 'confirm appointment',command = lambda:appt())
                appt_button.place(relx=0.63,rely=0.9)

                def _bak():
                    apptframe.destroy()
                    back_cat.destroy()

                back_cat = CTkButton(tab2,text = 'bak',command = lambda:_bak())
                back_cat.place(relx=0.1,rely=0.1)


            for i in range(1,len(time)):
                if time[i] == 'y':
                    button_dict[i] = CTkButton(timeframe,image=docicon,width=380, text = str(5+i)+'AM',compound='left',anchor='w',command = lambda item =str(5+i)+'AM':doc_time(item))
                    button_dict[i].pack(pady=10)
                else:
                    button_dict[i] = CTkButton(timeframe,image=docicon,width=380, text = str(5+i)+'AM',compound='left',anchor='w',state = 'disabled',command = lambda item =str(5+i)+'AM':doc_time(item))
                    button_dict[i].pack(pady=10)

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
    
    tabs.place(relx=0.5,rely=0.5,anchor='center')
    home_win.mainloop() 
home_page()