import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import random
from datetime import date
 
t=tkinter.Tk()
t.geometry('1400x800')
t.title('Login')
t.config(bg='black')


def EmailSending(x,y,z,w,v,u,q,s,n,m,r,t):
    from_address = "sahilsharma93685@gmail.com"
    to_address = str(w)
    msg=MIMEMultipart('alternative')
    msg['Subject'] = "Ragistration successful"
    msg['From'] = from_address
    msg['To'] = to_address
    html = "Registration :- "+str(x) + "      Institute ID :-"+str(y) +"     Student Name :-  "+ str(z) + "      Student Email :- " +str(w) + "       Student Adress :-  " +str(v) + "        Batch id :- "+ str(u)+ "       Registration fees :- "+ str(q) +"     Student Department :- "+str(s) +"          Student Phone :- "+str(n)+ "     Course id :- "+str(m)+ "        Fees Plan :- "+ str(r)+   " Course Name :- "+ str(t)           
    part1 = MIMEText(html,'html')
    msg.attach(part1)
    username = 'sahilsharma93685@gmail.com'
    password = 'fxmrdccfhnfacqmz'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    print('mail send')





def login():
    cc=Canvas(t,width=1900,height=800,bg='black')
    cc.place(x=0,y=0)
    ll1=Label(t,text='Welcome',fg='red',bg='black',font=('Georgia',65))
    ll1.place(x=650,y=50)
    ll2=Label(t,text='To',fg='red',bg='black',font=('Georgia',65))
    ll2.place(x=810,y=150)
    ll3=Label(t,text='Institute',fg='red',bg='black',font=('Georgia',65))
    ll3.place(x=690,y=250)
    ll4=Label(t,text='Management',fg='red',bg='black',font=('Georgia',65))
    ll4.place(x=590,y=350)
    ll5=Label(t,text='System',fg='red',bg='black',font=('Georgia',65))
    ll5.place(x=690,y=450)
    llm=Label(t,text='___________________________________________________________-',fg='white',font=('Georgia',1),width=500)
    llm.place(x=600,y=450)
    llw=Label(t,text='___________________________________________________________-',fg='white',font=('Georgia',1),width=350)
    llw.place(x=660,y=150)
    llt=Label(t,text='___________________________________________________________-',fg='white',font=('Georgia',1),width=100)
    llt.place(x=810,y=250)
    lli=Label(t,text='___________________________________________________________-',fg='white',font=('Georgia',1),width=350)
    lli.place(x=680,y=350)
    lls=Label(t,text='___________________________________________________________-',fg='white',font=('Georgia',1),width=280)
    lls.place(x=700,y=560)

    #  ***********  Institute   **********************************************************************
    def InsertInstitute():
        c2=Canvas(t,width=1300,height=800,bg='black')
        c2.place(x=200,y=0)
        def back():
            c2.destroy()
            
        
        def insert():
                
                a=e1.get()
                b=e2.get()
                c=int(e3.get())
                d=e4.get()
                e=e5.get()
                f=e6.get()
                h=e8.get()
                i=e9.get()
                gov=h+' :- '+i
                
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                if len(a)==0 or len(b)==0 or c==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(h)==0 or len(i)==0 :
                   messagebox.showerror('Error','Check All values first')
                else:
                   sql="insert into institute values('%s','%s',%d,'%s','%s','%s','%s')"%(a,b,c,d,e,f,gov)
                   cur.execute(sql)
                   db.commit()
                   messagebox.showinfo('Status','Data Saved')
                   db.close()
                   e1.delete(0,100)
                   e2.delete(0,100)
                   e3.delete(0,100)
                   e3.insert(0,'0')
                   e4.delete(0,100)
                   e5.delete(0,100)
                   e6.delete(0,100)
                   e8.delete(0,100)
                   e8.insert(0,'Select Governmnt Proof ID')
                   e9.delete(0,100)
                   
        
              
        def checkdata():
            a=e1.get()
            if len(a)==0:
                lblcheck.config(text='Plese enter institute id ',fg='red')
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            
            sql="select count(*) from institute where istid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                lblcheck.config(text='OK Please go ahead',fg='green')
            else:
                lblcheck.config(text='Sorry not available',fg='red')
                
                
        
                
        btncheck=Button(c2,text='Check',bg='red',fg='white',command=checkdata)
        btncheck.place(x=820,y=120)
        lblcheck=Label(c2,bg='black')
        lblcheck.place(x=610,y=140)

        l=Label(c2,text='Insert Institude',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c2,text='Institute ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c2,text='Institute Name :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c2,text='Institute Strength :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c2,text='Institute Address :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        l=Label(c2,text='Institute Email :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        l=Label(c2,text='Institute Phone :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=370)
      
        l=Label(c2,text='Government Proof :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=420)
        e1=Entry(c2,width=30,bg='red',fg='white')
        e1.place(x=610,y=120)
        e2=Entry(c2,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c2,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e3.insert(0,'0')
        e4=Entry(c2,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c2,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)
        e6=Entry(c2,width=30,bg='red',fg='white')
        e6.place(x=610,y=370)
        e8=ttk.Combobox(c2,width=30)
        e8.insert(0,'Select Governmnt Proof ID')
        e8.place(x=610,y=420)
        e8['values']='Aadhar Card','Pen Card','Driving Licence','Pass Port'
        e9=Entry(c2,width=30,fg='white',bg='red')
        e9.place(x=820,y=420)
        b1=Button(c2,text='     Save       ',bg='red',fg='white',command=insert)
        b1.place(x=490,y=470)
        b2=Button(c2,text='     Close       ',bg='red',fg='white',command=close)
        b2.place(x=620,y=470)
        b3=Button(c2,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
       
        
       
    def FindInstitute():
        c3=Canvas(t,width=1300,height=800,bg='black')
        c3.place(x=200,y=0)
        def back():
            c3.destroy()
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e8.delete(0,100)
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from institute where istid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e5.insert(0, data[4])
                e6.insert(0, data[5])
                e8.insert(0, data[6])
            db.close()
        def clear():   
            e1.delete(0,100)
            e1.insert(0, 'Select Institute id ')
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e8.delete(0,100)
            
        def refresh():
    
                l.place(x=300,y=30)
                l1.place(x=200,y=120)
                l2.place(x=200,y=170)
                l3.place(x=200,y=220)
                l4.place(x=200,y=270) 
                l5.place(x=200,y=320)
                l6.place(x=200,y=370)
                l7.place(x=200,y=420)
                e1.place(x=410,y=120)
                e2.place(x=410,y=170)
                e3.place(x=410,y=220)
                e4.place(x=410,y=270)
                e5.place(x=410,y=320)
                e6.place(x=410,y=370)
                e8.place(x=410,y=420)
                b1.place(x=290,y=470)
                b2.place(x=420,y=470)
                b3.place(x=20,y=30)

        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istid from institute "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c3,text='Find Institude',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l1=Label(c3,text='Institute ID :',bg='black',fg='red',font=('Georgia',15))
        l1.place(x=400,y=120)
        l2=Label(c3,text='Institute Name :',bg='black',fg='red',font=('Georgia',15))
        l2.place(x=400,y=170)
        l3=Label(c3,text='Institute Strength :',bg='black',fg='red',font=('Georgia',15))
        l3.place(x=400,y=220)
        l4=Label(c3,text='Institute Address :',bg='black',fg='red',font=('Georgia',15))
        l4.place(x=400,y=270) 
        l5=Label(c3,text='Institute Email :',bg='black',fg='red',font=('Georgia',15))
        l5.place(x=400,y=320)
        l6=Label(c3,text='Institute Phone :',bg='black',fg='red',font=('Georgia',15))
        l6.place(x=400,y=370)
        l7=Label(c3,text='Government Proof :',bg='black',fg='red',font=('Georgia',15))
        l7.place(x=400,y=420)
        e1=ttk.Combobox(c3,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Institute id ')
        e2=Entry(c3,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c3,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c3,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c3,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)
        e6=Entry(c3,width=30,bg='red',fg='white')
        e6.place(x=610,y=370)
        e8=Entry(c3,width=30,bg='red',fg='white')
        e8.place(x=610,y=420)
        b1=Button(c3,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=470)
        b2=Button(c3,text='     Clear       ',bg='red',fg='white',command=clear)
        b2.place(x=620,y=470)
        b3=Button(c3,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c3,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=20)
        
        
        
    def UpdateInstitute():
        c4=Canvas(t,width=1300,height=800,bg='black')
        c4.place(x=200,y=0)
        def back():
            c4.destroy()
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e8.delete(0,100)
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from institute where istid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e5.insert(0, data[4])
                e6.insert(0, data[5])
                e8.insert(0, data[6])
            db.close()
        def update():
            a=e1.get()
            b=e2.get()
            c=int(e3.get())
            d=e4.get()
            e=e5.get()
            f=e6.get()
            h=e8.get()
            i=e9.get()
            gov=h+' :- '+i
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(a)==0 or len(b)==0 or c==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(h)==0 :
                messagebox.showerror('Error','Check All values first')
            else:
              sql="update institute set istname='%s',iststrength=%d,istaddress='%s',istemail='%s',istphone='%s',istgovid='%s' where istid='%s' "%(b,c,d,e,f,gov,a)
              cur.execute(sql)
              db.commit()
              e1.delete(0,100)
              e1.insert(0, 'Select Institute id ')
              e2.delete(0,100)
              e3.delete(0,100)
              e3.insert(0,'0')
              e4.delete(0,100)
              e5.delete(0,100)
              e6.delete(0,100)
              e8.delete(0,100)

              messagebox.showinfo('Status','Data Updated')
            db.close() 
            
          
        
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istid from institute "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c4,text='Update Institude',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c4,text='Institute ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c4,text='Institute Name :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c4,text='Institute Strength :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c4,text='Institute Address :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        l=Label(c4,text='Institute Email :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        l=Label(c4,text='Institute Phone :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=370)
        
        l=Label(c4,text='Government Proof :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=420)
        e1=ttk.Combobox(c4,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Institute id ')
        e2=Entry(c4,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c4,width=30,bg='red',fg='white')
        e3.insert(0,'0')
        e3.place(x=610,y=220)
        e4=Entry(c4,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c4,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)
        e6=Entry(c4,width=30,bg='red',fg='white')
        e6.place(x=610,y=370)
        e8=ttk.Combobox(c4,width=30)
        e8.insert(0,'Select Details')
        e8.place(x=610,y=420)
        e8['values']='Aadhar Card','Pen Card','Driving Licence','Pass Port'
        e9=Entry(c4,width=30,fg='white',bg='red')
        e9.place(x=820,y=420)
        b1=Button(c4,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=470)
        b2=Button(c4,text='     Upadte       ',bg='red',fg='white',command=update)
        b2.place(x=620,y=470)
        b3=Button(c4,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
    def DeleteInstitute():
        c5=Canvas(t,width=1300,height=800,bg='black')
        c5.place(x=200,y=0)
        def back():
            c5.destroy()
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e8.delete(0,100)
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from institute where istid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e5.insert(0, data[4])
                e6.insert(0, data[5])
                e8.insert(0, data[6])
            db.close()
            
        def delete():
            a=e1.get()
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select count(*) from registration where istid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                sql="delete from institute where istid='%s' "%(a)
                cur.execute(sql)
                db.commit()
                e1.delete(0,100)
                e1.insert(0, 'Select Institute id ')
                e2.delete(0,100)
                e3.delete(0,100)
                e3.insert(0,'0')
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e8.delete(0,100)
                messagebox.showinfo('Status','record deleted')
                db.close()
            else:
                messagebox.showerror('Cant be Deleted','Already Exist in registration')
            
            
            
            
        
        
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istid from institute "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c5,text='Delete Institude',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c5,text='Institute ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c5,text='Institute Name :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c5,text='Institute Strength :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c5,text='Institute Address :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        l=Label(c5,text='Institute Email :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        l=Label(c5,text='Institute Phone :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=370)
        l=Label(c5,text='Government Proof:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=420)
        e1=ttk.Combobox(c5,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Institute id ')
        e2=Entry(c5,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c5,width=30,bg='red',fg='white')
        e3.insert(0,'0')
        e3.place(x=610,y=220)
        e4=Entry(c5,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c5,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)
        e6=Entry(c5,width=30,bg='red',fg='white')
        e6.place(x=610,y=370)
        e8=Entry(c5,width=30,bg='red',fg='white')
        e8.place(x=610,y=420)
        b1=Button(c5,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=470)
        b2=Button(c5,text='     delete       ',bg='red',fg='white',command=delete)
        b2.place(x=620,y=470)
        b3=Button(c5,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
        
    # ********       Course   **********************************************************************
    def InsertCourse():
        c6=Canvas(t,width=1300,height=800,bg='black')
        c6.place(x=200,y=0)
        def back():
            c6.destroy()
        def back():
            c6.destroy()
        
        def insert():
                a=e1.get()
                b=e2.get()
                c=int(e3.get())
                d=e4.get()
                g=e7.get()
                h=e8.get()
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                if len(a)==0 or len(b)==0 or c==0 or len(d)==0 or len(g)==0 or len(h)==0:
                    messagebox.showerror('Error','Check All values first')
                    
                sql="insert into course values('%s','%s',%d,'%s','%s','%s')"%(a,b,c,d,g,h)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Status','Data Saved')
                db.close()
                e1.delete(0,100)
                e2.delete(0,100)
                e2.insert(0,'Select Course Name')
                e3.delete(0,100)
                e3.insert(0,'0')
                e4.delete(0,100)
                e7.delete(0,100)
                e8.delete(0,100)

             
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            a=e1.get()
            sql="select count(*) from course where courseid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                lblcheck.config(text='OK Please go ahead',fg='green')
            else:
                lblcheck.config(text='Sorry not available',fg='red')
                
        btncheck=Button(c6,text='Check',bg='red',fg='white',command=checkdata)
        btncheck.place(x=820,y=120)
        lblcheck=Label(c6,bg='black')
        lblcheck.place(x=610,y=140)
       

        l=Label(c6,text='Insert Course',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c6,text='Course ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c6,text='Course Name :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c6,text='Fees :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c6,text='Course Duration :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        
        l=Label(c6,text='Stream :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        l=Label(c6,text='Description :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=370)
        e1=Entry(c6,width=30,bg='red',fg='white')
        e1.place(x=610,y=120)
        e2=ttk.Combobox(c6,width=30)
        e2.insert(0,'Select Course Name')
        e2.place(x=610,y=170)
        e2['values']='C++','C#','C language','Java','Python'
        if e2['values']=='c++':
            print('hellllooooo')
        
        e3=Entry(c6,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)   
        e3.insert(0 ,'0')
        e4=Entry(c6,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e7=Entry(c6,width=30,bg='red',fg='white')
        e7.place(x=610,y=320)
        e8=Entry(c6,width=30,bg='red',fg='white')
        e8.place(x=610,y=370)
        b1=Button(c6,text='     Save       ',bg='red',fg='white',command=insert)
        b1.place(x=490,y=420)
        b2=Button(c6,text='     Close       ',bg='red',fg='white')
        b2.place(x=620,y=420)
        b3=Button(c6,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
        
    def FindCourse():
        c7=Canvas(t,width=1300,height=800,bg='black')
        c7.place(x=200,y=0)
        def back():
            c7.destroy()
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from course where courseid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e7.insert(0, data[4])
                e8.insert(0, data[5])
            db.close()
        def clear():    
            e1.delete(0,100)
            e1.insert(0,'Select Course id ')
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            
        def refresh():
            l.place(x=300,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            l4.place(x=200,y=270) 
            l5.place(x=200,y=320)
            l6.place(x=200,y=370)
            e1.place(x=410,y=120)
            e2.place(x=410,y=170)
            e3.place(x=410,y=220)
            e4.place(x=410,y=270)
            e7.place(x=410,y=320)
            e8.place(x=410,y=370)
            b1.place(x=290,y=470)
            b2.place(x=420,y=470)
            b3.place(x=20,y=30)
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c7,text='Find Course',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l1=Label(c7,text='Course ID :',bg='black',fg='red',font=('Georgia',15))
        l1.place(x=400,y=120)
        l2=Label(c7,text='Course Name :',bg='black',fg='red',font=('Georgia',15))
        l2.place(x=400,y=170)
        l3=Label(c7,text='Fees :',bg='black',fg='red',font=('Georgia',15))
        l3.place(x=400,y=220)
        l4=Label(c7,text='Course Duration :',bg='black',fg='red',font=('Georgia',15))
        l4.place(x=400,y=270) 
        
        l5=Label(c7,text='Stream :',bg='black',fg='red',font=('Georgia',15))
        l5.place(x=400,y=320)
        l6=Label(c7,text='Description :',bg='black',fg='red',font=('Georgia',15))
        l6.place(x=400,y=370)
        e1=ttk.Combobox(c7,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Course id ')
        e2=Entry(c7,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c7,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c7,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        
        e7=Entry(c7,width=30,bg='red',fg='white')
        e7.place(x=610,y=320)
        e8=Entry(c7,width=30,bg='red',fg='white')
        e8.place(x=610,y=370)
        b1=Button(c7,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=430)
        b2=Button(c7,text='     Clear       ',bg='red',fg='white',command=clear)
        b2.place(x=620,y=430)
        b3=Button(c7,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c7,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=20)
        
        
        
    def UpdateCourse():
        c8=Canvas(t,width=1300,height=800,bg='black')
        c8.place(x=200,y=0)
        def back():
            c8.destroy()
        
        def update():
            a=e1.get()
            b=e2.get()
            c=int(e3.get())
            d=e4.get()
            g=e7.get()
            h=e8.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(a)==0 or len(b)==0 or c==0 or len(d)==0 or len(g)==0 or len(h)==0:
                messagebox.showerror('Error','Check All values first')
            else:
               sql="update course set coursename='%s',fees=%d,courseduration='%s',stream='%s',description='%s' where courseid='%s' "%(b,c,d,g,h,a)
               cur.execute(sql)
               db.commit()
               e1.delete(0,100)
               e1.insert(0, 'Select Course id ')
               e2.delete(0,100)
               e2.insert(0,'Select Course Name')
               e3.delete(0,100)
               e3.insert(0,'0')
               e4.delete(0,100)
               e7.delete(0,100)
               e8.delete(0,100)
               messagebox.showinfo('Status','Data Updated                            ')
            db.close()
        
        def find():
           e2.delete(0,100)
           e3.delete(0,100)
           e4.delete(0,100)
           e7.delete(0,100)
           e8.delete(0,100)
           
           a=e1.get()
           db=pymysql.connect(host='localhost',user='root',password='root',database='project')
           cur=db.cursor()
           sql="select * from course where courseid ='%s' "%(a)
           cur.execute(sql)
           data=cur.fetchone()
           if data==None:
               messagebox.showerror('Status','Data not Found')
           else:
               e2.insert(0, data[1])
               e3.insert(0, data[2])
               e4.insert(0, data[3])
               e7.insert(0, data[4])
               e8.insert(0, data[5])
           db.close()
        
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c8,text='Update Course',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c8,text='Course ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c8,text='Course Name :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c8,text='Fees :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c8,text='Course Duration :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
       
        l=Label(c8,text='Stream :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        l=Label(c8,text='Description :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=370)
        e1=ttk.Combobox(c8,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Course id ')
        e2=ttk.Combobox(c8,width=30)
        e2.insert(0,'Select Course Name')
        e2.place(x=610,y=170)
        e2['values']='C++','C#','C language','Java','Python'
        e3=Entry(c8,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e3.insert(0 ,'0')
        e4=Entry(c8,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        
        e7=Entry(c8,width=30,bg='red',fg='white')
        e7.place(x=610,y=320)
        e8=Entry(c8,width=30,bg='red',fg='white')
        e8.place(x=610,y=370)
        b1=Button(c8,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=430)
        b2=Button(c8,text='     Update       ',bg='red',fg='white',command=update)
        b2.place(x=620,y=430)
        b3=Button(c8,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
        
    def DeleteCourse():
        c9=Canvas(t,width=1300,height=800,bg='black')
        c9.place(x=200,y=0)
        def back():
            c9.destroy()
        def delete():
            a=e1.get()
            
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select count(*) from registration where regcourseid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
               db=pymysql.connect(host='localhost',user='root',password='root',database='project')
               cur=db.cursor()
               sql="delete from course where courseid='%s' "%(a)
               cur.execute(sql)
               db.commit()
               messagebox.showinfo('Status','record deleted')
               db.close()
               e1.delete(0,100)
               e1.insert(0, 'Select Course id ')
               e2.delete(0,100)
               e3.delete(0,100)
               e4.delete(0,100)
               e7.delete(0,100)
               e8.delete(0,100)
            else:
                messagebox.showerror('Cant be Deleted','Already Exist in registration')
            
        
        
        
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e7.delete(0,100)
            e8.delete(0,100)
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from course where courseid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e7.insert(0, data[4])
                e8.insert(0, data[5])
            db.close()
        
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c9,text='Delete Course',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c9,text='Course ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c9,text='Course Name :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c9,text='Fees :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c9,text='Course Duration :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        
        l=Label(c9,text='Stream :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        l=Label(c9,text='Description :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=370)
        e1=ttk.Combobox(c9,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Course id ')
        e2=Entry(c9,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c9,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c9,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        
        e7=Entry(c9,width=30,bg='red',fg='white')
        e7.place(x=610,y=320)
        e8=Entry(c9,width=30,bg='red',fg='white')
        e8.place(x=610,y=370)
        b1=Button(c9,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=430)
        b2=Button(c9,text='     Delete       ',bg='red',fg='white',command=delete)
        b2.place(x=620,y=430)
        b3=Button(c9,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
        
    #****************    Batch   **********************************************************************
    def InsertBatch():
        c10=Canvas(t,width=1300,height=800,bg='black')
        c10.place(x=200,y=0)
        def back():
            c10.destroy()
        def insert():
                a=e1.get()
                b=e2.get()
                c=e3.get()
                d=e4.get()
                e=e5.get()
               
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0:
                    messagebox.showerror('Error','Check All values first')
                else: 
                    if c>b:
                        sql="insert into batch values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Status','Data Saved')
                        db.close()
                        e1.delete(0,100)
                        e2.delete(0,100)
                        e3.delete(0,100)
                        e4.delete(0,100)
                        e5.delete(0,100)
                        e2.insert(0, mt)
                        lblcheck.delete(0,100)
                    else :
                        messagebox.showerror('alert','Plese Check date of batch over ')
                     
                
                    
                  

              
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            a=e1.get()
            sql="select count(*) from batch where batchid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                lblcheck.config(text='OK Please go ahead',fg='green')
            else:
                lblcheck.config(text='Sorry not available',fg='red')
                
        btncheck=Button(c10,text='Check',bg='red',fg='white',command=checkdata)
        btncheck.place(x=820,y=120)
        lblcheck=Label(c10,bg='black')
        lblcheck.place(x=610,y=140)
       

        l=Label(c10,text='Insert Batch',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c10,text='Batch ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c10,text='Batch Start :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c10,text='Batch Over:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c10,text='Batch Time :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        l=Label(c10,text='Batch Duration :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        e1=Entry(c10,width=30,bg='red',fg='white')
        e1.place(x=610,y=120)
        e2=Entry(c10,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=DateEntry(c10,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c10,width=30,bg='red',fg='white')
        '''  tl= time.time()
        at=time.localtime(tl)
        mt=time.asctime(at)'''
        mt=date.today()
        print(mt)
        e2.insert(0, mt)
        
        
        e4.place(x=610,y=270)
        e5=Entry(c10,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)

        b1=Button(c10,text='     Save       ',bg='red',fg='white',command=insert)
        b1.place(x=490,y=400)
        b2=Button(c10,text='     Close       ',bg='red',fg='white')
        b2.place(x=620,y=400)
        b3=Button(c10,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
    def FindBatch():
        c11=Canvas(t,width=1300,height=800,bg='black')
        c11.place(x=200,y=0)
        def back():
            c11.destroy()
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
          
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from batch where batchid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e5.insert(0, data[4])
            db.close()
        def clear():    
            e1.delete(0,100)
            e1.insert(0, 'Select Batch id ')
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
        def refresh():
            l.place(x=300,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            l4.place(x=200,y=270) 
            l5.place(x=200,y=320)
            e1.place(x=410,y=120)
            e2.place(x=410,y=170)
            e3.place(x=410,y=220)
            e4.place(x=410,y=270)
            e5.place(x=410,y=320)
            b1.place(x=290,y=470)
            b2.place(x=420,y=470)
            b3.place(x=20,y=30)
            
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select batchid from batch "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c11,text='Find Batch',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l1=Label(c11,text='Batch ID :',bg='black',fg='red',font=('Georgia',15))
        l1.place(x=400,y=120)
        l2=Label(c11,text='Batch Start :',bg='black',fg='red',font=('Georgia',15))
        l2.place(x=400,y=170)
        l3=Label(c11,text='Batch Over:',bg='black',fg='red',font=('Georgia',15))
        l3.place(x=400,y=220)
        l4=Label(c11,text='Batch Time :',bg='black',fg='red',font=('Georgia',15))
        l4.place(x=400,y=270) 
        l5=Label(c11,text='Batch Duration :',bg='black',fg='red',font=('Georgia',15))
        l5.place(x=400,y=320)
        e1=ttk.Combobox(c11,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Batch id ')
        e2=Entry(c11,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c11,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c11,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c11,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)

        b1=Button(c11,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=400)
        b2=Button(c11,text='     Close       ',bg='red',fg='white',command=clear)
        b2.place(x=620,y=400)
        b3=Button(c11,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c11,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=20)
        
       
        
    def UpdateBatch():
        c12=Canvas(t,width=1300,height=800,bg='black')
        c12.place(x=200,y=0)
        def back():
            c12.destroy()
        def update():
            a=e1.get()
            b=e2.get()
            c=e3.get()
            d=e4.get()
            e=e5.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0:
                messagebox.showerror('Error','Check All values first')
            else:
                if c>b:
                    sql="update batch set batchstart='%s',batchover='%s',batchtime='%s',batchduration='%s' where batchid='%s' "%(b,c,d,e,a)
                    cur.execute(sql)
                    db.commit()
                    e1.delete(0,100)
                    e1.insert(0, 'Select Batch id ')
                    e2.delete(0,100)
                    e3.delete(0,100)
                    e4.delete(0,100)
                    e5.delete(0,100)
                    e4.insert(0, mt)
                    messagebox.showinfo('Status','Data Updated')
                else :
                    messagebox.showerror('alert','Plese Check date of batch over ')
            

          
        
        def find():
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from batch where batchid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e5.insert(0, data[4])
            db.close()
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select batchid from batch "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c12,text='Update Batch',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c12,text='Batch ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c12,text='Batch Start :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c12,text='Batch Over:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c12,text='Batch Time :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        l=Label(c12,text='Batch Duration :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        e1=ttk.Combobox(c12,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Batch id ')
        e2=Entry(c12,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=DateEntry(c12,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c12,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c12,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)

        b1=Button(c12,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=400)
        b2=Button(c12,text='     Update       ',bg='red',fg='white',command=update)
        b2.place(x=620,y=400)
        b3=Button(c12,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
        
    def DeleteBatch():
        c13=Canvas(t,width=1300,height=800,bg='black')
        c13.place(x=200,y=0)
        def back():
            c13.destroy()
        def delete():
            a=e1.get()
            
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select count(*) from registration where regbatchid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
               db=pymysql.connect(host='localhost',user='root',password='root',database='project')
               cur=db.cursor()
               sql="delete from batch where batchid='%s' "%(a)
               cur.execute(sql)
               db.commit()
               messagebox.showinfo('Status','record deleted')
               db.close()
               e1.delete(0,100)
               e1.insert(0, 'Select Batch id ')
               e2.delete(0,100)
               e3.delete(0,100)
               e4.delete(0,100)
               e5.delete(0,100)
               e6.delete(0,100)
               e7.delete(0,100)
               e8.delete(0,100)
            else:
                messagebox.showerror('Cant be Deleted','Already Exist in registration')
            
            
            
        
        def find():
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from batch where batchid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
                e4.insert(0, data[3])
                e5.insert(0, data[4])
            db.close()
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select batchid from batch "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c13,text='Delete Batch',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c13,text='Batch ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c13,text='Batch Start :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c13,text='Batch Over:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)
        l=Label(c13,text='Batch Time :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=270) 
        l=Label(c13,text='Batch Duration :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=320)
        e1=ttk.Combobox(c13,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Batch id ')
        e2=Entry(c13,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c13,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)
        e4=Entry(c13,width=30,bg='red',fg='white')
        e4.place(x=610,y=270)
        e5=Entry(c13,width=30,bg='red',fg='white')
        e5.place(x=610,y=320)

        b1=Button(c13,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=400)
        b2=Button(c13,text='     Delete       ',bg='red',fg='white',command=delete)
        b2.place(x=620,y=400)
        b3=Button(c13,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
        
    #  ***************  Feeplans   **********************************************************************
    def InsertFeeplans():
        c14=Canvas(t,width=1300,height=800,bg='black')
        c14.place(x=200,y=0)
        def back():
            c14.destroy()
        def insert():
                a=e1.get()
                b=int(e2.get())
                c=int(e3.get())
               
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                if len(a)==0 or b==0 or c==0 or b<=999 or b>=100001:
                    messagebox.showerror('Error','Check All values first')
                else:
                  sql="insert into feesplans values('%s',%d,%d)"%(a,b,c)
                  cur.execute(sql)
                  db.commit()
                  messagebox.showinfo('Status','Data Saved')
                  db.close()
                  e1.delete(0,100)
                  e2.delete(0,100)
                  e3.delete(0,100)
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            a=e1.get()
            sql="select count(*) from feesplans where feeplanid='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                lblcheck.config(text='OK Please go ahead',fg='green')
            else:
                lblcheck.config(text='Sorry not available',fg='red')
                
        btncheck=Button(c14,text='Check',bg='red',fg='white',command=checkdata)
        btncheck.place(x=820,y=120)
        lblcheck=Label(c14,bg='black')
        lblcheck.place(x=610,y=140)
              

        l=Label(c14,text='Insert Fees Plans',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c14,text='Fees Plan ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c14,text='Amount :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c14,text='Installment:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)

        e1=Entry(c14,width=30,bg='red',fg='white')
        e1.place(x=610,y=120)
        e2=Entry(c14,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Spinbox(c14,from_=1,to=10,width=30)
        e3.place(x=610,y=220)
        e2.insert(0, '0')
        b1=Button(c14,text='     Save       ',bg='red',fg='white',command=insert)
        b1.place(x=490,y=300)
        b2=Button(c14,text='     Close       ',bg='red',fg='white')
        b2.place(x=620,y=300)
        b3=Button(c14,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
    def FindFeeplans():
        c15=Canvas(t,width=1300,height=800,bg='black')
        c15.place(x=200,y=0)
        def back():
            c15.destroy()
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from feesplans where feeplanid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
            db.close()
        def clear():    
            e1.delete(0,100)
            e1.insert(0, 'Select Feesplan ')
            e2.delete(0,100)
            e3.delete(0,100)
            
        def refresh():
            l.place(x=300,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            e1.place(x=410,y=120)
            e2.place(x=410,y=170)
            e3.place(x=410,y=220)
            b1.place(x=290,y=270)
            b2.place(x=420,y=270)
            b3.place(x=20,y=30)
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select feeplanid from feesplans "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c15,text='Find Fees Plans',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l1=Label(c15,text='Fees Plan ID :',bg='black',fg='red',font=('Georgia',15))
        l1.place(x=400,y=120)
        l2=Label(c15,text='Amount :',bg='black',fg='red',font=('Georgia',15))
        l2.place(x=400,y=170)
        l3=Label(c15,text='Installment:',bg='black',fg='red',font=('Georgia',15))
        l3.place(x=400,y=220)

        e1=ttk.Combobox(c15,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Feesplan ')
        e2=Entry(c15,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c15,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)

        b1=Button(c15,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=300)
        b2=Button(c15,text='     Clear       ',bg='red',fg='white',command=clear)
        b2.place(x=620,y=300)
        b3=Button(c15,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c15,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=20)
        
       
        
    def UpdateFeeplans():
        c16=Canvas(t,width=1300,height=800,bg='black')
        c16.place(x=200,y=0)
        def back():
            c16.destroy()
        def update():
            a=e1.get()
            b=int(e2.get())
            c=int(e3.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(a)==0 or b==0 or c==0:
                messagebox.showerror('Error','Check All values first')
            else:
              sql="update feesplans set amount=%d,insatallment=%d where feeplanid='%s' "%(b,c,a)
              cur.execute(sql)
              db.commit()
              messagebox.showinfo('Status','Data Updated                            ')
              db.close()
              e1.delete(0,100)
              e1.insert(0, 'Select Feesplan ')
              e2.delete(0,100)
              e3.delete(0,100)

           
        
        def find():
            
            e2.delete(0,100)
            e3.delete(0,100)
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from feesplans where feeplanid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
            db.close()
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select feeplanid from feesplans "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c16,text='Update Fees Plans',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c16,text='Fees Plan ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c16,text='Amount :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c16,text='Installment:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)

        e1=ttk.Combobox(c16,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Feesplan ')
        e2=Entry(c16,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Spinbox(t,from_=1,to=10,width=30)
        e3.place(x=810,y=220)
        e2.insert(0, '0')
        b1=Button(c16,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=300)
        b2=Button(c16,text='     Update       ',bg='red',fg='white',command=update)
        b2.place(x=620,y=300)
        b3=Button(c16,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
       
        
    def DeleteFeeplans():
        c17=Canvas(t,width=1300,height=800,bg='black')
        c17.place(x=200,y=0)
        def back():
            c17.destroy()
        def delete():
            a=e1.get()
            
            
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select count(*) from registration where regfeeplan='%s'"%(a)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
               db=pymysql.connect(host='localhost',user='root',password='root',database='project')
               cur=db.cursor()
               sql="delete from feesplans where feeplanid='%s' "%(a)
               cur.execute(sql)
               db.commit()
               messagebox.showinfo('Status','record deleted')
               db.close()
               e1.delete(0,100)
               e1.insert(0, 'Select Feesplan ')
               e2.delete(0,100)
               e3.delete(0,100)
            else:
                messagebox.showerror('Cant be Deleted','Already Exist in registration')
            
            
            
        
        def find():
            e2.delete(0,100)
            e3.delete(0,100)
            
            a=e1.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from feesplans where feeplanid ='%s' "%(a)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
                messagebox.showerror('Status','Data not Found')
            else:
                e2.insert(0, data[1])
                e3.insert(0, data[2])
            db.close()
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select feeplanid from feesplans "
        cur.execute(sql)
        data=cur.fetchall()
        
        l=Label(c17,text='Delete Fees Plans',fg='red',bg='black',font=('Georgia',30))
        l.place(x=500,y=30)
        l=Label(c17,text='Fees Plan ID :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=120)
        l=Label(c17,text='Amount :',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=170)
        l=Label(c17,text='Installment:',bg='black',fg='red',font=('Georgia',15))
        l.place(x=400,y=220)

        e1=ttk.Combobox(c17,width=30)
        e1.place(x=610,y=120)
        e1['values']=data
        e1.insert(0, 'Select Feesplan ')
        e2=Entry(c17,width=30,bg='red',fg='white')
        e2.place(x=610,y=170)
        e3=Entry(c17,width=30,bg='red',fg='white')
        e3.place(x=610,y=220)

        b1=Button(c17,text='     Find       ',bg='red',fg='white',command=find)
        b1.place(x=490,y=300)
        b2=Button(c17,text='     Delete       ',bg='red',fg='white',command=delete)
        b2.place(x=620,y=300)
        b3=Button(c17,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
        
        
    #  ***************  Enquiry   **********************************************************************
    def InsertEnquiry():
        c18=Canvas(t,width=1300,height=800,bg='black')
        c18.place(x=200,y=0)
        def back():
            c18.destroy()
        def insert():
             x=(a.get())
             y=(b.get())
             z=(c.get())
             w=(d.get())
             v=(e.get())
             u=(f.get())
             q=(g.get())
           
             
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0 or len(q)==0:
                 messagebox.showerror('Error','Check All values first')
             else:
                sql="insert into enquiry values('%s','%s','%s','%s','%s','%s','%s')"%(x,y,z,w,v,u,q)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Status","Values inserted")
                     
                a.delete(0,100)
                b.delete(0,100)
                c.delete(0,100)
                d.delete(0,100)
                e.delete(0,100)
                f.delete(0,100)
                f.insert(0,'Select Course ID')
                g.delete(0,100)

             
             
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            x=a.get()
            sql="select count(*) from enquiry where enqno='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                lblcheck.config(text='OK Please go ahead',fg='green')
            else:
                lblcheck.config(text='Sorry not available',fg='red')
                   
           
            

        
        
        btncheck=Button(c18,text='Check',bg='red',fg='white',command=checkdata)
        btncheck.place(x=820,y=120)
        lblcheck=Label(c18,bg='black')
        lblcheck.place(x=610,y=140)
        l=Label(c18,text='Insert Enquiry',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c18,text='Enquiry Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c18,text='Enquiry Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c18,text='Enquiry Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c18,text='Enquiry Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c18,text='Enquiry Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c18,text='Enquiry Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c18,text='Estimation of Joining:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c18,text='INSERT',width=10,bg='red',fg='white',command=insert)
        b2=Button(c18,text='CLEAR',width=10,bg='red',fg='white')
        b3=Button(c18,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        a=Entry(c18,width=30,bg='red',fg='white')
        b=Entry(c18,width=30,bg='red',fg='white')
        c=Entry(c18,width=30,bg='red',fg='white')
        d=Entry(c18,width=30,bg='red',fg='white')
        e=Entry(c18,width=30,bg='red',fg='white')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course"
        cur.execute(sql)
        data1=cur.fetchall()
        f=ttk.Combobox(c18,width=30)
        f.insert(0,'Select Course ID')
        f['values']=data1        
        g=Entry(c18,width=30,bg='red',fg='white')




        l.place(x=500,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)






        a.place(x=610,y=120)
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)




        b1.place(x=490,y=470)
        b2.place(x=610,y=470)

       
        
       
        
    def FindEnquiry():
        c19=Canvas(t,width=1300,height=800,bg='black')
        c19.place(x=200,y=0)
        def back():
            c19.destroy()
        
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  Enquiry where enqno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
             db.close
        def cleardata():
             a.delete(0,100)
             a.insert(0,'Select Enquiry Number.')
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
             
        def refresh():
            l.place(x=300,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            l4.place(x=200,y=270) 
            l5.place(x=200,y=320)
            l6.place(x=200,y=370) 
            l7.place(x=200,y=420)
            a.place(x=420,y=120)
            b.place(x=420,y=170)
            c.place(x=420,y=220)
            d.place(x=420,y=270)
            e.place(x=420,y=320)
            f.place(x=420,y=370)
            g.place(x=420,y=420)
            b1.place(x=290,y=470)
            b2.place(x=420,y=470)
            b3.place(x=20,y=30)
             
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select enqno from enquiry"
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c19,text='Find Enquiry',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c19,text='Enquiry Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c19,text='Enquiry Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c19,text='Enquiry Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c19,text='Enquiry Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c19,text='Enquiry Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c19,text='Enquiry Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c19,text='Estimation of Joining:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c19,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c19,text='CLEAR',width=10,bg='red',fg='white',command=cleardata)
        b3=Button(c19,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c19,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=30)
        a=ttk.Combobox(c19,width=30)

        b=Entry(c19,width=30,bg='red',fg='white')
        c=Entry(c19,width=30,bg='red',fg='white')
        d=Entry(c19,width=30,bg='red',fg='white')
        e=Entry(c19,width=30,bg='red',fg='white')
        f=Entry(c19,width=30,bg='red',fg='white')
        g=Entry(c19,width=30,bg='red',fg='white')




        l.place(x=500,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)






        a.place(x=610,y=120)
        a['values']=data
        a.insert(0, 'Select Enquiry Number ')
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)




        b1.place(x=490,y=470)
        b2.place(x=610,y=470)

        
           


        
        
        
        
        
    def UpdateEnquiry():
        c20=Canvas(t,width=1300,height=800,bg='black')
        c20.place(x=200,y=0)
        def back():
            c20.destroy()
        def find():
             
             
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
            
             
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  enquiry where enqno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
              

             db.close
            
            



        def update():
         
            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            v=(e.get())
            u=(f.get())
            q=(g.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0 or len(q)==0:
                messagebox.showerror('Error','Check All values first')
            else:
              sql="update enquiry set enqname='%s',enqaddress='%s',enqphone='%s',enqemail='%s',enqcourseid='%s',enqstart='%s' where enqno='%s'"%(y,z,w,v,u,q,x)
              cur.execute(sql)
              db.commit()
              print('Data update')    
              db.close
              messagebox.showinfo("Status","Values updated")
              a.delete(0,100)
              a.insert(0,'Select Enquiry Number.')
              b.delete(0,100)
              c.delete(0,100)
              d.delete(0,100)
              e.delete(0,100)
              f.delete(0,100)
              f.insert(0,'Select Course ID')
              g.delete(0,100)

           


        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select enqno from enquiry"
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c20,text='Update Enquiry',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c20,text='Enquiry Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c20,text='Enquiry Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c20,text='Enquiry Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c20,text='Enquiry Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c20,text='Enquiry Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c20,text='Enquiry Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c20,text='Estimation of Joining:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c20,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c20,text='CLEAR',width=10,bg='red',fg='white')
        b3=Button(c20,text='UPDATE',width=10,bg='red',fg='white',command=update)
        b4=Button(c20,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)

        a=ttk.Combobox(c20,width=30)
        a.insert(0, 'Select Enquiry Number ')
        b=Entry(c20,width=30,bg='red',fg='white')
        c=Entry(c20,width=30,bg='red',fg='white')
        d=Entry(c20,width=30,bg='red',fg='white')
        e=Entry(c20,width=30,bg='red',fg='white')
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course"
        cur.execute(sql)
        data1=cur.fetchall()
        f=ttk.Combobox(c20,width=30)
        f.insert(0,'Select Course ID')
        f['values']=data1        
        g=Entry(c20,width=30,bg='red',fg='white')




        l.place(x=500,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)






        a.place(x=610,y=120)
        a['values']=data

        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)




        b1.place(x=440,y=470)
        b2.place(x=560,y=470)
        b3.place(x=680,y=470)
        
        
        
       
        
       
        
    def DeleteEnquiry():
        c21=Canvas(t,width=1300,height=800,bg='black')
        c21.place(x=200,y=0)
        def back():
            c21.destroy()
        def delete():

            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            v=(e.get())
            u=(f.get())
            p=(g.get())
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0 or len(p)==0:
                messagebox.showerror('Error','Check All values first')
            else:
               sql="delete from enquiry where enqno='%s'"%(x)
               cur.execute(sql)
               db.commit()
               db.close
               messagebox.showinfo("Status","Values deleted")
               
               a.delete(0,100)
               a.insert(0,'Select Enquiry Number.')
               b.delete(0,100)
               c.delete(0,100)
               d.delete(0,100)
               e.delete(0,100)
               f.delete(0,100)
               g.delete(0,100)
               
        def find():
             
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             
             sql="select * from  Enquiry where enqno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
             db.close
            

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select enqno from enquiry"
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c21,text='Delete Enquiry',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c21,text='Enquiry Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c21,text='Enquiry Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c21,text='Enquiry Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c21,text='Enquiry Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c21,text='Enquiry Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c21,text='Enquiry Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c21,text='Estimation of Joining:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c21,text='DELETE',width=10,bg='red',fg='white',command=delete)
        b2=Button(c21,text='CLEAR',width=10,bg='red',fg='white')
        b3=Button(c21,text='FIND',width=10,bg='red',fg='white',command=find)
        b4=Button(c21,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)


        a=ttk.Combobox(c21,width=30)
        a.insert(0, 'Select Enquiry Number ')
        b=Entry(c21,width=30,bg='red',fg='white')
        c=Entry(c21,width=30,bg='red',fg='white')
        d=Entry(c21,width=30,bg='red',fg='white')
        e=Entry(c21,width=30,bg='red',fg='white')
        f=Entry(c21,width=30,bg='red',fg='white')
        g=Entry(c21,width=30,bg='red',fg='white')




        l.place(x=500,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)






        a.place(x=610,y=120)
        a['values']=data

        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)




        b1.place(x=440,y=470)
        b2.place(x=560,y=470)
        b3.place(x=680,y=470)




    #  ***************  Registration   **********************************************************************
    def InsertRegistration():
        c22=Canvas(t,width=1300,height=800,bg='black')
        c22.place(x=200,y=0)
        def back():
            c22.destroy()
        def insert():
             
            
             
            
             x=(a.get())
             y=(b.get())
             z=(c.get())
             w=(d.get())
             v=(e.get())
             u=(f.get())
             q=int(g.get())
             s=(h.get())
             n=(i.get())
             m=(j.get())
             r=(k.get())
             t=(lt.get())
             
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0 or q==0 or len(s)==0 or len(n)==0 or len(m)==0 or len(r)==0 or len(t)==0:
                 messagebox.showerror('Error','Check All values first')
             else:
                sql="insert into registration values('%s','%s','%s','%s','%s','%s',%d,'%s','%s','%s','%s','%s')"%(x,y,z,w,v,u,q,s,n,m,r,t)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Status","Values inserted")
                
                a.delete(0,100)
                b.delete(0,100)
                b.insert(0,'Select Institute ID')
                c.delete(0,100)
                d.delete(0,100)
                e.delete(0,100)
                f.delete(0,100)
                f.insert(0,'Select Batch ID')
                g.delete(0,100)
                g.insert(0,'100')
                h.delete(0,100)
                h.insert(0,'Select Institute Name')
                i.delete(0,100)
                j.delete(0,100)
                j.insert(0,'Select Course ID')
                k.delete(0,100)
                k.insert(0,'Select Fees plan')
                lt.delete(0,100)
                lt.insert(0,'Select Course Name')
                EmailSending(x,y,z,w,v,u,q,s,n,m,r,t)
                
                
                
                
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                sql="select count(*) from registration where istid='%s'"%(y)
                cur.execute(sql)
                data=cur.fetchone()
                print(data[0])
                print(type(data[0]))
                
                us.insert(0,data[0])
                
                usv=int(us.get())
                print(usv)
                
                db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                cur=db.cursor()
                sql="update institute set iststrength=%d where istid='%s'"%(usv,y)
                cur.execute(sql)
                db.commit()
                print('institute update')  
                
                
                db.close
            
                

                
              
                
                
          
             
        def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            x=a.get()
            sql="select count(*) from registration where regno='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            x=data[0]
            if x==0:
                lblcheck.config(text='OK Please go ahead',fg='green')
            else:
                lblcheck.config(text='Sorry not available',fg='red')
                   
           
            


        btncheck=Button(c22,text='Check',bg='red',fg='white',command=checkdata)
        btncheck.place(x=820,y=100)
        lblcheck=Label(c22,bg='black')
        lblcheck.place(x=610,y=120)
        l=Label(c22,text='Insert Registration',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c22,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c22,text='Institude ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c22,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c22,text='Student Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c22,text='Student Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c22,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c22,text='Registration Fees:-  ',fg='red',font=('Georgia',15),bg='black')
        l8=Label(c22,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l9=Label(c22,text='Student Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l10=Label(c22,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l11=Label(c22,text='Fees Plan:-  ',fg='red',font=('Georgia',15),bg='black')
        l12=Label(c22,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c22,text='INSERT',width=10,bg='red',fg='white',command=insert)
        b2=Button(c22,text='CLOSE',width=10,bg='red',fg='white')
        b3=Button(c22,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        a=Entry(c22,width=30,bg='red',fg='white')
        
         
        
        us=Entry(c22,width=30,bg='red',fg='white')
        c=Entry(c22,width=30,bg='red',fg='white')
        d=Entry(c22,width=30,bg='red',fg='white')
        e=Entry(c22,width=30,bg='red',fg='white')
        g=Entry(c22,width=30,bg='red',fg='white')
        g.insert(0,'100')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istname from institute"
        cur.execute(sql)
        data5=cur.fetchall()
        h=ttk.Combobox(c22,width=30)
        h['values']=data5
        h.insert(0, 'Select Institute Name ')
        
        i=Entry(c22,width=30,bg='red',fg='white')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istid from institute"
        cur.execute(sql)
        data2=cur.fetchall()
        b=ttk.Combobox(c22,width=30)
        b['values']=data2
        b.insert(0, 'Select Institute id ')
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select batchid from batch"
        cur.execute(sql)
        data1=cur.fetchall()
        f=ttk.Combobox(c22,width=30)
        f['values']=data1        
        f.insert(0, 'Select Batch id ')
      
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course"
        cur.execute(sql)
        data3=cur.fetchall()
        j=ttk.Combobox(c22,width=30)
        j['values']=data3 
        j.insert(0, 'Select Course id ')
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select feeplanid from feesplans"
        cur.execute(sql)
        data4=cur.fetchall()
        k=ttk.Combobox(c22,width=30)
        k['values']=data4 
        k.insert(0, 'Select Feesplan ')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select coursename from course"
        cur.execute(sql)
        data6=cur.fetchall()
        lt=ttk.Combobox(c22,width=30)
        lt['values']=data6 
        lt.insert(0, 'Select Course name ')
        
        l.place(x=440,y=20)
        l1.place(x=400,y=100)
        l2.place(x=400,y=150)
        l3.place(x=400,y=200)
        l4.place(x=400,y=250)
        l5.place(x=400,y=300)
        l6.place(x=400,y=350)
        l7.place(x=400,y=400)
        l8.place(x=400,y=450)
        l9.place(x=400,y=500)
        l10.place(x=400,y=550)
        l11.place(x=400,y=600)
        l12.place(x=400,y=650)

        a.place(x=610,y=100)
        b.place(x=610,y=150)
        c.place(x=610,y=200)
        d.place(x=610,y=250)
        e.place(x=610,y=300)
        f.place(x=610,y=350)
        g.place(x=610,y=400)
        h.place(x=610,y=450)
        i.place(x=610,y=500)
        j.place(x=610,y=550)
        k.place(x=610,y=600)
        lt.place(x=610,y=650)

        b1.place(x=490,y=700)
        b2.place(x=610,y=700)


    def FindRegistration():
        c23=Canvas(t,width=1300,height=800,bg='black')
        c23.place(x=200,y=0)
        def back():
            c23.destroy()
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
             h.delete(0,100)
             i.delete(0,100)
             j.delete(0,100)
             k.delete(0,100)
             lt.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  registration where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
                h.insert(0,data[7])
                i.insert(0,data[8])
                j.insert(0,data[9])
                k.insert(0,data[10])
                lt.insert(0,data[11])
             db.close
        def cleardata():
             a.delete(0,100)
             a.insert(0,'Select Registration NO.')
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
             h.delete(0,100)
             i.delete(0,100)
             j.delete(0,100)
             k.delete(0,100)
             lt.delete(0,100)
             
        def refresh():
            l.place(x=300,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            l4.place(x=200,y=270) 
            l5.place(x=200,y=320)
            l6.place(x=200,y=370) 
            l7.place(x=200,y=420)
            l8.place(x=200,y=470)
            l9.place(x=200,y=520)
            l10.place(x=200,y=570)
            l11.place(x=200,y=620) 
            l12.place(x=200,y=670)
            a.place(x=420,y=120)
            b.place(x=420,y=170)
            c.place(x=420,y=220)
            d.place(x=420,y=270)
            e.place(x=420,y=320)
            f.place(x=420,y=370)
            g.place(x=420,y=420)
            h.place(x=420,y=470)
            i.place(x=420,y=520)
            j.place(x=420,y=570)
            k.place(x=420,y=620)
            lt.place(x=420,y=670)
            b1.place(x=290,y=710)
            b2.place(x=420,y=710)
            b3.place(x=20,y=30)
             
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from registration "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c23,text='Find Registration',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c23,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c23,text='Institude ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c23,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c23,text='Student Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c23,text='Student Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c23,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c23,text='Registration Fees:-  ',fg='red',font=('Georgia',15),bg='black')
        l8=Label(c23,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l9=Label(c23,text='Student Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l10=Label(c23,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l11=Label(c23,text='Fees Plan:-  ',fg='red',font=('Georgia',15),bg='black')
        l12=Label(c23,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c23,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c23,text='CLEAR',width=10,bg='red',fg='white',command=cleardata)
        b3=Button(c23,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c23,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=30)
        
        a=ttk.Combobox(c23,width=30)
        b=Entry(c23,width=30,bg='red',fg='white')
        c=Entry(c23,width=30,bg='red',fg='white')
        d=Entry(c23,width=30,bg='red',fg='white')
        e=Entry(c23,width=30,bg='red',fg='white')
        f=Entry(c23,width=30,bg='red',fg='white')
        g=Entry(c23,width=30,bg='red',fg='white')
        h=Entry(c23,width=30,bg='red',fg='white')
        i=Entry(c23,width=30,bg='red',fg='white')
        j=Entry(c23,width=30,bg='red',fg='white')
        k=Entry(c23,width=30,bg='red',fg='white')
        lt=Entry(c23,width=30,bg='red',fg='white')

        a['values']=data
        a.insert(0, 'Select Registration Number ')
        l.place(x=440,y=20)
        l1.place(x=400,y=100)
        l2.place(x=400,y=150)
        l3.place(x=400,y=200)
        l4.place(x=400,y=250)
        l5.place(x=400,y=300)
        l6.place(x=400,y=350)
        l7.place(x=400,y=400)
        l8.place(x=400,y=450)
        l9.place(x=400,y=500)
        l10.place(x=400,y=550)
        l11.place(x=400,y=600)
        l12.place(x=400,y=650)

        a.place(x=610,y=100)
        b.place(x=610,y=150)
        c.place(x=610,y=200)
        d.place(x=610,y=250)
        e.place(x=610,y=300)
        f.place(x=610,y=350)
        g.place(x=610,y=400)
        h.place(x=610,y=450)
        i.place(x=610,y=500)
        j.place(x=610,y=550)
        k.place(x=610,y=600)
        lt.place(x=610,y=650)

        b1.place(x=490,y=700)
        b2.place(x=610,y=700)



        
    def UpdateRegistration():
        c24=Canvas(t,width=1300,height=800,bg='black')
        c24.place(x=200,y=0)
        def back():
            c24.destroy()
        def find():
         
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
             h.delete(0,100)
             i.delete(0,100)
             j.delete(0,100)
             k.delete(0,100)
             lt.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  registration where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
                h.insert(0,data[7])
                i.insert(0,data[8])
                j.insert(0,data[9])
                k.insert(0,data[10])
                lt.insert(0,data[11])
                
                
                
                
                

             db.close
        
             




        def update():
         
            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            v=(e.get())
            u=(f.get())
            q=int(g.get())
            s=(h.get())
            n=(i.get())
            m=(j.get())
            r=(k.get())
            t=(lt.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0 or q==0 or len(s)==0 or len(n)==0 or len(m)==0 or len(r)==0 or len(t)==0:
                messagebox.showerror('Error','Check All values first')
            else:
              sql="update registration set istid='%s',regname='%s',regemail='%s',regaddrees='%s',regbatchid='%s',regfees=%d,regdepartment='%s',regphone='%s',regcourseid='%s',regfeeplan='%s',coursename='%s' where regno='%s'"%(y,z,w,v,u,q,s,n,m,r,t,x)
              cur.execute(sql)
              db.commit()
              print('Data update')    
              db.close
              messagebox.showinfo("Status","Values updated")
              
              a.delete(0,100)
              a.insert(0,'Select Registration NO.')
              b.delete(0,100)
              b.insert(0,'Select Institute ID.')
              c.delete(0,100)
              d.delete(0,100)
              e.delete(0,100)
              f.delete(0,100)
              f.insert(0,'Select Batch ID.')
              g.delete(0,100)
              g.insert(0,'100')
              h.delete(0,100)
              h.insert(0,'Select Institute Name')
              i.delete(0,100)
              j.delete(0,100)
              j.insert(0,'Select Course ID.')
              k.delete(0,100)
              k.insert(0,'Select Feeplan.')
              lt.delete(0,100)
              lt.insert(0,'Select Course Name ')

           


        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from registration "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c24,text='Update Registration',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c24,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c24,text='Institude ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c24,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c24,text='Student Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c24,text='Student Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c24,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c24,text='Registration Fees:-  ',fg='red',font=('Georgia',15),bg='black')
        l8=Label(c24,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l9=Label(c24,text='Student Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l10=Label(c24,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l11=Label(c24,text='Fees Plan:-  ',fg='red',font=('Georgia',15),bg='black')
        l12=Label(c24,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')



        b1=Button(c24,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c24,text='CLOSE',width=10,bg='red',fg='white')
        b3=Button(c24,text='UPDATE',width=10,bg='red',fg='white',command=update)
        b4=Button(c24,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)

        a=ttk.Combobox(c24,width=30)
        c=Entry(c24,width=30,bg='red',fg='white')
        d=Entry(c24,width=30,bg='red',fg='white')
        e=Entry(c24,width=30,bg='red',fg='white')
        g=Entry(c24,width=30,bg='red',fg='white')
        g.insert(0,'100')
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istname from institute"
        cur.execute(sql)
        data5=cur.fetchall()
        h=ttk.Combobox(c24,width=30)
        h['values']=data5
        h.insert(0, 'Select Institute Name ')
        
        i=Entry(c24,width=30,bg='red',fg='white')
        a['values']=data
        a.insert(0, 'Select Registration Number ')
        
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istid from institute"
        cur.execute(sql)
        data2=cur.fetchall()
        b=ttk.Combobox(c24,width=30)
        b['values']=data2
        b.insert(0, 'Select Institute id ')
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select batchid from batch"
        cur.execute(sql)
        data1=cur.fetchall()
        f=ttk.Combobox(c24,width=30)
        f['values']=data1        
        f.insert(0, 'Select Batch id ')
      
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course"
        cur.execute(sql)
        data3=cur.fetchall()
        j=ttk.Combobox(c24,width=30)
        j['values']=data3 
        j.insert(0, 'Select Course id ')
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select feeplanid from feesplans"
        cur.execute(sql)
        data4=cur.fetchall()
        k=ttk.Combobox(c24,width=30)
        k['values']=data4
        k.insert(0, 'Select Feesplan id ')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select Coursename from course"
        cur.execute(sql)
        data6=cur.fetchall()
        lt=ttk.Combobox(c24,width=30)
        lt['values']=data6
        lt.insert(0, 'Select Course Name ')
        
        l.place(x=440,y=20)
        l1.place(x=400,y=100)
        l2.place(x=400,y=150)
        l3.place(x=400,y=200)
        l4.place(x=400,y=250)
        l5.place(x=400,y=300)
        l6.place(x=400,y=350)
        l7.place(x=400,y=400)
        l8.place(x=400,y=450)
        l9.place(x=400,y=500)
        l10.place(x=400,y=550)
        l11.place(x=400,y=600)
        l12.place(x=400,y=650)


        a.place(x=610,y=100)
        b.place(x=610,y=150)
        c.place(x=610,y=200)
        d.place(x=610,y=250)
        e.place(x=610,y=300)
        f.place(x=610,y=350)
        g.place(x=610,y=400)
        h.place(x=610,y=450)
        i.place(x=610,y=500)
        j.place(x=610,y=550)
        k.place(x=610,y=600)
        lt.place(x=610,y=650)


        b1.place(x=420,y=700)
        b2.place(x=555,y=700)
        b3.place(x=690,y=700)

        


    def DeleteRegistration():
        c25=Canvas(t,width=1300,height=800,bg='black')
        c25.place(x=200,y=0)
        def back():
            c25.destroy()
        def delete():                       

            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            v=(e.get())
            u=(f.get())
            q=int(g.get())
            s=(h.get())
            n=(i.get())
            m=(j.get())
            r=(k.get())
            t=(lt.get())
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0 or q==0 or len(s)==0 or len(n)==0 or len(m)==0 or len(r)==0 or len(t)==0:
                messagebox.showerror('Error','Check All values first')
            else:
               sql="delete from registration where regno='%s'"%(x)
               cur.execute(sql)
               db.commit()
               db.close
               messagebox.showinfo("Status","Values deleted")
               
               db=pymysql.connect(host='localhost',user='root',password='root',database='project')
               cur=db.cursor()
               sql="select count(*) from registration where istid='%s'"%(y)
               cur.execute(sql)
               data=cur.fetchone()
               print(data[0])
               print(type(data[0]))
               
               us.insert(0,data[0])
               
               usv=int(us.get())
               print(usv)
               
               db=pymysql.connect(host='localhost',user='root',password='root',database='project')
               cur=db.cursor()
               sql="update institute set iststrength=%d where istid='%s'"%(usv,y)
               cur.execute(sql)
               db.commit()
               print('institute update')    
               db.close
               
               a.delete(0,100)
               a.insert(0,'Select Registration NO.')
               b.delete(0,100)
               c.delete(0,100)
               d.delete(0,100)
               e.delete(0,100)
               f.delete(0,100)
               g.delete(0,100)
               g.insert(0,'0')
               h.delete(0,100)
               i.delete(0,100)
               j.delete(0,100)
               k.delete(0,100)
               lt.delete(0,100)
               
            
        def find():
              
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
             g.insert(0,'0')
             h.delete(0,100)
             i.delete(0,100)
             j.delete(0,100)
             k.delete(0,100)
             lt.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  registration where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
                h.insert(0,data[7])
                i.insert(0,data[8])
                j.insert(0,data[9])
                k.insert(0,data[10])
                lt.insert(0,data[11])
             db.close
        
           

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from registration "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c25,text='Delete Registration',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c25,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c25,text='Institude ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c25,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c25,text='Student Email:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c25,text='Student Address:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c25,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c25,text='Registration Fees:-  ',fg='red',font=('Georgia',15),bg='black')
        l8=Label(c25,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l9=Label(c25,text='Student Phone:-  ',fg='red',font=('Georgia',15),bg='black')
        l10=Label(c25,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l11=Label(c25,text='Fees Plan:-  ',fg='red',font=('Georgia',15),bg='black')
        l12=Label(c25,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')


        us=Entry(c25,width=30,bg='red',fg='white')
        b1=Button(c25,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c25,text='CLOSE',width=10,bg='red',fg='white')
        b3=Button(c25,text='DELETE',width=10,bg='red',fg='white',command=delete)
        b4=Button(c25,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)

        a=ttk.Combobox(c25,width=30)
        b=Entry(c25,width=30,bg='red',fg='white')
        c=Entry(c25,width=30,bg='red',fg='white')
        d=Entry(c25,width=30,bg='red',fg='white')
        e=Entry(c25,width=30,bg='red',fg='white')
        f=Entry(c25,width=30,bg='red',fg='white')
        g=Entry(c25,width=30,bg='red',fg='white')
        g.insert(0 ,'0')
        h=Entry(c25,width=30,bg='red',fg='white')
        i=Entry(c25,width=30,bg='red',fg='white')
        j=Entry(c25,width=30,bg='red',fg='white')
        k=Entry(c25,width=30,bg='red',fg='white')
        lt=Entry(c25,width=30,bg='red',fg='white')

        a['values']=data
        a.insert(0, 'Select Registration Number ')
        l.place(x=440,y=20)
        l1.place(x=400,y=100)
        l2.place(x=400,y=150)
        l3.place(x=400,y=200)
        l4.place(x=400,y=250)
        l5.place(x=400,y=300)
        l6.place(x=400,y=350)
        l7.place(x=400,y=400)
        l8.place(x=400,y=450)
        l9.place(x=400,y=500)
        l10.place(x=400,y=550)
        l11.place(x=400,y=600)
        l12.place(x=400,y=650)


        a.place(x=610,y=100)
        b.place(x=610,y=150)
        c.place(x=610,y=200)
        d.place(x=610,y=250)
        e.place(x=610,y=350)
        f.place(x=610,y=300)
        g.place(x=610,y=400)
        h.place(x=610,y=450)
        i.place(x=610,y=500)
        j.place(x=610,y=550)
        k.place(x=610,y=600)
        lt.place(x=610,y=650)


        b1.place(x=420,y=700)
        b2.place(x=555,y=700)
        b3.place(x=690,y=700)
        



        
    #  *************** Course Completion   **********************************************************************
    def InsertCompletion():
        c26=Canvas(t,width=1300,height=800,bg='black')
        c26.place(x=200,y=0)
        def back():
            c26.destroy()
        def insert():
             x=(a.get())
             y=(b.get())
             z=(c.get())
             w=(d.get())
             r=(e.get())
             s=(f.get())
             t=(g.get())
             
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(r)==0 or len(s)==0 or len(t)==0 :
                 messagebox.showerror('Error','Check All values first')
             else:
                sql="insert into coursecompletion values('%s','%s','%s','%s','%s','%s','%s')"%(x,y,z,w,r,s,t)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Status","Values inserted")
                
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="delete from registration where regno='%s'"%(x)
             cur.execute(sql)
             db.commit()
             db.close
           

        def cleardata():
             a.delete(0,100)
             a.insert(0,"Select Registration Number")
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             d.insert(0, mt)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)

    
        def find():
            
            b.delete(0,100)
            c.delete(0,100)
            d.delete(0,100)
            d.insert(0, mt)
            e.delete(0,100)
            f.delete(0,100)
            g.delete(0,100)
            
            x=(a.get())   
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from  registration where regno='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
               messagebox.showerror("status","Record not found")
            else:
               b.insert(0,data[5])
               c.insert(0,data[9])
               e.insert(0,data[2])
               f.insert(0,data[7])
               g.insert(0,data[11])

               
               
            db.close
        
            
            

        

         
        l=Label(c26,text='INSERT Course Completion',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c26,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c26,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c26,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c26,text='Date of complition:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c26,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c26,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c26,text='Course Name:- ',fg='red',font=('Georgia',15),bg='black')

        b1=Button(c26,text='INSERT',width=10,bg='red',fg='white',command=insert)
        b2=Button(c26,text='CLEAR',width=10,bg='red',fg='white',command=cleardata)
        b3=Button(c26,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c26,text='Find',width=7,bg='red',fg='white',command=find)
        b4.place(x=850,y=120)

        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from registration"
        cur.execute(sql)
        data4=cur.fetchall()
        a=ttk.Combobox(c26,width=30)
        a['values']=data4
        a.insert(0, 'Select Registration Number')
        d=Entry(c26,width=30,bg='red',fg='white')
        b=Entry(c26,width=30,bg='red',fg='white')
        c=Entry(c26,width=30,bg='red',fg='white')
        e=Entry(c26,width=30,bg='red',fg='white')
        f=Entry(c26,width=30,bg='red',fg='white')
        g=Entry(c26,width=30,bg='red',fg='white')


        
        
        
      
        
        

        l.place(x=340,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)
        
        '''  tl= time.time()
        at=time.localtime(tl)
        mt=time.asctime(at)'''
        mt=date.today()
        print(mt)
        d.insert(0, mt)

        a.place(x=610,y=120)
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)


        b1.place(x=490,y=490)
        b2.place(x=620,y=490)
        

        


    def FindCompletion():
        c27=Canvas(t,width=1300,height=800,bg='black')
        c27.place(x=200,y=0)
        def back():
            c27.destroy()
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  coursecompletion where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])

                
             db.close
        def cleardata():
             a.delete(0,100)
             a.insert(0,'Select Registration NO.')
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
             
        def refresh():
            l.place(x=200,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            l4.place(x=200,y=270) 
            l5.place(x=200,y=320)
            l6.place(x=200,y=370) 
            l7.place(x=200,y=420)
           
            a.place(x=420,y=120)
            b.place(x=420,y=170)
            c.place(x=420,y=220)
            d.place(x=420,y=270)
            e.place(x=420,y=320)
            f.place(x=420,y=370)
            g.place(x=420,y=420)
            
            b1.place(x=290,y=480)
            b2.place(x=420,y=480)
            b3.place(x=20,y=30)

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from coursecompletion "
        cur.execute(sql)
        data=cur.fetchall()    
        l=Label(c27,text='Find Course Completion',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c27,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c27,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c27,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c27,text='Date of complition:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c27,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c27,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c27,text='Course Name:- ',fg='red',font=('Georgia',15),bg='black')

        b1=Button(c27,text='Find',width=10,bg='red',fg='white',command=find)
        b2=Button(c27,text='CLEAR',width=10,bg='red',fg='white',command=cleardata)
        b3=Button(c27,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c27,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=30)
        a=ttk.Combobox(c27,width=30)
        b=Entry(c27,width=30,bg='red',fg='white')
        c=Entry(c27,width=30,bg='red',fg='white')
        d=Entry(c27,width=30,bg='red',fg='white')
        e=Entry(c27,width=30,bg='red',fg='white')
        f=Entry(c27,width=30,bg='red',fg='white')
        g=Entry(c27,width=30,bg='red',fg='white')

        l.place(x=340,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)


        a.place(x=610,y=120)
        a['values']=data
        a.insert(0, 'Select Registration Number ')
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)


        b1.place(x=490,y=490)
        b2.place(x=620,y=490)
        
        



    def UpdateCompletion():
        c28=Canvas(t,width=1300,height=800,bg='black')
        c28.place(x=200,y=0)
        def back():
            c28.destroy()
        def find():
            
            b.delete(0,100)
            c.delete(0,100)
            d.delete(0,100)
            e.delete(0,100)
            f.delete(0,100)
            g.delete(0,100)

            x=(a.get())   
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from  coursecompletion where regno='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
               messagebox.showerror("status","Record not found")
            else:
               b.insert(0,data[1])
               c.insert(0,data[2])
               d.insert(0,data[3])
               e.insert(0,data[4])
               f.insert(0,data[5])
               g.insert(0,data[6])

            db.close
            


        def update():

            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            r=(e.get())
            s=(f.get())
            t=(g.get())
           
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(r)==0 or len(s)==0 or len(t)==0:
                messagebox.showerror('Error','Check All values first')
            else:
              sql="update coursecompletion set batchid='%s',courseid='%s',dateofcompletion='%s', coursecomplstname='%s',istname='%s',coursename='%s' where regno='%s'"%(y,z,w,r,s,t,x)
              cur.execute(sql)
              db.commit()
              print('Data update')    
              db.close
              messagebox.showinfo("Status","Values updated")
              
              a.delete(0,100)
              a.insert(0,'Select Registration NO.')
              b.delete(0,100)
              b.insert(0,'Select Batch ID.')
              c.delete(0,100)
              c.insert(0,'Select Course ID.')
              d.delete(0,100)
              d.insert(0,mt)
              e.delete(0,100)
              e.insert(0,'Select Student Name.')
              f.delete(0,100)
              f.insert(0,'Select Institute Name.')
              g.delete(0,100)
              g.insert(0,'Select Course Name.')

        

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from coursecompletion "
        cur.execute(sql)
        data=cur.fetchall()    
        l=Label(c28,text='Update Course Completion',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c28,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c28,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c28,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c28,text='Date of complition:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c28,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c28,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c28,text='Course Name:- ',fg='red',font=('Georgia',15),bg='black')
        
        b1=Button(c28,text='Find',width=10,bg='red',fg='white',command=find)
        b2=Button(c28,text='CLOSE',width=10,bg='red',fg='white')
        b3=Button(c28,text='UPDATE',width=10,bg='red',fg='white',command=update)
        b4=Button(c28,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)

        a=ttk.Combobox(c28,width=30)
        d=Entry(c28,width=30,bg='red',fg='white')

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select batchid from batch"
        cur.execute(sql)
        data1=cur.fetchall()
        b=ttk.Combobox(c28,width=30)
        b.insert(0,'Select Batch ID.')
        b['values']=data1 
        
        tl= time.time()
        at=time.localtime(tl)
        mt=time.asctime(at)
        print(mt)
        d.insert(0, mt)
        
        e=Entry(c28,width=30,bg='red',fg='white')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istname from institute"
        cur.execute(sql)
        data2=cur.fetchall()
        f=ttk.Combobox(c28,width=30)
        f.insert(0,'Select Institute Name.')
        f['values']=data2 
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select coursename from course"
        cur.execute(sql)
        data4=cur.fetchall()
        g=ttk.Combobox(c28,width=30)
        g.insert(0,'Select Course Name.')
        g['values']=data4 
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select coursecomplstname from coursecompletion"
        cur.execute(sql)
        data5=cur.fetchall()
        e=ttk.Combobox(c28,width=30)
        e.insert(0,'Select Student Name.')
        e['values']=data5 


        
      
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select courseid from course"
        cur.execute(sql)
        data3=cur.fetchall()
        c=ttk.Combobox(c28,width=30)
        c.insert(0,'Select Course ID.')
        c['values']=data3

        l.place(x=340,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)


        a.place(x=610,y=120)
        a['values']=data
        a.insert(0, 'Select Registration Number ')
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)



        b1.place(x=440,y=490)
        b2.place(x=560,y=490)
        b3.place(x=680,y=490)

       
        
       
        
    def DeleteCompletion():
        c29=Canvas(t,width=1300,height=800,bg='black')
        c29.place(x=200,y=0)
        def back():
            c29.destroy()
        def delete():

            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            r=(e.get())
            s=(f.get())
            t=(g.get())
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="delete from coursecompletion where regno='%s'"%(x)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo("Status","Values deleted")
            db.close()
            
            a.delete(0,100)
            a.insert(0,'Select Registration NO.')
            b.delete(0,100)
            c.delete(0,100)
            d.delete(0,100)
            e.delete(0,100)
            f.delete(0,100)
            g.delete(0,100)
            
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             g.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  coursecompletion where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
                g.insert(0,data[6])
             db.close
            

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from coursecompletion "
        cur.execute(sql)
        data=cur.fetchall()    
        l=Label(c29,text='Delete Course Completion',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c29,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c29,text='Batch ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c29,text='Course ID:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c29,text='Date of complition:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c29,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c29,text='Institute Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l7=Label(c29,text='Course Name:- ',fg='red',font=('Georgia',15),bg='black')

        b1=Button(c29,text='Find',width=10,bg='red',fg='white',command=find)
        b2=Button(c29,text='CLOSE',width=10,bg='red',fg='white')
        b3=Button(c29,text='DELETE',width=10,bg='red',fg='white',command=delete)
        b4=Button(c29,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)

        a=ttk.Combobox(c29,width=30)
        a.insert(0,'Select Registration NO.')

        b=Entry(c29,width=30,bg='red',fg='white')
        c=Entry(c29,width=30,bg='red',fg='white')
        d=Entry(c29,width=30,bg='red',fg='white')
        e=Entry(c29,width=30,bg='red',fg='white')
        f=Entry(c29,width=30,bg='red',fg='white')
        g=Entry(c29,width=30,bg='red',fg='white')


        l.place(x=340,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)
        l7.place(x=400,y=420)


        a.place(x=610,y=120)
        a['values']=data
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)
        g.place(x=610,y=420)


        b1.place(x=440,y=490)
        b2.place(x=560,y=490)
        b3.place(x=680,y=490)
        
        
    #  *************** Certificate  **********************************************************************
    def InsertCertificate():
        c30=Canvas(t,width=1300,height=800,bg='black')
        c30.place(x=200,y=0)
        def back():
            c30.destroy()
        def insert():
             x=(a.get())
             y=(b.get())
             z=(c.get())
             w=(d.get())
             v=(e.get())
             u=(f.get())
             
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0:
                 messagebox.showerror('Error','Check All values first')
             else:
               sql="insert into certificate values('%s','%s','%s','%s','%s','%s')"%(x,y,z,w,v,u)
               cur.execute(sql)
               db.commit()
               messagebox.showinfo("Status","Values inserted")
               
               a.delete(0,100)
               a.insert(0,'Select Registration Number')
               b.delete(0,100)
               c.delete(0,100)
               d.delete(0,100)
               d.insert(0, mt)
               e.delete(0,100)
               f.delete(0,100)
             
             
        def find():
            
            b.delete(0,100)
            c.delete(0,100)
            d.delete(0,100)
            d.insert(0, mt)
            e.delete(0,100)
            f.delete(0,100)
            
            
            x=(a.get())   
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="select * from  coursecompletion where regno='%s'"%(x)
            cur.execute(sql)
            data=cur.fetchone()
            if data==None:
               messagebox.showerror("status","Record not found")
            else:
               b.insert(0,data[4])
               c.insert(0,data[2])
               e.insert(0,data[5])
               f.insert(0,data[7])
            db.close
            
            
                   
           
            


        btncheck=Button(c30,text='Find',bg='red',fg='white',command=find)
        btncheck.place(x=820,y=120)
        lblcheck=Label(c30,bg='black')
        lblcheck.place(x=610,y=140)


         
        l=Label(c30,text='INSERT CERTIFICATE',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c30,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c30,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c30,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c30,text='Issue Date:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c30,text='Institude Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c30,text='Certificate Number:-  ',fg='red',font=('Georgia',15),bg='black')


        b1=Button(c30,text='INSERT',width=10,bg='red',fg='white',command=insert)
        b2=Button(c30,text='CLOSE',width=10,bg='red',fg='white')
        b3=Button(c30,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from coursecompletion"
        cur.execute(sql)
        data4=cur.fetchall()
        a=ttk.Combobox(c30,width=30)
        a['values']=data4
        a.insert(0, 'Select Registration Number')
        
        
        
        b=Entry(c30,width=30,bg='red',fg='white')
        c=Entry(c30,width=30,bg='red',fg='white')
        d=Entry(c30,width=30,bg='red',fg='white')
        e=Entry(c30,width=30,bg='red',fg='white')

        
       
        
        f=Entry(c30,width=30,bg='red',fg='white')

        mt=date.today()
        print(mt)
        d.insert(0, mt)

        l.place(x=390,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)




        a.place(x=610,y=120)
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)



        b1.place(x=490,y=430)
        b2.place(x=610,y=430)


        
    def FindCertificate():
        c31=Canvas(t,width=1300,height=800,bg='black')
        c31.place(x=200,y=0)
        def back():
            c31.destroy()
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             d.insert(0,100)
             e.delete(0,100)
             f.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  certificate where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
             db.close
        def cleardata():
             a.delete(0,100)
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             e.delete(0,100)
             f.delete(0,100)
             
        def refresh():
            l.place(x=200,y=30)
            l1.place(x=200,y=120)
            l2.place(x=200,y=170)
            l3.place(x=200,y=220)
            l4.place(x=200,y=270) 
            l5.place(x=200,y=320)
            l6.place(x=200,y=370) 
           
            a.place(x=420,y=120)
            b.place(x=420,y=170)
            c.place(x=420,y=220)
            d.place(x=420,y=270)
            e.place(x=420,y=320)
            f.place(x=420,y=370)
            
            b1.place(x=290,y=450)
            b2.place(x=420,y=450)
            b3.place(x=20,y=30)
             
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from certificate "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c31,text='     Find Certificate',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c31,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c31,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c31,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c31,text='Issue Date:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c31,text='Institude Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c31,text='Certificate Number:-  ',fg='red',font=('Georgia',15),bg='black')


        b1=Button(c31,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c31,text='CLEAR',width=10,bg='red',fg='white',command=cleardata)
        b3=Button(c31,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b3.place(x=40,y=30)
        b4=Button(c31,text='Specification',bg='red',fg='white',command=refresh)
        b4.place(x=1050,y=30)
        a=ttk.Combobox(c31,width=30)
        b=Entry(c31,width=30,bg='red',fg='white')
        c=Entry(c31,width=30,bg='red',fg='white')
        d=Entry(c31,width=30,bg='red',fg='white')
        e=Entry(c31,width=30,bg='red',fg='white')
        f=Entry(c31,width=30,bg='red',fg='white')



        l.place(x=390,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)




        a.place(x=610,y=120)
        a['values']=data
        a.insert(0, 'Select Registration Number ')
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)



        b1.place(x=490,y=430)
        b2.place(x=610,y=430)
        



        
        
        
        
    def UpdateCertificate():
        c32=Canvas(t,width=1300,height=800,bg='Black')
        c32.place(x=200,y=0)
        def back():
            c32.destroy()
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             d.insert(0,100)
             e.delete(0,100)
             f.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  certificate where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])

             db.close
            



        def update():
         
             x=(a.get())
             y=(b.get())
             z=(c.get())
             w=(d.get())
             v=(e.get())
             u=(f.get())

             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             if len(x)==0 or len(y)==0 or len(z)==0 or len(w)==0 or len(v)==0 or len(u)==0:
                 messagebox.showerror('Error','Check All values first')
             else:
               sql="update certificate set name='%s',coursename='%s',issuedate='%s',istname='%s',certno='%s' where regno='%s'"%(y,z,w,v,u,x)
               cur.execute(sql)
               db.commit()
               print('Data update')    
               db.close
               messagebox.showinfo("Status","Values updated")
               
               a.delete(0,100)
               a.insert(0,"Select Ragistration Number")
               b.delete(0,100)
               c.delete(0,100)
               d.delete(0,100)
               e.delete(0,100)
               e.insert(0,"select Institute Name")
               f.delete(0,100)

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from certificate "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c32,text='     Update Certificate',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c32,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c32,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c32,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c32,text='Issue Date:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c32,text='Institude Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c32,text='Certificate Number:-  ',fg='red',font=('Georgia',15),bg='black')


        b1=Button(c32,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c32,text='CLEAR',width=10,bg='red',fg='white')
        b3=Button(c32,text='Update',width=10,bg='red',fg='white',command=update)
        b4=Button(c32,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)
        a=ttk.Combobox(c32,width=30)
        b=Entry(c32,width=30,bg='red',fg='white')
        c=Entry(c32,width=30,bg='red',fg='white')
        d=Entry(c32,width=30,bg='red',fg='white')
        
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select istname from institute"
        cur.execute(sql)
        data4=cur.fetchall()
        e=ttk.Combobox(c32,width=30)
        e['values']=data4
        e.insert(0, 'Select Institute Name')
        
        f=Entry(c32,width=30,bg='red',fg='white')



        l.place(x=390,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)




        a.place(x=610,y=120)
        a['values']=data
        a.insert(0, 'Select Registration Number ')
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)



        b1.place(x=460,y=430)
        b2.place(x=580,y=430)
        b3.place(x=690,y=430)
       

        
    def DeleteCertificate():
        c33=Canvas(t,width=1300,height=800,bg='black')
        c33.place(x=200,y=0)
        def back():
            c33.destroy()
        def delete():

            x=(a.get())
            y=(b.get())
            z=(c.get())
            w=(d.get())
            v=(e.get())
            u=(f.get())
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
            cur=db.cursor()
            sql="delete from certificate where regno='%s'"%(x)
            cur.execute(sql)
            db.commit()
            db.close
            messagebox.showinfo("Status","Values deleted")
            
            a.delete(0,100)
            b.delete(0,100)
            c.delete(0,100)
            d.delete(0,100)
            e.delete(0,100)
            f.delete(0,100)
            
        def find():
            
             b.delete(0,100)
             c.delete(0,100)
             d.delete(0,100)
             d.insert(0,100)
             e.delete(0,100)
             f.delete(0,100)
         
             x=(a.get())   
             db=pymysql.connect(host='localhost',user='root',password='root',database='project')
             cur=db.cursor()
             sql="select * from  certificate where regno='%s'"%(x)
             cur.execute(sql)
             data=cur.fetchone()
             if data==None:
                messagebox.showerror("status","Record not found")
             else:
                b.insert(0,data[1])
                c.insert(0,data[2])
                d.insert(0,data[3])
                e.insert(0,data[4])
                f.insert(0,data[5])
             db.close
            

        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select regno from certificate "
        cur.execute(sql)
        data=cur.fetchall()
        l=Label(c33,text='     Delete Certificate',fg='red',bg='black',font=('Georgia',30))
        l1=Label(c33,text='Registration Number:-  ',fg='red',bg='black',font=('Georgia',15))
        l2=Label(c33,text='Student Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l3=Label(c33,text='Course Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l4=Label(c33,text='Issue Date:-  ',fg='red',font=('Georgia',15),bg='black')
        l5=Label(c33,text='Institude Name:-  ',fg='red',font=('Georgia',15),bg='black')
        l6=Label(c33,text='Certificate Number:-  ',fg='red',font=('Georgia',15),bg='black')


        b1=Button(c33,text='FIND',width=10,bg='red',fg='white',command=find)
        b2=Button(c33,text='CLEAR',width=10,bg='red',fg='white')
        b3=Button(c33,text='DELETE',width=10,bg='red',fg='white',command=delete)
        b4=Button(c33,text='<−−−−−',bg='black',fg='red',font=('Georgia',20),border=0,command=back)
        b4.place(x=40,y=30)
        a=ttk.Combobox(c33,width=30)
        b=Entry(c33,width=30,bg='red',fg='white')
        c=Entry(c33,width=30,bg='red',fg='white')
        d=Entry(c33,width=30,bg='red',fg='white')
        e=Entry(c33,width=30,bg='red',fg='white')
        f=Entry(c33,width=30,bg='red',fg='white')



        l.place(x=390,y=30)
        l1.place(x=400,y=120)
        l2.place(x=400,y=170)
        l3.place(x=400,y=220)
        l4.place(x=400,y=270)
        l5.place(x=400,y=320)
        l6.place(x=400,y=370)




        a.place(x=610,y=120)
        a['values']=data
        a.insert(0, 'Select Registration Number ')
        b.place(x=610,y=170)
        c.place(x=610,y=220)
        d.place(x=610,y=270)
        e.place(x=610,y=320)
        f.place(x=610,y=370)



        b1.place(x=460,y=430)
        b2.place(x=580,y=430)
        b3.place(x=690,y=430)
        

        

    c=Canvas(t,width=200,height=800,bg='red')
    c.place(x=0,y=0)
    x=IntVar()
    A=Label(c,text='Institute               ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=20)
    b1=Radiobutton(c,text='Insert',variable=x,value=1,command=InsertInstitute,bg='red')
    b2=Radiobutton(c,text='Find',variable=x,value=2,command=FindInstitute,bg='red')
    b3=Radiobutton(c,text='Update',variable=x,value=3,command=UpdateInstitute,bg='red')
    b4=Radiobutton(c,text='Delete',variable=x,value=4,command=DeleteInstitute,bg='red')
    b1.place(x=20,y=50)
    b2.place(x=90,y=50)
    b3.place(x=20,y=70)
    b4.place(x=90,y=70)
    A=Label(c,text='Course                  ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=100)
    b5=Radiobutton(c,text='Insert',variable=x,value=5,command=InsertCourse,bg='red')
    b6=Radiobutton(c,text='Find',variable=x,value=6,command=FindCourse,bg='red')
    b7=Radiobutton(c,text='Update',variable=x,value=7,command=UpdateCourse,bg='red')
    b8=Radiobutton(c,text='Delete',variable=x,value=8,command=DeleteCourse,bg='red')
    b5.place(x=20,y=130)
    b6.place(x=90,y=130)
    b7.place(x=20,y=150)
    b8.place(x=90,y=150)
    A=Label(c,text='Batch                     ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=180)
    b9=Radiobutton(c,text='Insert',variable=x,value=9,command=InsertBatch,bg='red')
    b10=Radiobutton(c,text='Find',variable=x,value=10,command=FindBatch,bg='red')
    b11=Radiobutton(c,text='Update',variable=x,value=11,command=UpdateBatch,bg='red')
    b12=Radiobutton(c,text='Delete',variable=x,value=12,command=DeleteBatch,bg='red')
    b9.place(x=20,y=210)
    b10.place(x=90,y=210)
    b11.place(x=20,y=230)
    b12.place(x=90,y=230)
    A=Label(c,text='Feesplans           ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=260)
    b13=Radiobutton(c,text='Insert',variable=x,value=13,command=InsertFeeplans,bg='red')
    b14=Radiobutton(c,text='Find',variable=x,value=14,command=FindFeeplans,bg='red')
    b15=Radiobutton(c,text='Update',variable=x,value=15,command=UpdateFeeplans,bg='red')
    b16=Radiobutton(c,text='Delete',variable=x,value=16,command=DeleteFeeplans,bg='red')
    b13.place(x=20,y=290)
    b14.place(x=90,y=290)
    b15.place(x=20,y=310)
    b16.place(x=90,y=310)
    A=Label(c,text='Enquiry                 ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=340)
    b17=Radiobutton(c,text='Insert',variable=x,value=17,command=InsertEnquiry,bg='red')
    b18=Radiobutton(c,text='Find',variable=x,value=18,command=FindEnquiry,bg='red')
    b19=Radiobutton(c,text='Update',variable=x,value=19,command=UpdateEnquiry,bg='red')
    b20=Radiobutton(c,text='Delete',variable=x,value=20,command=DeleteEnquiry,bg='red')
    b17.place(x=20,y=370)
    b18.place(x=90,y=370)
    b19.place(x=20,y=390)
    b20.place(x=90,y=390)
    A=Label(c,text='Registration      ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=420)
    b21=Radiobutton(c,text='Insert',variable=x,value=21,command=InsertRegistration,bg='red')
    b22=Radiobutton(c,text='Find',variable=x,value=22,command=FindRegistration,bg='red')
    b23=Radiobutton(c,text='Update',variable=x,value=23,command=UpdateRegistration,bg='red')
    b24=Radiobutton(c,text='Delete',variable=x,value=24,command=DeleteRegistration,bg='red')
    b21.place(x=20,y=450)
    b22.place(x=90,y=450)
    b23.place(x=20,y=470)
    b24.place(x=90,y=470)
    A=Label(c,text='Cousrse Completion',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=10,y=500)
    b25=Radiobutton(c,text='Insert',variable=x,value=25,command=InsertCompletion,bg='red')
    b26=Radiobutton(c,text='Find',variable=x,value=26,command=FindCompletion,bg='red')
    b27=Radiobutton(c,text='Update',variable=x,value=27,command=UpdateCompletion,bg='red')
    b28=Radiobutton(c,text='Delete',variable=x,value=28,command=DeleteCompletion,bg='red')
    b25.place(x=20,y=530)
    b26.place(x=90,y=530)
    b27.place(x=20,y=550)
    b28.place(x=90,y=550)
    A=Label(c,text='Certificate         ',fg='white',font=('Copperplate Gothic Bold',15),bg='black')
    A.place(x=15,y=580)
    b29=Radiobutton(c,text='Insert',variable=x,value=29,command=InsertCertificate,bg='red')
    b30=Radiobutton(c,text='Find',variable=x,value=30,command=FindCertificate,bg='red')
    b31=Radiobutton(c,text='Update',variable=x,value=31,command=UpdateCertificate,bg='red')
    b32=Radiobutton(c,text='Delete',variable=x,value=32,command=DeleteCertificate,bg='red')
    b29.place(x=20,y=610)
    b30.place(x=90,y=610)
    b31.place(x=20,y=630)
    b32.place(x=90,y=630)




    t.mainloop()


def check():
    a=ue.get()
    b=pe.get()
    db=pymysql.connect(host='localhost',user='root',password='root',database='project')
    cur=db.cursor()
    sql="select password from user where username ='%s' "%(a)
    cur.execute(sql)
    data=cur.fetchone()
    if data==None:
        messagebox.showerror('Status','     Invalid User           ')
    else:
        l1.insert(0, data[0])
        pw=l1.get()
        if b==pw:
            login()
        else:
            messagebox.showerror('Alart','       Wonge Password        ')
            l1.delete(0, 100)
    db.close()
    
def account():
    print('call this')
    acc=Canvas(lll,width=1300,height=800,bg='red')
    acc.place(x=850,y=0)
    
    
    def newotp():
        
        
        y=random.randint(1000, 9999)
        
            
        
        
        def newotpcheck():
            newotpv=int(cotpe.get())
            if newotpv==y:
                
                
                def usercreate():
                   
                    newz=(newpee.get())
                    
                    db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                    cur=db.cursor()
                    sql="insert into user values('%s','%s','%s')"%(newid,newz,newgmail)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo("Status","Account Created")
                  
                      
                
                newp=Label(acc,text='Create password :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',15))
                newp.place(x=10,y=400)
                newpee=Entry(acc,width=40,bg='black',fg='white')
                newpee.place(x=230,y=410)
                newb=Button(acc,text='                 Create             -> ',bg='black',fg='white',font=('Georgia',10),command=usercreate)
                newb.place(x=125,y=450)
                
                
                
        
        newid=cnewe.get()
        newgmail=cgmle.get()
        
        
        from_address = "utkarsh4549@gmail.com"
        to_address = newgmail
        msg=MIMEMultipart('alternative')
        msg['Subject'] = "Run Email Code"
        msg['From'] = from_address
        msg['To'] = to_address
        html = " Dear Sir/ma'am,' <br>Your One Time Password (OTP) is :- <br>" + str(y) +"<br> Do not share your OTP with anyone including your depository participant(DP)."                              
        part1 = MIMEText(html,'html')
        msg.attach(part1)
        username = 'utkarsh4549@gmail.com'
        password = 'fxmrdccfhnfacqmz'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print('OTP sent')
        
        otpl=Label(acc,text='Enter OTP :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',20))
        otpl.place(x=50,y=300)
        cotpe=Entry(acc,width=20,bg='black',fg='white')
        cotpe.place(x=260,y=315)
        cotpb=Button(acc,text='                 Confirm              -> ',bg='black',fg='white',font=('Georgia',10),command=newotpcheck)
        cotpb.place(x=125,y=360)
        
    
    cnew=Label(acc,text='User id :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',20))
    cnew.place(x=50,y=100)
    cnewe=Entry(acc,width=40,bg='black',fg='white')
    cnewe.place(x=200,y=110)
    
    cgml=Label(acc,text='Gmail :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',20))
    cgml.place(x=50,y=150)
    cgmle=Entry(acc,width=40,bg='black',fg='white')
    cgmle.place(x=200,y=160)
    gmlb=Button(acc,text='                 sent              -> ',bg='black',fg='white',font=('Georgia',10),command=newotp)
    gmlb.place(x=125,y=220)
    
    
def forpass():
    x=random.randint(1000, 9999)
    def otp():
        
        uid=gmleu.get()
        ugmail=gmle.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database='project')
        cur=db.cursor()
        sql="select gmail from user where username ='%s' "%(uid)
        cur.execute(sql)
        data=cur.fetchone()
        if data==None:
            messagebox.showerror('Status','     Invalid User           ')
        else:
            ggg.insert(0, data[0])
            gw=ggg.get()
            if ugmail==gw:
                
                
                def otpcheck():
                    otpvalue=int(otpe.get())
                    print('value',x)
                    print('otp',otpvalue)
                    if otpvalue==x:
                        
                        def changepass():
                            npass=newpe.get()
                            nrpass=rnewpe.get()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='project')
                            cur=db.cursor()
                            if npass==nrpass:
                                sql="update user set password='%s' where username='%s'"%(npass,uid)
                                cur.execute(sql)
                                db.commit()
                                print('Password update')    
                                db.close
                                messagebox.showinfo("Status","Password Changed")
                                log.destroy()
                            else:
                                messagebox.showerror('not same','Your Password not Same ')
                            
                        
                         
                        
                        

                        
                        newp=Label(log,text='New Password :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',15))
                        newp.place(x=10,y=400)
                        newpe=Entry(log,width=40,bg='black',fg='white')
                        newpe.place(x=230,y=410)
                        rnewp=Label(log,text='Re-Enter Password :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',15))
                        rnewp.place(x=10,y=450)
                        rnewpe=Entry(log,width=40,bg='black',fg='white')
                        rnewpe.place(x=230,y=460)
                        newb=Button(log,text='                 Change              -> ',bg='black',fg='white',font=('Georgia',10),command=changepass)
                        newb.place(x=125,y=510)
                    else:
                        messagebox.showerror('wonge','   Wonge OTP   ')
                
               
                from_address = "sahilsharma93685@gmail.com"
                to_address = gw
                msg=MIMEMultipart('alternative')
                msg['Subject'] = "OTP"
                msg['From'] = from_address
                msg['To'] = to_address
                html = " Dear Sir/ma'am,' <br>Your One Time Password (OTP) is :- <br>" + str(x) +"<br> Do not share your OTP with anyone including your depository participant(DP)."               
                part1 = MIMEText(html,'html')
                msg.attach(part1)
                username = 'sahilsharma93685@gmail.com'
                password = 'fxmrdccfhnfacqmz'
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login(username, password)
                server.sendmail(from_address, to_address, msg.as_string())
                server.quit()
                print('OTP sent')
                
                otpl=Label(log,text='Enter OTP :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',20))
                otpl.place(x=50,y=300)
                otpe=Entry(log,width=20,bg='black',fg='white')
                otpe.place(x=260,y=315)
                otpb=Button(log,text='                 Confirm              -> ',bg='black',fg='white',font=('Georgia',10),command=otpcheck)
                otpb.place(x=125,y=360)
                
            else:
                messagebox.showerror('Alart','       Wonge Gmail       ')
        
        
        
     
    
    log=Canvas(lll,width=1300,height=800,bg='red')
    log.place(x=850,y=0)
    
    gmlu=Label(log,text='User id :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',20))
    gmlu.place(x=50,y=100)
    gmleu=Entry(log,width=40,bg='black',fg='white')
    ggg=Entry(log,width=40,bg='black',fg='white')
    gmleu.place(x=200,y=110)
    
    gml=Label(log,text='Gmail :- ',fg='black',bg='red',font=('Copperplate Gothic Bold',20))
    gml.place(x=50,y=150)
    gmle=Entry(log,width=40,bg='black',fg='white')
    gmle.place(x=200,y=160)
    gmlb=Button(log,text='                 get              -> ',bg='black',fg='white',font=('Georgia',10),command=otp)
    gmlb.place(x=125,y=220)

    
    
    
lll=Canvas(t,width=1700,height=800,bg='Black')
lll.place(x=0,y=0)  
l1=Entry(lll,width=20)
u=Label(lll,text='Username :- ',fg='red',bg='black',font=('Georgia',20))
p=Label(lll,text='Password :- ',fg='red',bg='black',font=('Georgia',20))
ue=Entry(lll,width=30,bg='red',fg='white')
pe=Entry(lll,width=30,bg='red',fg='white',show='*')
u.place(x=450,y=150)
p.place(x=450,y=220)
ue.place(x=660,y=160)
pe.place(x=660,y=230)

b1=Button(lll,text='                      Login                    ->   ',bg='red',fg='white',font=('Georgia',10),command=check)
b2=Button(lll,text='      Forget Password ?       ',bg='black',fg='green',font=('Georgia',10),border=0,command=forpass)
b1.place(x=530,y=300)
b2.place(x=705,y=250)
cre=Label(lll,text='---------------------------or------------------------------- ',fg='red',bg='black',font=('Georgia',15))
cre.place(x=440,y=360)
b3=Button(lll,text='Dont have a account yet ? Create... ',bg='green',fg='white',font=('Georgia',10),border=0,command=account)
def st():
   tm= time.strftime("%H:%M:%S") 
   tmm.config(text=tm)
   tmm.after(200,st)
   

tmm=Label(t,fg='green',bg='black',font=('OCR A Extended',20,'bold'))
tmm.place(x=100,y=150)
st()
b3.place(x=540,y=450)




def create_mines(lll):

    bubbles = []

    for __ in range(90):

        x = random.randint(0, 1400)
        y = random.randint(0, 800)
        r = random.randint(5, 5)

        mine = lll.create_rectangle(x-r, y-r, x+r, y+r,fill='red')

        bubbles.append( [mine, r] )

    return bubbles


def moves_mines(lll, bubbles):

    for mine, r in bubbles:

        #lll.move(mine, 0, -1)
        
        # get position
        x1, y1, x2, y2 = lll.coords(mine)

        # change 
        y1 -= 1
        y2 -= 1

        # if top then move to the bottom
        if y2 <= 0:
            y1 = 400
            y2 = y1 + 2*r
            
        # set position
        lll.coords(mine, x1, y1, x2, y2)
    # run after 40ms - it gives 25FPS
    t.after(40, moves_mines, lll, bubbles)

# --- main ---


lll.pack()
bubbles = create_mines(lll)
# run after 40ms - it gives 25FPS
t.after(800, moves_mines, lll, bubbles)
t.config(bg='red')

t.mainloop()






