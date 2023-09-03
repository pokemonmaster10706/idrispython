#import tkinter as tk
import pwinput
import customtkinter as ctk
from customtkinter import *    #importing all libraries as part of python itself(no longer need to call customtkinter)
from PIL import ImageTk, Image
from colorama import Fore
import mysql.connector as msconn
import re

set_appearance_mode('dark')#can be changed to light
set_default_color_theme('green')#can also be blue or dark-blue

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def test():
    pass

#----------------------------------------------------↓↓↓↓↓database checking/creation function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def check_database():
    global sqlcon

    cur = sqldb.cursor()
    cur.execute('show databases')
    db = cur.fetchall()
    dbs = []

    for i in db:
        dbs.append(i[0].lower())

    if 'hospital' not in dbs:
        cur.execute('create database Hospital')
        sqldb.commit()
        cur.close()
        sqldb.close()
        sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = '%s'%(passw,), database = 'Hospital')
        cur2 = sqlcon.cursor()
        cur2.execute('create table Login(username varchar(20) primary key,password varchar(20) not null, phone_number int(10) unique not null, admin char(1) default "n")')
        cur2.execute('create table Staff(Staff_ID int(10) primary key ,Name varchar(30) not null ,Age int(3) ,Gender char(1) not null ,Address varchar(50) not null ,Category varchar(30) not null ,Date_Of_Join date not null ,Salary decimal(10,2) Not null )')
        cur2.execute('create table Doctors(ID varchar(15) primary key, Staff_ID int(10) unique not null, Department varchar(50) not null, constraint staffkey foreign key(Staff_ID) references staff(Staff_ID))')
        cur2.execute('create table Rooms(Room_NO int(7) primary key, Type varchar(30) not null, Capacity int(2) not null, Available_Beds int(2) not null, Class varchar(10))')
        cur2.execute('create table Labs(Lab_NO int(7) primary key, Type varchar(20) not null, Available char(1))')
        cur2.execute('create table Appointments(Appt_NO int primary key, Patient_Name varchar(30) not null, Date_Time datetime default now(), Doc_ID varchar(15) not null, Insurance varchar(50), constraint dockey foreign key(Doc_ID) references Doctors(ID))')
        cur2.execute('create table Patients(ID int primary key, Name varchar(30) not null, Appt_NO int, Doc_ID varchar(15), constraint apptkey foreign key(Appt_NO) references appointments(Appt_NO), constraint docidkey foreign key(Doc_ID) references Doctors(ID))')
        cur2.execute('create table Inpatient(slno int primary key auto_increment ,Patient_ID int, Room_NO int(7), Lab_NO int(7), admition_date datetime default now(), discharge datetime not null , constraint patkey foreign key(Patient_id) references patients(id), constraint roomkey foreign key(room_no) references rooms(room_no), constraint labkey foreign key (lab_no) references labs(lab_no))')
        cur2.execute('create table Outpatients(slno int primary key auto_increment ,Patient_ID int, Lab_NO int(7), constraint patkey2 foreign key(Patient_id) references patients(id), constraint labkey2 foreign key (lab_no) references labs(lab_no))')
        cur2.execute('create table Bills(slno int primary key auto_increment ,Patient_ID int,moneytemp int,totaltemp int, constraint patkey3 foreign key(Patient_id) references patients(id))')
        sqlcon.commit()
        cur2.close()

    else:
        cur.close()
        sqldb.close()
        sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = '%s'%(passw,), database = 'Hospital')

