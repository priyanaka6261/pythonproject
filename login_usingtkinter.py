from tkinter import *
from mysql.connector import *
import tkinter. messagebox as msg
def gui():
    root=Tk()
    global uname
    global password
    uname=StringVar()
    password=StringVar()

    lbltitle=Label(root,text="login")
    lbltitle.grid(row=0,column=0,columnspan=2)
    

    lbluname=Label(root,text="username")
    lbluname.grid(row=1,column=0)

    entuname=Entry(root,textvariable=uname)
    entuname.grid(row=1,column=1)

    lblpassword=Label(root,text="password")
    lblpassword.grid(row=2,column=0)

    entpassword=Entry(root,textvariable=password)
    entpassword.grid(row=2,column=1)

    btn=Button(root,text="login",command=db)
    btn.grid(row=3,column=1,columnspan=2)
    root.mainloop()

def db():
    con= connect(host="localhost",user="root",password="",database="dblecture4")
    cur=con.cursor()
    global uname
    global password
    qry=f"select * from logins where uname='{uname.get()}' and password='{password.get()}'"
    cur.execute(qry)
    result=cur.fetchone()

    if(result==None):
        msg.showerror("login failed","invalid username")
    else:
        name=uname.get()
        uname.set("")
        password.set("")
        var=msg.showinfo("login succesfull")
        if(var=='ok'):
            win=Tk()
            
            lbl=Label(win,text=name)
            lbl.grid()
        con.close ()
    
gui()        
        





    
