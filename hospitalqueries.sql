drop database hospital;
create database hospital;

use hospital;
create table Details(Emirates_ID char(18) primary key,username varchar(20) unique not null,Name varchar(30) not null,address varchar(50) not null, insurance varchar(30) not null,allergies varchar(90))
create table staff(Staff_ID int(10) primary key ,Name varchar(30) not null ,Age int(3) ,Gender char(1) not null ,Address varchar(50) not null ,Category varchar(30) not null ,Date_Of_Join date not null ,Salary decimal(10,2) Not null );
create table Login(Emirates_ID char(18) primary key, username varchar(20) unique not null,password varchar(20) not null, phone_number int(10) unique not null , admin char(1) default "n")
create table Doctors(ID varchar(15) primary key, Staff_ID int(10) unique not null, Department varchar(50) not null, constraint staffkey foreign key(Staff_ID) references staff(Staff_ID));
create table rooms(Room_NO int(7) primary key, Type varchar(30) not null, Capacity int(2) not null, Available_Beds int(2) not null, Class varchar(10));
create table labs(Lab_NO int(7) primary key, Type varchar(20) not null, Available char(1));
create table Appointments(Appt_NO int primary key, Patient_Name varchar(30) not null, Date_Time datetime default now(), Doc_ID varchar(15) not null, Insurance varchar(50), constraint dockey foreign key(Doc_ID) references Doctors(ID));
create table patients(ID int primary key, Name varchar(30) not null, Appt_NO int, Doc_ID varchar(15), constraint apptkey foreign key(Appt_NO) references appointments(Appt_NO), constraint docidkey foreign key(Doc_ID) references Doctors(ID));
create table inpatient(slno int primary key auto_increment ,Patient_ID int, Room_NO int(7), Lab_NO int(7), admition_date datetime default now(), discharge datetime not null , constraint patkey foreign key(Patient_id) references patients(id), constraint roomkey foreign key(room_no) references rooms(room_no), constraint labkey foreign key (lab_no) references labs(lab_no));
create table outpatients(slno int primary key auto_increment ,Patient_ID int, Lab_NO int(7), constraint patkey2 foreign key(Patient_id) references patients(id), constraint labkey2 foreign key (lab_no) references labs(lab_no));
create table bills(slno int primary key auto_increment ,Patient_ID int,moneytemp int,totaltemp int, constraint patkey3 foreign key(Patient_id) references patients(id));