#----------------------------------------------------↓↓↓↓↓password checking function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def password(passentry,repassentry,frame,yaxis,xaxis = 45):
    global passwrd_check, pass_error_label, paswrd

    paswrd = passentry.get()
    repas = repassentry.get()

    passwrd_check = False

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
        passwrd_check = True
        pass_error_label.destroy()
        pass_error_label=CTkLabel(master=frame, text="Password accepted", font=('Dubai', 12), text_color='Green', height=1)
        pass_error_label.place(x=xaxis,y=yaxis)


    else:

        if length_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=frame, text="Invalid password. Must have 8 or more characters", font=('Dubai', 12), text_color='Red', height=1)

        elif upper_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=frame, text="Invalid password. Must include an upper case letter", font=('Dubai', 12), text_color='Red', height=1)

        elif nmbr_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=frame, text="Invalid password. Must include a number", font=('Dubai', 12), text_color='Red', height=1)

        elif spl_check is False:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=frame, text="Invalid password. Must include a special character", font=('Dubai', 12), text_color='Red', height=1)

        elif paswrd != repas:
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=frame, text="Passwords do not match", font=('Dubai', 12), text_color='Red', height=1)

        pass_error_label.place(x=xaxis,y=yaxis)


#----------------------------------------------------↓↓↓↓↓signup button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def adsignup_button():
    global pass_error_label, user_error_label, mob_error_label, passwrd_check


    username = userentry.get()
    signup_cur = sqlcon.cursor()

    signup_cur.execute('select * from login where username = "%s"'%(username))
    user_exist = signup_cur.fetchall()

    if user_exist == []:

        user_check = False
        mob_check = False

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
                user_error_label=CTkLabel(master=adminsignframe, text="Invalid username. Must have 8 or more characters", font=('Dubai', 12), text_color='Red', height=1)

            elif upper_check is False:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=adminsignframe, text="Invalid username. Must include an upper case letter", font=('Dubai', 12), text_color='Red', height=1)

            elif nmbr_check is False:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=adminsignframe, text="Invalid username. Must include a number", font=('Dubai', 12), text_color='Red', height=1)

            elif spl_check is False:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=adminsignframe, text="Invalid username. Must include a special character", font=('Dubai', 12), text_color='Red', height=1)

            elif ' ' in username:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=adminsignframe, text="Username cannot contain spaces", font=('Dubai', 12), text_color='Red', height=1)

            user_error_label.place(x=45,y=98)

        if user_check is True:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=adminsignframe, text="Username accepted.", font=('Dubai', 12), text_color='Green', height=1)
            user_check = True

        user_error_label.place(x=45,y=98)

        password(passentry,repassentry,adminsignframe,200)

        mob_no = phone_entry.get()
        length_check = False
        nmbr_check = False

        if len(str(mob_no)) != 10:
            mob_error_label.destroy()
            mob_error_label=CTkLabel(master=adminsignframe, text="Phone number not valid, Please recheck", font=('Dubai', 12), text_color='Red', height=1)

        else:
            length_check = True
            for i in mob_no:
                if i.isdigit() == False:
                    mob_error_label.destroy()
                    mob_error_label=CTkLabel(master=adminsignframe, text="Phone number can only contain numbers", font=('Dubai', 12), text_color='Red', height=1)
                else:
                    nmbr_check = True

        if length_check == nmbr_check is True:
            mob_check = True

        mob_error_label.place(x=45,y=260)



        if passwrd_check == user_check == mob_check is True:
            signup_cur.execute("insert into login values('%s','%s',%s,'y')"%(username,paswrd,mob_no))
            sqlcon.commit()
            signup_cur.close()
            log.destroy()
            adminlog()

    else:
        user_error_label.destroy()
        user_error_label=CTkLabel(master=adminsignframe, text="Sorry, This username is already in use.", font=('Dubai', 12), text_color='Red', height=1)
        user_error_label.place(x=45,y=98)


#----------------------------------------------------↓↓↓↓↓signup button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------


