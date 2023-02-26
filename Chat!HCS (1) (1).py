import mysql.connector as a
import pyttsx3

con=a.connect(host="localhost",user="root",passwd="rohit")
c=con.cursor()

def mod():
    pas1=input("Enter the password: ")
    if pas1.upper()=="SSV":
        ch=input("Enter the name of Hospital you want to add:")
        s="create database if not exists"+" "+ch
        c.execute(s)
    
            

def user():   
    hn=input("Enter the name of the Hospital: ")
    s2="use"+" "+hn
    c.execute(s2)

nandini=1
while(nandini<2):        
    print("""
           +*************************************************+
           |              Welcome to Chat!HCS                |    
           +-------------------------------------------------+
           |                   Sign in as                    |
           +-------------------------------------------------+
           |         USER                    MODERATOR       |
           +*************************************************+""")
    si=input("---->")
    print(" ")
    if si.upper()=="MODERATOR":
        np=1
        while(np<2):
            mod()
            co=input("Want to Sign out? [yes/no] ")
            if co.upper()=="YES":
                np+=5
                print(" ")
            
    elif si.upper()=="USER":
        user()
        nandini+=5



# -> CREATING A TABLE FOR PATIENT:

abc="create table if not exists pat \
(adhaar_no varchar(15) primary key,\
name varchar(20),\
problem varchar(10),\
p_id int(10),\
address varchar(40),\
phone varchar(30),\
treated_successfully varchar(5) )"
c.execute(abc)

# -> CREATING A TABLE FOR DOCTOR:

s="create table if not exists doct  \
(doctor_name  varchar(20),\
p_id int(10) unique,\
specification varchar(30),\
gender varchar(10),\
doc_id varchar(10) primary key,\
working_hour int(10),\
patient_not_recovered int(10) )"
c.execute(s)

# -> CREATING A TABLE FOR MEDICINE:

s="create table if not exists medi_t   \
(med_name char(20),\
p_id int(10), \
no_of_quantity int(20), \
price int(10))"
c.execute(s)

def a_p():
    add=input("Adhaar Number ")
    n=input("Patient Name:")
    c=input("Problem:")
    r=input("Patient id:")
    a=input("Address:")
    p=input("Phone:")
    t=input('Treated or Not :')
    data=(add,n,c,r,a,p,t)
    sql="insert into pat values(%s,%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-----------------------------------------------------------------------<")
    main()

def r_p():            
    c=input("Patient Name:")
    r=int(input("Patient_id:"))
    data=(c,r)
    sql="delete from pat where name=%s and p_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data deleted")
    print(">-----------------------------------------------------------------------<")
    main()

def update_p():         
    add=input("Patient_Number ")
    n=input("Patient _Name:")
    c=input("Problem :")
    r=input("Patient_id:")
    a=input("Address:")
    p=input("Phone:")
    t=input('Treated or Not:')
    data=(add,n,c,r,a,p,t)
    sql="insert into pat values(%s,%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA UPDATE SUCCESSFULLY")
    print(">-----------------------------------------------------------------------<")
    main()
   
def up_p():            
    print("please enter old information")
    c=input("Patient Name :")
    r=input("Patient_id:")
    data=(c,r)
    sql="delete from pat where name=%s and p_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">======================================================================<")
    update_p()
    print("data update successfully")

def d_p():         
    cl=input("PATIENT_ID:")
    data=(cl,)
    sql="select * from pat where p_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("ADHAAR NUMBER :",i[0])
        print("PATIENT NAME :",i[1])
        print("PROBLEM :",i[2])
        print("PATIENT_ID :",i[3])
        print("ADDRESS :",i[4])
        print("PHONE :",i[5])
        print('TREATED OR NOT:', i[6]) 
        print(">----------------------------------<")
    print(">-----------------------------------------------------------------------<")
    main()

def a_d():       
    n=input("Doctor Name:")
    p=int(input("Patients ID"))
    a=input("Specification:")
    ph=input("Gender:")
    ac=input("Doc_ID:")
    s=int(input("Working Hour:"))
    r=int(input("Number of patient not got recovered:"))
    data=(n,p,a,ph,ac,s,r)
    sql="insert into doct values(%s,%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-----------------------------------------------------------------------<")
    main()

