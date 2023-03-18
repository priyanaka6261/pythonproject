import tkinter
from tkinter import *
win=Tk()
photo=PhotoImage(file='image.png')
lbl2 = Label(win,image=photo)
lbl2.place(x=0,y=0,relwidth=1,relheight=1)
win.geometry("500x500")
win.resizable(0,0)

win.columnconfigure(0,weight=1)
win.columnconfigure(1,weight=1)

lb1=Label(win,text="Login",bg="red",font=34)
lb1.grid(column=0,row=0,columnspan=2,sticky='nsew',)

lbluname=Label(win,text="Username",font=('Arial',14))
lbluname.grid(column=0,row=1,ipady=10,ipadx=10)
entuname=Entry(win)
entuname.grid(column=1,row=1)

lblpwd=Label(win,text="Password",font=('Arial',14))
lblpwd.grid(column=0,row=2)
entpwd=Entry(win)
entpwd.grid(column=1,row=2)

btnlogin=Button(win,text="login")
btnlogin.grid(column=1,row=3,columnspan=2,ipadx=10,ipady=10)
win.mainloop()