def signup_button(xpass,xuser,xmob,xeid):
    global pass_error_label, user_error_label, mob_error_label, EID_error_label, passwrd_check


    username = userentry.get()
    signup_cur = sqlcon.cursor()

    signup_cur.execute('select * from login where username = "%s"'%(username))
    user_exist = signup_cur.fetchall()

    if user_exist == []:

        user_check = False
        mob_check = False

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
                user_error_label=CTkLabel(master=signframe, text="Invalid username. Must have 8 or more characters", font=('Dubai', 12), text_color='Red', height=1)

            elif upper_check is False:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=signframe, text="Invalid username. Must include an upper case letter", font=('Dubai', 12), text_color='Red', height=1)

            elif nmbr_check is False:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=signframe, text="Invalid username. Must include a number", font=('Dubai', 12), text_color='Red', height=1)

            elif spl_check is False:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=signframe, text="Invalid username. Must include a special character", font=('Dubai', 12), text_color='Red', height=1)

            elif ' ' in username:
                user_error_label.destroy()
                user_error_label=CTkLabel(master=signframe, text="Username cannot contain spaces", font=('Dubai', 12), text_color='Red', height=1)

            user_error_label.place(x=45,y=xuser)

        if user_check is True:
            user_error_label.destroy()
            user_error_label=CTkLabel(master=signframe, text="Username accepted.", font=('Dubai', 12), text_color='Green', height=1)
            user_check = True

        user_error_label.place(x=45,y=xuser)

        password(passentry,repassentry,signframe,xpass)

        mob_no = phone_entry.get()
        length_check = False
        nmbr_check = False

        if len(str(mob_no)) != 10:
            mob_error_label.destroy()
            mob_error_label=CTkLabel(master=signframe, text="Phone number not valid, Please recheck", font=('Dubai', 12), text_color='Red', height=1)

        else:
            length_check = True
            for i in mob_no:
                if i.isdigit() == False:
                    mob_error_label.destroy()
                    mob_error_label=CTkLabel(master=signframe, text="Phone number can only contain numbers", font=('Dubai', 12), text_color='Red', height=1)
                else:
                    mob_error_label.destroy()
                    mob_error_label=CTkLabel(master=signframe, text="Phone number accepted", font=('Dubai', 12), text_color='Green', height=1)
                    nmbr_check = True

        if length_check == nmbr_check is True:
            mob_check = True

        mob_error_label.place(x=45,y=xmob)

        emirates_id = EID_entry.get()
        pattern = re.compile(r'^\d{3}-?\d{4}-?\d{7}-?\d$')

        EID_check = False
        signup_cur.execute('select * from login where Emirates_ID = "%s"'%(emirates_id))
        EID_exists = signup_cur.fetchall()

        if pattern.match(emirates_id) and emirates_id[0:3] == '784':

            if EID_exists == []:
                EID_error_label.destroy()
                EID_error_label=CTkLabel(master=signframe, text="Emirates ID accepted", font=('Dubai', 12), text_color='Green', height=1)
                EID_check = True
                EID_error_label.place(x=45,y=xeid)

            else:
                EID_error_label.destroy()
                EID_error_label=CTkLabel(master=signframe, text="Emirates ID already registered", font=('Dubai', 12), text_color='Red', height=1)
                EID_error_label.place(x=45,y=xeid)

        else:
            EID_error_label.destroy()
            EID_error_label=CTkLabel(master=signframe, text="Emirates ID Invalid", font=('Dubai', 12), text_color='Red', height=1)
            EID_error_label.place(x=45,y=xeid)

        if passwrd_check == user_check == mob_check == EID_check is True:
            signup_cur.execute("insert into login values('%s','%s','%s',%s,'n')"%(emirates_id,username,paswrd,mob_no))
            sqlcon.commit()
            signup_cur.close()
            log.destroy()
            login_win()

    else:
        user_error_label.destroy()
        user_error_label=CTkLabel(master=signframe, text="Sorry, This username is already in use.", font=('Dubai', 12), text_color='Red', height=1)
        user_error_label.place(x=45,y=xuser)

#----------------------------------------------------↓↓↓↓↓admin login button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def adlogin_button():
    global user_error_label, pass_error_label

    username = userentry.get()
    paswrd = passentry.get()


    log_cur = sqlcon.cursor()
    log_cur.execute('select * from login where username = "%s"'%(username))
    user_pass = log_cur.fetchall()