def r_d():       
    n=input("Doctor Name:")
    ac=int(input("Doc_ID:"))
    data=(n,ac)
    sql="delete from doct where doctor_name=%s and doc_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data Updated")
    print(">-----------------------------------------------------------------------<")
    main()

def update_d():
    n=input("Doctor Name:")
    p=int(input("Patients ID:"))
    a=input("Specification:")
    ph=input("Gender:")
    ac=input("Doc_ID:")
    s=int(input("Working Hour:"))
    r=int(input("Number of patient not got recovered:"))
    data=(n,p,a,ph,ac,s,r)
    sql="insert into doct values(%s,%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA UPDATE SUCCESSFULLY")
    print(">-----------------------------------------------------------------------<")
    main()

def up_d():     
    print("please enter old information")
    n=input("Name:")
    ac=input("Doc_ID:")
    data=(n,ac)
    sql="delete from doct where doctor_name=%s and doc_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">======================================================<")
    update_d()

def d_d():      
    sql="select * from doct"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("DOCTER NAME :",i[0])
        print("PATIENTS ID :",i[1])
        print("SPECIFICATION :",i[2])
        print("GENDER :",i[3])
        print("DOCTER ID :",i[4])
        print("WORKING HOUR :",i[5])
        print("PATIENT NOT RECOVERED:",i[6])
        print(">----------------------------------<")
    print(">-----------------------------------------------------------------------<")
    main()

def a_m():

    add=input("Name of Medicines:")
    n=int(input("Patient ID:"))
    c=input("Quantity available:")
    r=int(input("Price:"))
    data=(add,n,c,r)
    sql="insert into medi_t values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-----------------------------------------------------------------------<")
    main()

def r_m():
    n=input("Name of Medicines:")
    ac=int(input("Patient ID:"))
    data=(n,ac)
    sql="delete from medi_t where med_name=%s and p_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data Updated")
    print(">-----------------------------------------------------------------------<")
    main()

def update_m():         
    add=input("Name of Medicines:")
    n=int(input("Patient ID:"))
    c=input("Quantity available:")
    r=int(input("Price:"))
    data=(add,n,c,r)
    sql="insert into medi_t values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA UPDATE SUCCESSFULLY")
    print(">-----------------------------------------------------------------------<")
    main()
   
def up_m():            
    print("please enter old information")
    c=input("Name of Medicines:")
    r=int(input("Patient_id:"))
    data=(c,r)
    sql="delete from medi_t where med_name=%s and p_id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">======================================================================<")
    update_m()
    print("data update successfully")

def d_m():
    sql="select * from medi_t"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("NAME OF MEDICINE :",i[0])
        print("PATIENTS ID :",i[1])
        print("QUANTITY AVAILABLE :",i[2])
        print("PRICE :",i[3])
        print(">----------------------------------<")
    print(">-----------------------------------------------------------------------<")
    main()

#--------------------------------------------------------------------------------------------------------------

def chat(mes):
        engine= pyttsx3.init() 
        print(mes) 

        engine.setProperty('rate', 128) 
        engine.setProperty('volume',250)
        engine.say(mes) 
        engine.runAndWait()

def ide():
    com=input()
    ex=1
    for i in com.split():
        if i.upper()=="MEDICINES":
            med()
            ex+=1
            rep()
        elif i.upper()=="MEDICINE":
            med()
            ex+=1
            rep()
        elif i.upper()=="PATIENT":
            tre()
            ex+=1
            rep()
        elif i.upper()=="PATIENTS":
            tre()
            ex+=1
            rep()
        elif i.upper()=="DOCTORS":
            do()
            ex+=1
            rep()
        elif i.upper()=="DOCTOR":
            do()
            ex+=1
            rep()
        
    if ex==1:
        mes6="Sorry, I am not designed for this task"
        chat(mes6)
        rep()


def rep():
    nm=1
    while(nm<2):
        mes7="Do you want to ask anything more?"
        chat(mes7)
        con3=input("[Yes/No]")
        if con3.upper()=="YES":
            mes8="Okay, then ask"
            chat(mes8)
            ide()
            
        else:
            nm+=4
            mes9="Okay, thank you"
            chat(mes9)
            exit()

