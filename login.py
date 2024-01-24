#import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
from colorama import Fore
import mysql.connector as msconn

set_appearance_mode('dark')#can be changed to light
set_default_color_theme('green')#can also be blue or dark-blue



#--------------------------------------------------↓↓↓↓↓creating the home page↓↓↓↓↓-------------------------------------------------------

def home_page():
    home_win = CTk()
    home_win.geometry('1280x720')
    home_win.title('Welcome')

    homeimg = ImageTk.PhotoImage(Image.open('pxfuel.jpg'))
    homebg = CTkLabel(master=home_win, image=homeimg)
    homebg.pack()

    home_win.mainloop()

#----------------------------------------------------↓↓↓↓↓signup button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def signup_button():
    global pass_error_label, user_error_label


    username = userentry.get()

    pass_check = False
    user_check = False
    space_check = False
    length_check = False
    nmbr_check = False
    upper_check = False

    spl = '`\~!@\#$%^&*()_-+={[:;\\\'\"<>,.?/]}'
    spl_check = False


    if len(username) > 7:
        length_check = True

    for i in username:

        if i.isdigit():
            nmbr_check = True
            continue

        else:

            if i in spl:
                spl_check = True
                continue

            else:

                if i.isupper():
                    upper_check = True
                    continue

                else:
                    continue

    if ' ' in username:
        space_check = False

    else:
        space_check = True

    if length_check == spl_check == nmbr_check == upper_check == space_check == True:
        user_check = True

    else:

        if length_check is False:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=signframe, text="Invalid username. Must have 8 or more characters", font=('Dubai', 12), text_color='Red')

        elif upper_check is False:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=signframe, text="Invalid username. Must include an upper case letter", font=('Dubai', 12), text_color='Red')

        elif nmbr_check is False:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=signframe, text="Invalid username. Must include a number", font=('Dubai', 12), text_color='Red')

        elif spl_check is False:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=signframe, text="Invalid username. Must include a special character", font=('Dubai', 12), text_color='Red')

        elif ' ' in username:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=signframe, text="Username cannot contain spaces", font=('Dubai', 12), text_color='Red')

        user_error_label.place(x=45,y=136)

    if user_check is True:
        user_error_label.destroy()
        user_error_label=CTkLabel(master=signframe, text="Username accepted.", font=('Dubai', 12), text_color='Green')

    user_error_label.place(x=45,y=136)


    paswrd = passentry.get()
    repas = repassentry.get()

    length_check = False
    nmbr_check = False
    upper_check = False

    spl = '`\~!@\#$%^&*()_-+={[:;\\\'\"<>,.?/]}'
    spl_check = False


    if len(paswrd) > 7:
        length_check = True

    for i in paswrd:

        if i.isdigit():
            nmbr_check = True
            continue

        else:

            if i in spl:
                spl_check = True
                continue

            else:

                if i.isupper():
                    upper_check = True
                    continue

                else:
                    continue

    if length_check == spl_check == nmbr_check == upper_check == True and paswrd == repas:
        pass_check = True

    else:

        if length_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=signframe, text="Invalid password. Must have 8 or more characters", font=('Dubai', 12), text_color='Red')

        elif upper_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=signframe, text="Invalid password. Must include an upper case letter", font=('Dubai', 12), text_color='Red')

        elif nmbr_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=signframe, text="Invalid password. Must include a number", font=('Dubai', 12), text_color='Red')

        elif spl_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=signframe, text="Invalid password. Must include a special character", font=('Dubai', 12), text_color='Red')

        elif paswrd != repas:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=signframe, text="Passwords do not match", font=('Dubai', 12), text_color='Red')

        pass_error_label.place(x=45,y=192)

    if pass_check == user_check is True:
        signup_cur = sqlcon.cursor()
        signup_cur.execute("insert into login values('%s','%s')"%(username,paswrd))
        sqlcon.commit()
        signup_cur.close()
        log.destroy()
        login_win()

#----------------------------------------------------↓↓↓↓↓login button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def login_button():
    global user_error_label, pass_error_label

    username = userentry.get()
    paswrd = passentry.get()

    log_cur = sqlcon.cursor()
    log_cur.execute('select * from login where username = "%s"'%(username))
    user_pass = log_cur.fetchall()