#    print(user_pass)      #for debugging

    if user_pass != []:

        if user_pass[0][1] == paswrd:
            if user_pass[0][3] == 'y':
                user_error_label.destroy()
                pass_error_label.destroy()
                enter_label=CTkLabel(master=adminlogframe, text="Welcome", font=('Dubai', 12), text_color='Lime')
                enter_label.place(x=45,y=137)
                log.after(1000,log.destroy())
                ad_home_page()
            else:
                user_error_label.destroy()
                pass_error_label.destroy()
                pass_error_label=CTkLabel(master=adminlogframe, text="Not an admin account", font=('Dubai', 12), text_color='Red', height=1)
                pass_error_label.place(x=45,y=193)


        else:
            user_error_label.destroy()
            pass_error_label.destroy()
            pass_error_label=CTkLabel(master=adminlogframe, text="Incorrect password", font=('Dubai', 12), text_color='Red', height=1)
            pass_error_label.place(x=45,y=193)

    else:
        pass_error_label.destroy()
        user_error_label.destroy()
        user_error_label=CTkLabel(master=adminlogframe, text="Account does not exist", font=('Dubai', 12), text_color='Red', height=1)
        user_error_label.place(x=45,y=137)


#----------------------------------------------------↓↓↓↓↓login button function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def login_button():
    global user_error_label, pass_error_label

    username = userentry.get()
    paswrd = passentry.get()

    if username == 'Admin.user' and paswrd == 'Admin.pass':
        adminlog()


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
            pass_error_label=CTkLabel(master=logframe, text="Incorrect password", font=('Dubai', 12), text_color='Red', height=1)
            pass_error_label.place(x=45,y=193)

    else:
        pass_error_label.destroy()
        user_error_label.destroy()
        user_error_label=CTkLabel(master=logframe, text="Account does not exist", font=('Dubai', 12), text_color='Red', height=1)
        user_error_label.place(x=45,y=137)

#----------------------------------------------------↓↓↓↓↓change password function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def chngpass():
    global mobentry, passentry, repassentry, mob_error_label, frgtframe, user_error_label, pass_error_label

    mob = mobentry.get()
    if mob.isdigit():
        if len(mob)==10:
            mobcur = sqlcon.cursor()
            mobcur.execute('select * from login where phone_number = %s'%(mob))
            acc = mobcur.fetchall()

            if acc == []:
                mob_error_label.destroy()
                mob_error_label=CTkLabel(master=frgtframe, text="Mobile number not registered", font=('Dubai', 12), text_color='Red', height=1)
                mob_error_label.place(x=45,y=130)

            else:
                mob_error_label.destroy()
                mob_error_label=CTkLabel(master=frgtframe, text="Mobile number accepted", font=('Dubai', 12), text_color='Green', height=1)
                mob_error_label.place(x=45,y=130)

                username = userentry.get()
                if acc[0][0] == username:
                    user_error_label.destroy()
                    user_error_label=CTkLabel(master=frgtframe, text="Username accepted", font=('Dubai', 12), text_color='Green', height=1)
                    user_error_label.place(x=45,y=180)

                    password(passentry,repassentry,frgtframe,257)
                    if passwrd_check is True:
                        print(Fore.WHITE + paswrd)
                        mobcur.execute('update login set password = "%s" where phone_number = "%s"'%(paswrd,mob))
                        sqlcon.commit()
                        mobcur.close()
                        switchlog()

                else:
                    user_error_label.destroy()
                    user_error_label=CTkLabel(master=frgtframe, text="Username not registered with this number", font=('Dubai', 12), text_color='Red', height=1)
                    user_error_label.place(x=45,y=180)
    else:
        mob_error_label.destroy()
        mob_error_label=CTkLabel(master=frgtframe, text="Mobile number not valid", font=('Dubai', 12), text_color='Green', height=1)
        mob_error_label.place(x=45,y=130)

#----------------------------------------------------↓↓↓↓↓login / signup window creation↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------


