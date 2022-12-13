from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import cx_Oracle
import random

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
        bookbtn=Button(frame_menu,command=self.user_window3,text="BOOKING",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
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

    def user_window3(self):
        self.new_window3=Toplevel(self.root)
        self.app3=Room_Booking(self.new_window3)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('REGISTER')
        self.root.geometry('1600x900+0+0')
        
        #variables
        # self.var_fname=StringVar()
        # self.var_lname=StringVar()
        # self.var_contact=StringVar()
        # self.var_email=StringVar()
        # self.var_sex=StringVar()
        # self.var_address=StringVar()
        # self.var_aadhar=StringVar()
        # self.var_city=StringVar()
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
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

# Customer  number
        cust_id=Label(frame,text="Customer No.",font=('times new roman',15,'bold'),bg="white")
        cust_id.place(x=50,y=100)

        cust_id_entry=Entry(frame,textvariable=self.var_ref,font=('times new roman',15,'bold'))
        cust_id_entry.place(x=50,y=130,width=250)


#  last name  
        name=Label(frame,text="Full Name",font=('times new roman',15,'bold'),bg="white")
        name.place(x=400,y=100)

        self.name_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.name_entry.place(x=400,y=130,width=250)

# contact number
        contact=Label(frame,text="Contact Number",font=('times new roman',15,'bold'),bg="white")
        contact.place(x=50,y=160)

        self.contact_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.contact_entry.place(x=50,y=190,width=250)

# email
        email=Label(frame,text="Email",font=('times new roman',15,'bold'),bg="white")
        email.place(x=400,y=160)

        self.email_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.email_entry.place(x=400,y=190,width=250)

# sex
        sex=Label(frame,text="Select Sex",font=('times new roman',15,'bold'),bg="white")
        sex.place(x=50,y=220)

# sequrity_entry=Entry(frame,font=('times new roman',15,'bold'))
# sequrity_entry.place(x=50,y=250,width=250)

        self.combo_sexA=ttk.Combobox(frame ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_sexA["values"]=("select","Male","Female","Other")
        self.combo_sexA.place(x=50,y=250,width=250)
        self.combo_sexA.current(0)



# address
        post=Label(frame,text="Post code",font=('times new roman',15,'bold'),bg="white")
        post.place(x=400,y=220)

        self.post_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.post_entry.place(x=400,y=250,width=250)
# aadhar no

        aadhar=Label(frame,text="Aadhar Number",font=('times new roman',15,'bold'),bg="white")
        aadhar.place(x=50,y=280)

        self.aadhar_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.aadhar_entry.place(x=50,y=310,width=250)

 
# city
        City=Label(frame,text="City",font=('times new roman',15,'bold'),bg="white")
        City.place(x=400,y=280)

        self.City_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.City_entry.place(x=400,y=310,width=250)


# check button
        checkbtn=Checkbutton(frame,text="I Agree The Terms and Condtions",variable=self.var_check,font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=360)
        

# button 

        b1=Button(frame,text="ADD",command=self.register_data,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b1.place(x=10,y=430,width=100)

        b2=Button(frame,text="UPDATE",borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b2.place(x=150,y=430,width=100)

        b3=Button(frame,text="DELETE",borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b3.place(x=300,y=430,width=100)

        b4=Button(frame,text="RESET",borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b4.place(x=450,y=430,width=100)


# function declarartion
# 
    def register_data(self):
        if self.name_entry.get()=="" or self.contact_entry.get()=="" or self.email_entry.get()=="" or self.combo_sexA.get()=="" or self.aadhar_entry.get()=="" or self.post_entry.get()=="" or self.City_entry.get()=="":
            messagebox.showerror("Error","all fields are requires",parent=self.root)
        elif self.var_check==0:
            messagebox.showerror("Error",'Please agree terms and conditions')
        else:
            try:   
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()    
                var="insert into customer values(:cust_no,:name,:contact,:email,:sex,:post_code,:addhar_no,:city)"
                cur.execute(var,(self.var_ref.get(),self.name_entry.get(),self.contact_entry.get(),self.email_entry.get(),self.combo_sexA.get(),    self.post_entry.get(),self.aadhar_entry.get(),self.City_entry.get()))
                con.commit()                    
                cur2=con.cursor()
                cur2.execute('select * from customer')
                res=cur2.fetchall()
                for i in res:
                    print(i)   
                cur.close()
                cur2.close()    
                con.close()
                messagebox.showinfo("Success","Registered Successfully")
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)
                         


# booking


class Room_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title('ROOM BOOKING')
        self.root.geometry('1600x900+0+0')
        
        # variable declaration

        self.var_rno=IntVar()
        self.var_category=StringVar()
        self.var_status=StringVar()
        self.var_price=IntVar()
        # Background color

        self.root.config(bg='floral white')

        # image

        self.bg1=ImageTk.PhotoImage(file=r"D:\python proj\room_white.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # frame

        frame=Frame(self.root,bg='ghost white')
        frame.place(x=520,y=100,width=800,height=550)

        # label

        booking_label=Label(frame,text="ROOM BOOKING DETAILS",font=('times new roman',30,'bold'),bg="ghost white",fg="peach puff")
        booking_label.place(x=30,y=30)

        # label and entry
        # room number
        room_no=Label(frame,text="Room Number",font=('times new roman',15,'bold'),bg="white")
        room_no.place(x=80,y=100)

        room_no_entry=Entry(frame,textvariable=self.var_rno,font=('times new roman',15,'bold'))
        room_no_entry.place(x=80,y=130,width=250)

        # category of room

        category=Label(frame,text="Select Category of Room",font=('times new roman',15,'bold'),bg="white")
        category.place(x=80,y=170)

        self.combo_category=ttk.Combobox(frame,textvariable=self.var_category ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_category["values"]=("select","AC ","NON- AC")
        self.combo_category.place(x=80,y=200,width=250)
        self.combo_category.current(0)

        # status of room

        status=Label(frame,text="Status Of Room",font=('times new roman',15,'bold'),bg="white")
        status.place(x=80,y=250)

        self.combo_status=ttk.Combobox(frame,textvariable=self.var_status ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_status["values"]=("select","OCCUPIED","AVAILABLE")
        self.combo_status.place(x=80,y=280,width=250)
        self.combo_status.current(0)

        # price

        price=Label(frame,text="Price",font=('times new roman',15,'bold'),bg="white")
        price.place(x=80,y=320)

        price_entry=Entry(frame,textvariable=self.var_price,font=('times new roman',15,'bold'))
        price_entry.place(x=80,y=350,width=250)

        # button

        img=Image.open(r"D:\python proj\registernow.jpg")
        img=img.resize((100,50))
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=100,y=430,width=100)

        # function declaration

        def booking_data(self):
            if self.var_rno.get()=="" or self.var_category.get()=="" or self.var_status.get()=="" or self.var_price.get()=="":
                messagebox.showerror("Error","all fiels are required")
        
            else:
                messagebox.showinfo("Success","Welcome")          


main()


