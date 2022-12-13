from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop() 
                                                    

class Login_Window:
    def __init__ (self,root):
        self.root=root  
        self.root.title("Login")
        self.root.geometry('1800x1000+0+0')

        self.var_password=StringVar()
        
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg.jpg")
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
        password=lbl=Label(frame,text="Password",font=("times new romen",15,'bold'),fg="white",bg="black")
        password.place(x=70,y=225)
         
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
        loginbtn=Button(frame,command=self.user_window,text="LogIn",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey',activeforeground='white',activebackground='grey')
        loginbtn.place(x=110,y=300,width=120,height=35)
     
# register button
        Registerbtn=Button(frame,text="New user register",font=("times new romen",10,'bold'),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        Registerbtn.place(x=15,y=350,width=160)
     
        # password button

        passwordbtn=Button(frame,command=self.forget_password,text="forget password",font=("times new romen",10,'bold'),borderwidth=0,fg='white',bg='black',activeforeground='white',activebackground='black')
        passwordbtn.place(x=10,y=370,width=160)
    
    def user_window(self):
        self.new_window=Toplevel(self.root)
        self.app=hotelmanagement(self.new_window)

    def forget_password(self):
        self.window=Tk()
        self.window.geometry('500x500')
        self.window.title('Forget Password')

        # frame for forget password

        frame_for=Frame(self.window,bg='black')
        frame_for.place(x=5,y=10,width=480,height=880)

        # img2=Image.open(r"D:\python proj\forget_logo.jpg")
        # img2=img2.resize((25,25))
        # self.photoimage2=ImageTk.PhotoImage(img2)
        # lblimg2=Label(image=self.photoimage2,bg='black',borderwidth=0)
        # lblimg2.place(x=650,y=323,width=25,height=25)
 



        # label for forget password

        get_pass=Label(frame_for,text='FORGET PASSWORD',font=('Times New Roman',30,'bold'),fg='White',bg='black')
        get_pass.place(x=5,y=15)

        # NEW PASSWORD
        #label for password
        new_pass=lbl=Label(frame_for,text="Enter New Password",font=("times new romen",15,'bold'),fg="white",bg="black")
        new_pass.place(x=20,y=155)
         
        #textEntry for password
        self.txtpass=ttk.Entry(frame_for,font=("times new romen",15,'bold'))
        self.txtpass.place(x=225,y=155,width=200)

        # label for password

        new_pass_check=lbl=Label(frame_for,text="Confirm Password",font=("times new romen",15,'bold'),fg="white",bg="black")
        new_pass_check.place(x=20,y=220)
         
        # textEntry for password

        self.txtcheck=ttk.Entry(frame_for,font=("times new romen",15,'bold'))
        self.txtcheck.place(x=225,y=220,width=200)

        # reset button

        resetbtn=Button(frame_for,text="RESET",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey',activeforeground='white',activebackground='grey')
        resetbtn.place(x=180,y=300,width=120,height=35)
   

    # def login(self):
    #     if self.txtuser.get=="" or self.txtpass.get()=="":
    #         messagebox.showerror("Error","all fields required")
    #     elif self.txtuser.get()=="Tanu" and self.txtpass.get()=="Tanu":
    #         messagebox.showinfo("Sucess","wlecome to hotel managemnet project")
    #     else:
    #         messagebox.showerror("Invalid","Invalid Username and Password")

     

class hotelmanagement:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL  MANAGEMENT   SYSTEM")
        self.root.geometry("1550x800")

    # Background Image
        self.Back_img=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg.jpg")
        label_img=Label(self.root,image=self.Back_img)
        label_img.place(x=0,y=0,relwidth=1,relheight=1)

    # image 1
    
        img1=Image.open(r"D:\python proj\hotelimg2.jpg")
        img1=img1.resize((1550,180))
        self.photoimg1=ImageTk.PhotoImage(img1)
        un=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        un.place(x=0,y=0,width=1550,height=180)

    # image 2

        img2=Image.open(r"D:\python proj\h1.jpg")
        img2=img2.resize((230,180))
        self.photoimg2=ImageTk.PhotoImage(img2)
        un=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        un.place(x=0,y=0,width=230,height=180)

        lb=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Algerian",60),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb.place(x=0,y=180,width=1550,height=80)

    # image3  

        img3=Image.open(r"D:\python proj\f1.jpg")
        img3=img3.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        un=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        un.place(x=0,y=260,width=230,height=180)

    # image 4
        img4=Image.open(r"D:\python proj\h2.jpg")
        img4=img4.resize((230,180),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        un=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        un.place(x=0,y=430,width=230,height=180)
     
    # LAbel for menu
        lb_menu=Label(self.root,text="MENU",font=("Algerian",60),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb_menu.place(x=450,y=290,width=550,height=80)

    # Menu Frame
        frame_menu=Frame(self.root,bg='black')
        frame_menu.place(x=450,y=380,width=550,height=400)
    
    # Customer Button
        custbtn=Button(frame_menu,command=self.user_window2,text="CUSTOMER",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        custbtn.place(x=35,y=30,width=500,height=60)
    
    # Booking Button
        bookbtn=Button(frame_menu,text="BOOKING",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=100,width=500,height=60)

    # Detail Button
        bookbtn=Button(frame_menu,text="DETAIL",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=170,width=500,height=60)   

    # Record Button
        bookbtn=Button(frame_menu,text="RECORD",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=240,width=500,height=60)     

    
    # log out Button
        bookbtn=Button(frame_menu,text="LOG OUT",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=310,width=500,height=60)

# FUNCTION DECLARATION
    def main_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","all fiels are required")
        elif self.var_password.get()==self.var_confirmpassword.get():
                messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
                messagebox.showerror("error","please agree terms and conditions")
        else:
                messagebox.showinfo("Success","Welcome")   


    def user_window2(self):
        self.new_window2=Toplevel(self.root)
        self.app2=Register(self.new_window2)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('REGISTER')
        self.root.geometry('1600x900+0+0')
        
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sex=StringVar()
        self.var_address=StringVar()
        self.var_aadhar=StringVar()
        self.var_city=StringVar()
        self.var_check =IntVar()
        




        #background image
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg2.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
       
        #main Frame
        frame=Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)


        #label
        register_label=Label(frame,text="CUSTOMER DETAILS",font=('times new roman',20,'bold'),bg="white",fg="blue")
        register_label.place(x=20,y=20)
        

        #label and entry

# first name
        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),bg="white")
        fname.place(x=50,y=100)

        fname_entry=Entry(frame,textvariable=self.var_fname,font=('times new roman',15,'bold'))
        fname_entry.place(x=50,y=130,width=250)


#  last name  
        lname=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg="white")
        lname.place(x=400,y=100)

        lname_entry=Entry(frame,textvariable=self.var_lname,font=('times new roman',15,'bold'))
        lname_entry.place(x=400,y=130,width=250)

# contact number
        contact=Label(frame,text="Contact Number",font=('times new roman',15,'bold'),bg="white")
        contact.place(x=50,y=160)

        contact_entry=Entry(frame,textvariable=self.var_contact,font=('times new roman',15,'bold'))
        contact_entry.place(x=50,y=190,width=250)

# email
        email=Label(frame,text="Email",font=('times new roman',15,'bold'),bg="white")
        email.place(x=400,y=160)

        email_entry=Entry(frame,textvariable=self.var_email,font=('times new roman',15,'bold'))
        email_entry.place(x=400,y=190,width=250)

# sex
        sex=Label(frame,text="Select Sex",font=('times new roman',15,'bold'),bg="white")
        sex.place(x=50,y=220)

# sequrity_entry=Entry(frame,font=('times new roman',15,'bold'))
# sequrity_entry.place(x=50,y=250,width=250)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_sex ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","Male","Female","Other")
        self.combo_security_Q.place(x=50,y=250,width=250)
        self.combo_security_Q.current(0)



# address
        Address=Label(frame,text="Address",font=('times new roman',15,'bold'),bg="white")
        Address.place(x=400,y=220)

        Address_entry=Entry(frame,textvariable=self.var_address,font=('times new roman',15,'bold'))
        Address_entry.place(x=400,y=250,width=250)
# aadhar no

        aadhar=Label(frame,text="Aadhar Number",font=('times new roman',15,'bold'),bg="white")
        aadhar.place(x=50,y=280)

        aadhar_entry=Entry(frame,textvariable=self.var_aadhar,font=('times new roman',15,'bold'))
        aadhar_entry.place(x=50,y=310,width=250)

 
# city
        City=Label(frame,text="City",font=('times new roman',15,'bold'),bg="white")
        City.place(x=400,y=280)

        City_entry=Entry(frame,textvariable=self.var_city,font=('times new roman',15,'bold'))
        City_entry.place(x=400,y=310,width=250)


# check button
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Condtions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=360)
        

# button 

        img=Image.open(r"D:\python proj\registernow.jpg")
        img=img.resize((100,50))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=430,width=100)



        img1=Image.open(r"D:\python proj\loginb2.jpg")
        img1=img1.resize((100,50))
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=390,y=430,width=100)


# function declarartion
# 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_aadhar()=="":
                messagebox.showerror("Error","all fiels are required")
        elif self.var_check.get()==0:
                messagebox.showerror("error","please agree terms and conditions")
        else:
                messagebox.showinfo("Success","Welcome")          



main()