def login_win():
    global log , logbg, logframe, adminlogframe, pass_error_label, user_error_label, mob_error_label, mobentry, passentry, repassentry, switchlog, switchsignup, switchfrgt, adminlog

    #----------------------------------------------------↓↓↓↓↓admin login frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def adminlog():
        global userentry, passentry, adminlogframe, pass_error_label, user_error_label

        adminlogframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        adminlogframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        loglabel=CTkLabel(master=adminlogframe, text="Admin login", font=('Dubai', 20))
        loglabel.place(x=50,y=45)

        userentry=CTkEntry (master=adminlogframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=110)

        passentry=CTkEntry (master=adminlogframe, width=220, placeholder_text="Password")
        passentry.place(x=50, y=165)

        frgtpasbutton=CTkButton (master=adminlogframe, text="Not an admin?", width=100, height=20, corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchlog())
        frgtpasbutton.place(x=170,y=195)

        pass_error_label=CTkLabel(master=adminlogframe, text="")
        pass_error_label.place(x=45,y=192)

        user_error_label=CTkLabel(master=adminlogframe, text="")
        user_error_label.place(x=45,y=135)

        logbutton=CTkButton(master=adminlogframe, width=220, text='Login', corner_radius=6, command=lambda:adlogin_button())
        logbutton.place(x=50,y=240)

#        googlelogo=CTkImage(Image.open("google.png").resize((20,20), Image.Resampling.LANCZOS))
#        fblogo=CTkImage(Image.open("facebook.png").resize((20,20), Image.Resampling.LANCZOS))
#
#        googlebutton=CTkButton(master=adminlogframe, image=googlelogo, text="Google", width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='White', hover_color='#A4A4A4')
#        googlebutton.place(x=50,y=290)
#
#        fbbutton=CTkButton(master=adminlogframe, image=fblogo, text="Facebook", width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='White', hover_color='#A4A4A4')
#        fbbutton.place(x=170,y=290)
#
        switchbutton=CTkButton(master=adminlogframe, width=220, text="Create admin account", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:adminsignup())
        switchbutton.place(x=50,y=320)

    #----------------------------------------------------↓↓↓↓↓signup frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def adminsignup():
        global repassentry, passentry, userentry, adminsignframe, pass_error_label, user_error_label, phone_entry, mob_error_label

        log.title('ADMIN SIGNUP')

        adminsignframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        adminsignframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        signlabel=CTkLabel(master=adminsignframe, text="Admin signup", font=('Dubai', 20))
        signlabel.place(x=50,y=20)

        userentry=CTkEntry (master=adminsignframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=70)

        passentry=CTkEntry (master=adminsignframe, width=220, placeholder_text="Password")
        passentry.place(x=50, y=130)

        repassentry=CTkEntry (master=adminsignframe, width=220, placeholder_text="Repeat Password")
        repassentry.place(x=50, y=165)

        phone_entry=CTkEntry (master=adminsignframe, width=220, placeholder_text="Phone Number")
        phone_entry.place(x=50, y=230)

        user_error_label=CTkLabel(master=adminsignframe, text="")
        user_error_label.place(x=45,y=88)

        pass_error_label=CTkLabel(master=adminsignframe, text="")
        pass_error_label.place(x=45,y=190)

        mob_error_label=CTkLabel(master=adminsignframe, text="")
        mob_error_label.place(x=45,y=128)

        signbutton=CTkButton(master=adminsignframe, width=220, text='Sign up', corner_radius=6, command=lambda:adsignup_button())
        signbutton.place(x=50,y=280)

        switchbutton=CTkButton(master=adminsignframe, width=220, text="Login as admin", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:adminlog())
        switchbutton.place(x=50,y=320)


    #----------------------------------------------------↓↓↓↓↓forgot password frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def switchfrgt():
        global userentry, passentry, repassentry, logframe, frgtframe, mobentry, pass_error_label, user_error_label, mob_error_label

        frgtframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        frgtframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        frgtlabel=CTkLabel(master=frgtframe, text="Change your password", font=('Dubai', 20))
        frgtlabel.place(x=50,y=45)

        mobentry=CTkEntry (master=frgtframe, width=220, placeholder_text="Mobile number")
        mobentry.place(x=50, y=100)

        userentry=CTkEntry (master=frgtframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=150)

        passentry=CTkEntry (master=frgtframe, width=220, placeholder_text="New password")
        passentry.place(x=50, y=200)

        repassentry=CTkEntry (master=frgtframe, width=220, placeholder_text="Repeat password")
        repassentry.place(x=50, y=230)

        user_error_label=CTkLabel(master=frgtframe, text="")
        user_error_label.place(x=45,y=135)

        pass_error_label=CTkLabel(master=frgtframe, text="")
        pass_error_label.place(x=45,y=192)

        mob_error_label=CTkLabel(master=frgtframe, text="")
        mob_error_label.place(x=45,y=230)

        chngbutton=CTkButton(master=frgtframe, width=220, text='Change password', corner_radius=6, command=lambda:chngpass())
        chngbutton.place(x=50,y=280)

        switchbutton=CTkButton(master=frgtframe, width=100, text="← back to login page", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchlog())
        switchbutton.place(x=50,y=320)


    #----------------------------------------------------↓↓↓↓↓login frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def switchlog():
        global userentry, passentry, logframe, pass_error_label, user_error_label

        log.title('LOGIN')

        logframe = CTkFrame(master=logbg, width=320, height=360, corner_radius=15)
        logframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        loglabel=CTkLabel(master=logframe, text="Log into your Account", font=('Dubai', 20))
        loglabel.place(x=50,y=45)

        userentry=CTkEntry (master=logframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=110)

        passentry=CTkEntry (master=logframe, width=220, placeholder_text="Password")
        passentry.place(x=50, y=165)

        frgtpasbutton=CTkButton (master=logframe, text="Forgot password?", width=100, height=20, corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchfrgt())
        frgtpasbutton.place(x=165,y=195)

        pass_error_label=CTkLabel(master=logframe, text="")
        pass_error_label.place(x=45,y=192)

        user_error_label=CTkLabel(master=logframe, text="")
        user_error_label.place(x=45,y=135)

        logbutton=CTkButton(master=logframe, width=220, text='Login', corner_radius=6, command=lambda:login_button())
        logbutton.place(x=50,y=240)

