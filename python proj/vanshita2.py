from cProfile import label
from distutils.cmd import Command
from functools import partial
from modulefinder import IMPORT_NAME
from turtle import width
from PIL import Image,ImageTk
from tkinter import *
import cx_Oracle
from tkinter import messagebox

def main():
    win=Tk()
    app=login(win)
    win.mainloop()

class login:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title('login screen')
        self.root.geometry('1366x700')
        #------------------------------image------------------------------
        self.photo=ImageTk.PhotoImage(file=r"D:\python proj\hotel3.jpg")
        label_img=Label(self.root,image=self.photo)
        label_img.place(x=0,y=0,relwidth=1,relheight=1)
        #-----------------------------datAFRAME-----------------------------
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=400,y=130,width=600,height=400)
        dataframeleft=LabelFrame(dataframe,bd=5,relief=FLAT,padx=10,font=('TIMES NEW ROMEN',23,'bold'),text='LOGIN HERE',fg='plum',bg='white')
        dataframeleft.place(x=300,y=0,width=120,height=150)
        #-------------------------------PHOTO----------------------------
        self.photo1=ImageTk.PhotoImage(file=r"D:\python proj\hotel3.jpg")
        label_img1=Label(self.root,image=self.photo1)
        label_img1.place(x=400,y=130,width=600,height=400)
        #=====================username================================
        self.usernamelabel=Label(self.root,bd=20,relief=SUNKEN,text='USERNAME',fg='PURPLE',bg='gray',font=('areil',20,'bold')).place(x=420,y=250)
        username=StringVar()
        self.usernameentry=Entry(self.root,bd=20,relief=RIDGE,textvariable=username,fg='BLACK',bg='gray',font=('TIMES NEW ROMEN',20,'bold')).place(x=620,y=250)
        #-----------------------password------------------------------------------------------------
        self.passwordlabel=Label(self.root,bd=20,relief=SUNKEN,text='PASSWORD',fg='purple',bg='gray',font=('areil',20,'bold')).place(x=420,y=340)
        password=StringVar()
        self.passwordentry=Entry(self.root,bd=20,relief=RIDGE,textvariable=password,show='*',fg='BLACK',bg='gray',font=('TIMES NEW ROMEN',20,'bold')).place(x=620,y=340)
        #-------------------------buttons--------------------------------------------------
        self.loginbutton=Button(self.root,bd=10,relief=RAISED,text='login',command=self.validatelogin,fg='BLACK',bg='PLUM',font=('areil',20,'bold')).place(x=540,y=420)
        self.resetbutton=Button(self.root,bd=10,relief=RAISED,text='reset',command=self.reset,fg='BLACK',bg='PLUM',font=('areil',20,'bold')).place(x=650,y=420)
        self.exitbutton=Button(self.root,bd=10,relief=RAISED,text='exit',command=self.iexit,fg='BLACK',bg='PLUM',font=('areil',20,'bold')).place(x=760,y=420)
    #---------------------------login button---------------------------------------------
    def validatelogin(self):
        # u=self.username.get()
        # p=self.password.get()
        # print('entered username',u)
        # print('entered password',p)
        # if(u==str('luxury') and p==str('1234')):
        if(self.usernameentry.get()=='Vanshit'  and self.passwordentry.get()=='Vanshu'):
            self.new_window=Toplevel(self.root2)
            self.app=self.window2(self.new_window)
        else:
            messagebox.askyesno("invalid login details")
            self.usernameentry.set("")
            self.passwordentry.set("")
            self.usernameentry.focus()
    
    def reset(self):#-------------------------reset button--------------------------------------
        self.usernameentry.set(" ")
        self.passwordentry.set(" ")
        self.usernameentry.focus()
     #--------------------------exit button--------------------------------------
    def iexit(self):
        self.iexit=messagebox.askyesno('do you really want to exit')
        if self.iexit>0:
            self.root.destroy()
        else:
            
            return
    def new_window(self):
        self.newWindow=Toplevel(self.root)
        self.app=window2(self.newWindow)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=window2(self.new_window)

class window2():
    def __init__(self):
        self.root2=Tk()
        self.root2.title('login screen')
        self.root2.geometry('1366x700')


main()