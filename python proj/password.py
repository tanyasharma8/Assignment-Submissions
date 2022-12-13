from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

class Password_Window:
    def __init__ (self,root):
        self.root=root  
        self.root.title("Change Password")
        self.root.geometry('600x600')
             
        # Background image

        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

         #main Frame
        frame_pass=Frame(self.root,bg='white')
        frame_pass.place(x=150,y=100,width=300,height=350)


        pass_str=Label(frame_pass,text='Forget Password',font=('times new romen',15,'bold'),fg="red",bg="white")
        pass_str.place(x=55,y=10)

        #label for password
        new_pass=lbl=Label(frame_pass,text="Enter New Password",font=("times new romen",15,'bold'),fg="white",bg="black")
        new_pass.place(x=45,y=50)
         
        #textEntry for password
        self.txtpass=ttk.Entry(frame_pass,font=("times new romen",15,'bold'))
        self.txtpass.place(x=45,y=85,width=200)



        #label for password
        new_pass=lbl=Label(frame_pass,text="Check Password",font=("times new romen",15,'bold'),fg="white",bg="black")
        new_pass.place(x=45,y=120)
         
        #textEntry for password
        self.txtcheck=ttk.Entry(frame_pass,font=("times new romen",15,'bold'))
        self.txtcheck.place(x=45,y=160,width=200)

        # reset button

        loginpbtn=Button(frame_pass,text="Reset Password",command=self.password,font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey',activeforeground='white',activebackground='grey')
        loginpbtn.place(x=30,y=250,width=250,height=35)
        
    def password(self):
        if self.txtpass.get()==self.txtcheck.get():
            messagebox.showerror("success","password changes")
        
        else:
            messagebox.showerror("error","change password and check password does'nt match ")
             



root=Tk()
app=Password_Window(root)
root.mainloop()





