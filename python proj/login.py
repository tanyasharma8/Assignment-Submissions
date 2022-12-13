from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class Login_Window:
    def __init__ (self,root):
        self.root=root  
        self.root.title("Login")
        self.root.geometry('1800x1000+0+0')

        self.var_password=StringVar()
        
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\hotel3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        #Frame
        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)
        
        #First Image in Frame
        img1=Image.open(r"D:\python proj\login.jpg")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        

        #GeT started label
        get_str=Label(frame,text='Get Started',font=('times new romen',20,'bold'),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label for user
        username=lbl=Label(frame,text="Username",font=("times new romen",15,'bold'),fg="white",bg="black")
        username.place(x=70,y=155)
         
        #textEntry for user
        self.txtuser=ttk.Entry(frame,font=("times new romen",15,'bold'))
        self.txtuser.place(x=40,y=180,width=250)

        #password label
        password1=lbl=Label(frame,text="Password",font=("times new romen",15,'bold'),fg="white",bg="black")
        password1.place(x=70,y=225)
         
        #password entry area
        self.txtpass=ttk.Entry(frame,textvariable=self.var_password,show='*',font=("times new romen",15,'bold'))
        self.txtpass.place(x=40,y=250,width=250)
         

        #icon Images   
        img2=Image.open(r"D:\python proj\logo.jpg")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg='black',borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)
 
        img3=Image.open(r"D:\python proj\pass.jpg")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg='black',borderwidth=0)
        lblimg3.place(x=650,y=392,width=25,height=25)
# login button
        loginbtn=Button(frame,command=self.login,text="LogIn",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey',activeforeground='white',activebackground='grey')
        loginbtn.place(x=110,y=300,width=120,height=35)
     
# register button
        Registerbtn=Button(frame,text="New user register",font=("times new romen",10,'bold'),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        Registerbtn.place(x=15,y=350,width=160)
     
# password button

        passwordbtn=Button(frame,text="forget password",font=("times new romen",10,'bold'),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        passwordbtn.place(x=10,y=370,width=160)
     
    def login(self):
        if self.txtuser.get=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif self.txtuser.get()=="Tanu" and self.txtpass.get()=="Tanu":
            messagebox.showinfo("Sucess","wlecome to hotel managemnet project")
        else:
            messagebox.showerror("Invalid","Invalid Username and Password")
             



root=Tk()
app=Login_Window(root)
root.mainloop()