#--------------------------------------------------------------------------------------------------------------

def med():
    mes5=[]
    d="select med_name FROM medi_t where no_of_quantity<1000"
    c.execute(d)
    ad=c.fetchall()
    for i in ad:
        mes5.append(i)
    if mes5==[]:
        mes9="All medicines are available in sufficient quantity so, chill"
        chat(mes9)
    else:
        ms="So, According to my analysis the quantity remaining for "+str(mes5)+" medicine is too low and it can be dangerous, so please increase the doses"
        chat(ms)

def tre():
    mes5=[]
    d="select doctor_name FROM doct where patient_not_recovered>5"
    c.execute(d)
    ad=c.fetchall()
    for i in ad:
        mes5.append(i)
    if mes5==[]:
        mes9="All docters are working well hence, patients recovering faster"
        chat(mes9)
    else:
        ms='''So, According to my analysis the most of the patients of '''+str(mes5)+'''are not able to recover 
so, please look into this matter'''
        chat(ms)

def do():
    mes5=[]
    d="select doctor_name FROM doct where working_hour>12"
    c.execute(d)
    ad=c.fetchall()
    for i in ad:
        mes5.append(i)
    if mes5==[]:
        mes9="All situation is under control, no need to worry"
        chat(mes9)
    else:
        ms='''So, According to my analysis '''+str(mes5)+'''is having so much workforce 
so, please try to hire new doctors of same speciality to reduce their pressure'''
        chat(ms)

def iden():
    com=input()
    ex=1
    for i in com.split():
        if i.upper()=="MEDICINES":
            med()
            ex+=1
            rep()
        elif i.upper()=="MEDICINE":
            med()
            ex+=1
            rep()
        elif i.upper()=="PATIENT":
            tre()
            ex+=1
            rep()
        elif i.upper()=="PATIENTS":
            tre()
            ex+=1
            rep()
        elif i.upper()=="DOCTORS":
            do()
            ex+=1
            rep()
        elif i.upper()=="DOCTOR":
            do()
            ex+=1
            rep()
        
    if ex==1:
        mes6="Sorry, I am not designed for this task"
        chat(mes6)
        rep()


def CHCS():
    ms3="Hello, this is Chat HCS"
    chat(ms3)
    ms2="What's your name"
    chat(ms2)
    nm=input()
    ms1="Hello "+(nm)
    chat(ms1)
    a2="how are you"
    chat(a2)
    nm=input()
    ms4="Okay, How can I help you"
    chat(ms4)
    iden()

def main():
    print("""
           +-------------------------------------------------+
           |                    Chat!HCS                     |    
           +-------------------------------------------------+
           |     1.ADD PATIENT         2.REMOVE PATIENT      |
           |     3.ADD DOCTOR          4.REMOVE DOCTOR       |
           |     5.ADD MEDICINES       6.REMOVE MEDICINES    |
           |     7.UPDATE PATIENT      8.UPDATE DOCTOR       |
           |     9.UPDATE MEDICINES   10.DISPLAY PATIENT     |
           |    11.DISPLAY DOCTER     12.DISPLAY MEDICINES   |
           |    13.Chat!BOT           14.EXIT                |
           +-------------------------------------------------+""")

    choice=input("Enter Task No :")
    print(">----------------------------------<")
    if (choice=='1'):
        a_p()
    elif (choice=='2'):
        r_p()
    elif (choice=='3'):
        a_d()
    elif (choice=='4'):
        r_d()
    elif (choice=='5'):
        a_m()
    elif (choice=='6'):
        r_m()
    elif (choice=='7'):
        up_p()
    elif (choice=='8'):
        up_d()
    elif (choice=='9'):
        up_m()
    elif (choice=='10'):
        d_p()
    elif (choice=='11'):
        d_d()
    elif (choice=='12'):
        d_m()
    elif (choice=='13'):
        CHCS()
    elif (choice=='11'):
        exit()
    else:
        print("Wrong input!")
main()

