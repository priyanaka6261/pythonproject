from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="python"
        )
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("data inserted successfully")
def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("id is  mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row= cursor.fetchall()
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
            conn.commit()
            conn.close()
        else :
            msg.showinfo("id not found")
def update_data():
    if e_id.get()=="" or e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("update Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("data updated successfully")
def delete_data():
    if e_id.get()=="":
        msg.showinfo("delete  Status","id is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from  student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("data deleted successfully")        
    
            
        
        
root=Tk()
root.geometry("400x380")
root.title("My Desktop Application")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Arial",12))
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME",font=("Arial",12))
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last NAME",font=("Arial",12))
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",12))
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE",font=("Arial",12))
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root)
e_fname.place(x=200,y=100)

e_lname=Entry(root)
e_lname.place(x=200,y=150)

e_email=Entry(root)
e_email.place(x=200,y=200)

e_mobile=Entry(root)
e_mobile.place(x=200,y=250)

insert=Button(root,text="INSERT",font=("Arial",12),bg="yellow",fg="black",command=insert_data)
insert.place(x=50,y=300)

insert=Button(root,text="SEARCH",font=("Arial",12),bg="yellow",fg="black",command=search_data)
insert.place(x=121,y=300)

insert=Button(root,text="UPDATE",font=("Arial",12),bg="yellow",fg="black",command=update_data)
insert.place(x=203,y=300)

insert=Button(root,text="DELETE",font=("Arial",12),bg="yellow",fg="black",command=delete_data)
insert.place(x=283,y=300)