#        googlelogo=CTkImage(Image.open("google.png").resize((20,20), Image.Resampling.LANCZOS))
#        fblogo=CTkImage(Image.open("facebook.png").resize((20,20), Image.Resampling.LANCZOS))
#
#        googlebutton=CTkButton(master=logframe, image=googlelogo, text="Google", width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='White', hover_color='#A4A4A4')
#        googlebutton.place(x=50,y=290)
#
#        fbbutton=CTkButton(master=logframe, image=fblogo, text="Facebook", width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='White', hover_color='#A4A4A4')
#        fbbutton.place(x=170,y=290)
#
        switchbutton=CTkButton(master=logframe, width=220, text="Don't have an account? sign up.", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:switchsignup())
        switchbutton.place(x=50,y=320)

    #----------------------------------------------------↓↓↓↓↓signup frame↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

    def switchsignup():
        global repassentry, passentry, userentry, signframe,EID_entry, EID_error_label, pass_error_label, user_error_label, phone_entry, mob_error_label

        log.title('SIGNUP')

        signframe = CTkFrame(master=logbg, width=320, height=450, corner_radius=15)
        signframe.place(relx=0.5,rely=0.5,anchor=CENTER)

        signlabel=CTkLabel(master=signframe, text="Create new account", font=('Dubai', 20))
        signlabel.place(x=50,y=20)

        userentry=CTkEntry (master=signframe, width=220, placeholder_text="Username")
        userentry.place(x=50, y=70)

        passentry=CTkEntry (master=signframe, width=220, placeholder_text="Password")
        passentry.place(x=50, y=130)

        repassentry=CTkEntry (master=signframe, width=220, placeholder_text="Repeat Password")
        repassentry.place(x=50, y=165)

        phone_entry=CTkEntry (master=signframe, width=220, placeholder_text="Phone Number")
        phone_entry.place(x=50, y=225)

        EID_entry=CTkEntry (master=signframe, width=220, placeholder_text="Emirates ID")
        EID_entry.place(x=50, y=285)

        user_error_label=CTkLabel(master=signframe, text="", height=1)
        user_error_label.place(x=45,y=105)

        pass_error_label=CTkLabel(master=signframe, text="", height=1)
        pass_error_label.place(x=45,y=200)

        mob_error_label=CTkLabel(master=signframe, text="", height=1)
        mob_error_label.place(x=45,y=260)

        EID_error_label=CTkLabel(master=signframe, text="", height=1)
        EID_error_label.place(x=45,y=320)

        testlabel=CTkLabel(master=signframe, text="", height=1)
        testlabel.place(x=45,y=400)

        signbutton=CTkButton(master=signframe, width=220, text='Sign up', corner_radius=6, command=lambda:signup_button(xpass=200,xuser=105,xmob=260,xeid=320))
        signbutton.place(x=50,y=350)

        def del_frame():
            signframe.destroy()
            switchlog()

        switchbutton=CTkButton(master=signframe, width=220, text="Already have an account? Login.", corner_radius=6, compound='right', fg_color='#2b2b2b', hover_color='#2b2b2b', command=lambda:del_frame())
        switchbutton.place(x=50,y=410)

    #--------------------------------------------------↓↓↓↓↓creating the login window↓↓↓↓↓-------------------------------------------------------

    log = CTk()
    log.geometry('640x675')
    log.title('LOGIN')

    logimg = ImageTk.PhotoImage(Image.open('pxfuel.jpg'))
    logbg = CTkLabel(master=log, image=logimg)
    logbg.pack()


    switchlog()

    log.mainloop()

    '''    def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    center_window(log)'''