#    print(user_pass)      #for debugging

    if user_pass != []:

        if user_pass[0][1] == paswrd:
            user_error_label.destroy()
            pass_error_label.destroy()
            enter_label=CTkLabel(master=logframe, text="Welcome", font=('Dubai', 12), text_color='Lime')
            enter_label.place(x=45,y=137)
            log.after(1000,log.destroy())
            home_page()

        else:
            user_error_label.destroy()
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=logframe, text="Incorrect password", font=('Dubai', 12), text_color='Red')
            pass_error_label.place(x=45,y=192)

    else:
        pass_error_label.destroy()
        user_error_label.destroy()
        user_error_label=CTkLabel(master=logframe, text="Account does not exist", font=('Dubai', 12), text_color='Red')
        user_error_label.place(x=45,y=137)

#----------------------------------------------------↓↓↓↓↓login / signup window creation↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------


def login_win():
    global log , logbg, logframe, pass_error_label, user_error_label

    #----------------------------------------------------↓↓↓↓↓login frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def switchlog():
        global userentry, passentry, logframe, pass_error_label, user_error_label

        logframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        logframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        loglabel=CTkLabel(master=logframe, text="Log into your Account", font=('Dubai', 20))
        loglabel.place(x=50,y=45)

        userentry=CTkEntry (master=logframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=110)

        passentry=CTkEntry (master=logframe, width=220, placeholder_text="Password")
        passentry.place(x=50, y=165)

        frgtpasbutton=CTkButton (master=logframe, text="Forgot password?", width=100, height=20, corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:test())
        frgtpasbutton.place(x=165,y=195)

        pass_error_label=CTkLabel(master=logframe, text="")
        pass_error_label.place(x=45,y=192)

        user_error_label=CTkLabel(master=logframe, text="")
        user_error_label.place(x=45,y=135)

        logbutton=CTkButton(master=logframe, width=220, text='Login', corner_radius=6, command=lambda:login_button())
        logbutton.place(x=50,y=240)

        googlelogo=CTkImage(Image.open("google.png").resize((20,20), Image.Resampling.LANCZOS))
        fblogo=CTkImage(Image.open("facebook.png").resize((20,20), Image.Resampling.LANCZOS))

        googlebutton=CTkButton(master=logframe, image=googlelogo, text="Google", width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='White', hover_color='#A4A4A4')
        googlebutton.place(x=50,y=290)

        fbbutton=CTkButton(master=logframe, image=fblogo, text="Facebook", width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='White', hover_color='#A4A4A4')
        fbbutton.place(x=170,y=290)

        switchbutton=CTkButton(master=logframe, width=220, text="Don't have an account? sign up.", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchsignup())
        switchbutton.place(x=50,y=320)

    #----------------------------------------------------↓↓↓↓↓signup frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def switchsignup():
        global repassentry, passentry, userentry, signframe, pass_error_label,user_error_label

        log.title('SIGNUP')

        signframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        signframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        signlabel=CTkLabel(master=signframe, text="Create new account", font=('Dubai', 20))
        signlabel.place(x=50,y=45)

        userentry=CTkEntry (master=signframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=107)

        passentry=CTkEntry (master=signframe, width=220, placeholder_text="Password")
        passentry.place(x=50, y=164)

        repassentry=CTkEntry (master=signframe, width=220, placeholder_text="Repeat Password")
        repassentry.place(x=50, y=220)

        user_error_label=CTkLabel(master=signframe, text="")
        user_error_label.place(x=45,y=136)

        pass_error_label=CTkLabel(master=signframe, text="")
        pass_error_label.place(x=50,y=192)

        signbutton=CTkButton(master=signframe, width=220, text='Sign up', corner_radius=6, command=lambda:signup_button())
        signbutton.place(x=50,y=260)

        switchbutton=CTkButton(master=signframe, width=220, text="Already have an account? Login.", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchlog())
        switchbutton.place(x=50,y=320)

    #--------------------------------------------------↓↓↓↓↓creating the login window↓↓↓↓↓-------------------------------------------------------

    log = CTk()
    log.geometry('600x440')
    log.title('LOGIN')

    logimg = ImageTk.PhotoImage(Image.open('pxfuel.jpg'))
    logbg = CTkLabel(master=log, image=logimg)
    logbg.pack()

    switchlog()

    log.mainloop()