#--------------------------------------------------↓↓↓↓↓creating the home page↓↓↓↓↓-------------------------------------------------------

def detailspage():
    detail_win = CTk()
    detail_win.geometry('1280x720')
    detail_win.title('Python Hospital')

    detailimg = ImageTk.PhotoImage(Image.open('home-bg.jpg'))
    detailbg = CTkLabel(master=detail_win, image=detailimg)
    detailbg.pack()

    detailframe = CTkFrame(master=detailbg, width=750, height=790, corner_radius=15)
    detailframe.place(relx=0.5,rely=0.5,anchor=CENTER)



    detail_win.mainloop()


#--------------------------------------------------↓↓↓↓↓creating the home page↓↓↓↓↓-------------------------------------------------------

def home_page():
    home_win = CTk()
    home_win.geometry('1280x800')
    home_win.title('Python Hospital')

    home_win.eval('tk::PlaceWindow . center')

    homeimg = ImageTk.PhotoImage(Image.open('home-bg.jpg'))
    homebg = CTkLabel(master=home_win, image=homeimg)
    homebg.pack()

    homeframe = CTkFrame(master=homebg, width=750, height=790, corner_radius=15)
    homeframe.place(relx=0.5,rely=0.5,anchor=CENTER)


    home_win.mainloop()

#----------------------------------------------------↓↓↓↓↓main function↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

def main():
    pass


#----------------------------------------------------↓↓↓↓↓code activation↓↓↓↓↓---------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    global passw
    passw = 'idris7'
#    passw = pwinput.pwinput()
#    passw = input('Enter Password: ')
#    print('\b'*(len(passw)+1))
    sqldb = msconn.connect(host = 'localhost', user = 'root', passwd = '%s'%(passw,))

    check_database()
    login_win()
    main()

    sqlcon.close()
