from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import cx_Oracle
import random
import os
import pyttsx3

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
        self.txtpass=ttk.Entry(frame,show='*',font=("times new romen",15,'bold'))
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
            self.new_window=Toplevel(self.root)
            self.app=hotelmanagement(self.new_window)
        else:                                                                    
            messagebox.showerror("Invalid","Invalid Username and Password")     

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
        bookbtn=Button(frame_menu,command=self.user_window4,text="DETAIL",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=170,width=500,height=60)  
        # Record Button
        bookbtn=Button(frame_menu,text="RESTURANT",command=self.user_window5,font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=240,width=500,height=60)     
        # BILL Button
        bookbtn=Button(frame_menu,command=self.user_window6,text="BILL",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
        bookbtn.place(x=35,y=310,width=500,height=60)

    def user_window2(self):
        self.new_window2=Toplevel(self.root)
        self.app2=Register(self.new_window2)
    
    def user_window3(self):
        self.new_window3=Toplevel(self.root)
        self.app3=Room_Booking(self.new_window3)
    
    def user_window4(self):
        self.new_window4=Toplevel(self.root)
        self.app4=Details(self.new_window4)
    
    def user_window5(self):
        self.new_window5=Toplevel(self.root)
        self.app5=Resturant(self.new_window5)

    def user_window6(self):
        self.new_window6=Toplevel(self.root)
        self.app6=bill(self.new_window6)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('REGISTER')
        self.root.geometry('1600x900+0+0')
        # test-to-Speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
        #variables
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sex=StringVar()
        self.var_post=StringVar()
        self.var_aadhar=StringVar()
        self.var_city=StringVar()
        self.var_ref=StringVar()
        self.var_name=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_check =IntVar()
        #background image
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        #main Frame
        frame=Frame(self.root,bg='white')
        frame.place(x=820,y=100,width=700,height=550)
        #label
        register_label=Label(frame,text="CUSTOMER DETAILS",font=('times new roman',20,'bold'),bg="white",fg="blue")
        register_label.place(x=20,y=20)
        #label and entry
        # Customer  number
        cust_id=Label(frame,text="Customer No.",font=('times new roman',15,'bold'),bg="white")
        cust_id.place(x=50,y=100)
        cust_id_entry=Entry(frame,textvariable=self.var_ref,font=('times new roman',15,'bold'))
        cust_id_entry.place(x=50,y=130,width=250)
        #  full name  
        name=Label(frame,text="Full Name",font=('times new roman',15,'bold'),bg="white")
        name.place(x=400,y=100)
        name_entry=Entry(frame,textvariable=self.var_name,font=('times new roman',15,'bold'))
        name_entry.place(x=400,y=130,width=250)
    
        # contact number
        contact=Label(frame,text="Contact Number",font=('times new roman',15,'bold'),bg="white")
        contact.place(x=50,y=160)
        self.contact_entry=Entry(frame,textvariable=self.var_contact,font=('times new roman',15,'bold'))
        self.contact_entry.place(x=50,y=190,width=250)
        # email
        email=Label(frame,text="Email",font=('times new roman',15,'bold'),bg="white")
        email.place(x=400,y=160)
        self.email_entry=Entry(frame,textvariable=self.var_email,font=('times new roman',15,'bold'))
        self.email_entry.place(x=400,y=190,width=250)
        # sex
        sex=Label(frame,text="Select Sex",font=('times new roman',15,'bold'),bg="white")
        sex.place(x=50,y=220)
        self.combo_sexA=ttk.Combobox(frame ,textvariable=self.var_sex,font=("times new roman",15,"bold"),state="readonly")
        self.combo_sexA["values"]=("select","Male","Female","Other")
        self.combo_sexA.place(x=50,y=250,width=250)
        self.combo_sexA.current(0)
        # pin code
        post=Label(frame,text="Pin code",font=('times new roman',15,'bold'),bg="white")
        post.place(x=400,y=220)
        self.post_entry=Entry(frame,textvariable=self.var_post,font=('times new roman',15,'bold'))
        self.post_entry.place(x=400,y=250,width=250)
        # aadhar no
        aadhar=Label(frame,text="Aadhar Number",font=('times new roman',15,'bold'),bg="white")
        aadhar.place(x=50,y=280)
        self.aadhar_entry=Entry(frame,textvariable=self.var_aadhar,font=('times new roman',15,'bold'))
        self.aadhar_entry.place(x=50,y=310,width=250)
        # city
        City=Label(frame,text="City",font=('times new roman',15,'bold'),bg="white")
        City.place(x=400,y=280)
        self.City_entry=Entry(frame,textvariable=self.var_city,font=('times new roman',15,'bold'))
        self.City_entry.place(x=400,y=310,width=250) 
       # check button
        checkbtn=Checkbutton(frame,text="I Agree The Terms and Condtions",variable=self.var_check,font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=360)
        # button 

        b1=Button(frame,text="ADD",command=self.validation,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b1.place(x=10,y=430,width=100)

        b2=Button(frame,text="UPDATE",command=self.update,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b2.place(x=150,y=430,width=100)

        b3=Button(frame,text="DELETE",command=self.delete,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b3.place(x=300,y=430,width=100)
    
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        detail_frame.place(x=0 ,y=100 ,width=818,height=550) 
        table_frame=Label(detail_frame,text="View details and search system",font=('times new roman',12,'bold'),bg="grey",fg='black')
        table_frame.place(x=10,y=20)
        table_frame=Label(detail_frame,text="Search By",font=('times new roman',12,'bold'),bg="red",fg='white')
        table_frame.place(x=10,y=48)
        search=Label(detail_frame,text="Select ",font=('times new roman',13,'bold'),bg="white")
        search.place(x=90,y=48)
        self.search_var=StringVar()
        self.combo_search=ttk.Combobox(detail_frame,textvariable=self.search_var ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_search["values"]=("select","Contact")
        self.combo_search.place(x=160,y=48,width=80)
        self.combo_search.current(0)
        self.txt_search=StringVar()
        self.search_entry=Entry(detail_frame,textvariable=self.txt_search,font=('times new roman',13,'bold'))
        self.search_entry.place(x=240,y=48,width=120)
        b5=Button(detail_frame,text="SEARCH",command=self.search,borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        b5.place(x=350,y=48,width=85)
        b6=Button(detail_frame,text="SHOW ALL",command=self.fetch_data,borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        b6.place(x=450,y=48,width=85)                     
        # table frame
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='white')
        table_frame.place(x=0 ,y=100 ,width=818,height=400)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.hotel_table=ttk.Treeview(table_frame,columns=("cno","name","contact","email","sex","Post","aadhar","City"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)
        self.hotel_table.heading("cno",text="Customer Id") 
        self.hotel_table.heading("name",text="Name")                                                                                  
        self.hotel_table.heading("contact",text="Contact")                                                                                  
        self.hotel_table.heading("email",text="Email")                                                                                  
        self.hotel_table.heading("sex",text="Sex")                                                                                  
        self.hotel_table.heading("Post",text="Pin Code")                                                                                  
        self.hotel_table.heading("aadhar",text="Aadhar No")                                                                                  
        self.hotel_table.heading("City",text="City") 
        self.hotel_table["show"]="headings"

        self.hotel_table.column("cno",width=100)
        self.hotel_table.column("name",width=100)
        self.hotel_table.column("contact",width=100)
        self.hotel_table.column("email",width=150)
        self.hotel_table.column("sex",width=100)
        self.hotel_table.column("Post",width=100)
        self.hotel_table.column("aadhar",width=100)
        self.hotel_table.column("City",width=100)

        self.hotel_table.pack(fill=BOTH,expand=1)                                                                               
        self.hotel_table.bind("<ButtonRelease-1>",self.get_cursur)
        self.fetch_data()
# function declarartion
    def validation(self):
        if self.var_name.get()=='':
            self.engine.say('Please enter your name')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter your Name",parent=self.root)     
        elif self.var_contact.get()=='' or len(self.var_contact.get())!=10:
            self.engine.say('Please enter your contact number')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter your Contact Number",parent=self.root)     
        elif self.var_email.get()=='':
            self.engine.say('Please enter your email')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter your email Number",parent=self.root)
        elif self.var_post.get()=='':
            self.engine.say('Please Enter your pin code')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter pin code",parent=self.root)
        elif self.var_aadhar.get()=='' or len(self.var_aadhar.get())!=12:
            self.engine.say('Please enter your aadhar Number')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please Enter your Aadhar Number",parent=self.root)
        elif self.var_city.get()=='':
            self.engine.say('Please enter your city ')
            self.engine.runAndWait()
            messagebox.showerror("Error","Please enter your city",parent=self.root)
        elif self.var_check.get()==0:
            self.engine.say('Please Agree terms and conditions')
            self.engine.runAndWait()          
        try:   
            con=cx_Oracle.connect('scott/tiger')
            cur=con.cursor()    
            var="insert into customer values(:cust_no,:name,:contact,:email,:sex,:post_code,:addhar_no,:city)"
            cur.execute(var,(self.var_ref.get(),self.var_name.get(),self.var_contact.get(),self.var_email.get(),self.var_sex.get(),self.var_post.get(),self.var_aadhar.get(),self.var_city.get()))
            con.commit()    
            self.fetch_data()                
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

    def fetch_data(self):
        con=cx_Oracle.connect('scott/tiger')
        cur=con.cursor()    
        cur.execute("select * from customer")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for i in rows:
                self.hotel_table.insert("",END,values=i)
            con.commit()
        con.close()

    def get_cursur(self,event=""):
        cursor_row=self.hotel_table.focus()
        content=self.hotel_table.item(cursor_row)
        row=content["values"]
        self.var_checkin=StringVar()
        self.var_checkin=StringVar()
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_email.set(row[3])
        self.var_sex.set(row[4]),
        self.var_post.set(row[5]),
        self.var_aadhar.set(row[6]),
        self.var_city.set(row[7])

    def delete(self):
        if  self.var_ref.get()=="":
            messagebox.showerror('Error','Nothing to delete')
        else:
            try:
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor() 
                st="delete from customer where cust_no='"+self.var_ref.get()+"' "
                cur.execute(st)
                con.commit()
                cur.close()
                messagebox.showinfo('Success','Successfully deleted')
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

    def update(self):
        if self.contact_entry.get()=="":
            messagebox.showerror("Error",'Nothing to update',parent=self.root)
        else:
            try:
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()
                cur.execute("update customer set name=:1,contact=:2,email=:3,sex=:4,post_code=:5,aadhar_no=:6,city=:7 where cust_no=:8" ,(
                                                                                                                                    self.var_name.get(),
                                                                                                                                    self.var_contact.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_sex.get(),
                                                                                                                                    self.var_post.get(),
                                                                                                                                    self.var_aadhar.get(),
                                                                                                                                    self.var_city.get(),
                                                                                                                                    self.var_ref.get()
                                                                                                                                    ))                                                                                                                                                                                                                                                                
                con.commit()
                self.fetch_data()
                cur.close()
                messagebox.showinfo('Success','Successfully Updated')
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}')
    
    def search(self):
        con=cx_Oracle.connect('scott/tiger')
        cur=con.cursor()
        cur.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for i in rows:
                self.hotel_table.insert("",END,values=i)
            con.commit()
        con.close()        

# booking

class Room_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title('ROOM BOOKING')
        self.root.geometry('1600x900+0+0')

        # Background color
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\bg.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        # image 
        self.bg1=ImageTk.PhotoImage(file=r"D:\python proj\room_white.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        # frame   
        frame=Frame(self.root,bd=10)
        frame.place(x=820,y=100,width=700,height=550)        
        # frame
        frame=Frame(self.root,bd=10)
        frame.place(x=820,y=100,width=700,height=550)

        # label
        booking_label=Label(frame,text="ROOM BOOKING DETAILS",font=('times new roman',30,'bold'),bg="ghost white",fg="plum")
        booking_label.place(x=30,y=30)
        # room number
        self.var_cust_id=StringVar()
        cust_id=Label(frame,text="Customer Contact No",font=('times new roman',15,'bold'),bg="white")
        cust_id.place(x=80,y=100)
        cust_id_entry=Entry(frame,textvariable=self.var_cust_id,font=('times new roman',15,'bold'))
        cust_id_entry.place(x=80,y=130,width=250)
        self.var_rno=StringVar()
        roomno=Label(frame,text="Room Number",font=('times new roman',15,'bold'),bg="white")
        roomno.place(x=350,y=100)
        roomno_entry=Entry(frame,textvariable=self.var_rno,font=('times new roman',15,'bold'))
        roomno_entry.place(x=350,y=130,width=250)
        self.var_checkin=StringVar() 
        Checkin=Label(frame,text="Check In",font=('times new roman',15,'bold'),bg="white")
        Checkin.place(x=80,y=170)
        Checkin_entry=Entry(frame,textvariable=self.var_checkin,font=('times new roman',15,'bold'))
        Checkin_entry.place(x=80,y=200,width=250)
        self.var_checkout=StringVar()
        Checkout=Label(frame,text="Check Out",font=('times new roman',15,'bold'),bg="white")
        Checkout.place(x=350,y=170)
        Checkout_entry=Entry(frame,textvariable=self.var_checkout,font=('times new roman',15,'bold'))
        Checkout_entry.place(x=350,y=200,width=250)
        self.var_bill=StringVar()
        Bill=Label(frame,text="Room Rent",font=('times new roman',15,'bold'),bg="white")
        Bill.place(x=350,y=240)
        Bill_entry=Entry(frame,textvariable=self.var_bill,font=('times new roman',15,'bold'))
        Bill_entry.place(x=350,y=270,width=250)
        self.var_days=StringVar()
        days=Label(frame,text="No of Days",font=('times new roman',15,'bold'),bg="white")
        days.place(x=80,y=240)
        days_entry=Entry(frame,textvariable=self.var_days,font=('times new roman',15,'bold'))
        days_entry.place(x=80,y=270,width=250)
        but1=Button(frame,text="ADD",command=self.get_data,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        but1.place(x=10,y=430,width=100)
        b2=Button(frame,text="UPDATE",command=self.update,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b2.place(x=150,y=430,width=100)
        b3=Button(frame,text="DELETE",command=self.delete,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b3.place(x=300,y=430,width=100)

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        detail_frame.place(x=0 ,y=100 ,width=818,height=550) 
        table_frame=Label(detail_frame,text="View details and search system",font=('times new roman',12,'bold'),bg="grey",fg='black')
        table_frame.place(x=10,y=20)
        table_frame=Label(detail_frame,text="Search By",font=('times new roman',12,'bold'),bg="red",fg='white')
        table_frame.place(x=10,y=48)
        search=Label(detail_frame,text="Select ",font=('times new roman',13,'bold'),bg="white")
        search.place(x=90,y=48)
        self.search_var=StringVar()
        self.combo_search=ttk.Combobox(detail_frame,textvariable=self.search_var ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_search["values"]=("select","Room No")
        self.combo_search.place(x=160,y=48,width=80)
        self.combo_search.current(0)
        self.txt_search=StringVar()
        self.search_entry=Entry(detail_frame,textvariable=self.txt_search,font=('times new roman',13,'bold'))
        self.search_entry.place(x=240,y=48,width=120)
        b5=Button(detail_frame,text="SEARCH",command=self.search,borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        b5.place(x=350,y=48,width=85)
        b6=Button(detail_frame,text="SHOW ALL",borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        b6.place(x=450,y=48,width=85)                     
        # table frame
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='white')
        table_frame.place(x=0 ,y=100 ,width=818,height=400)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.hotel_table=ttk.Treeview(table_frame,columns=("cust_id","room_id","checkin","checkout","rent","no of days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)
        self.hotel_table.heading("cust_id",text="Customer Id") 
        self.hotel_table.heading("room_id",text="Room No")                                                                                                                                                                         
        self.hotel_table.heading("checkin",text="Check In")                                                                                                                                                                 
        self.hotel_table.heading("checkout",text="Check Out")                                                                                  
        self.hotel_table.heading("rent",text="Room Rent")                                                                                  
        self.hotel_table.heading("no of days",text="No of Days") 
        self.hotel_table.column("cust_id",width=200)
        self.hotel_table.column("room_id",width=200)
        self.hotel_table.column("checkin",width=200)
        self.hotel_table.column("checkout",width=200)
        self.hotel_table.column("rent",width=200)
        self.hotel_table.column("no of days",width=100)
        self.hotel_table.pack(fill=BOTH,expand=1)                                                                               
        self.hotel_table.bind("<ButtonRelease-1>",self.get_cursur)
        self.fetch_data()

    def get_cursur(self,event=""):
        cursor_row=self.hotel_table.focus()
        content=self.hotel_table.item(cursor_row)
        row=content["values"]    
        self.var_cust_id.set(row[0]),
        self.var_rno.set(row[1]),
        self.var_checkin.set(row[2]),
        self.var_checkout.set(row[3])
        self.var_bill.set(row[4]),
        self.var_days.set(row[5])

    def get_data(self):
        if self.var_cust_id.get()=="" or self.var_rno.get()=="" or self.var_checkin.get()=="" or self.var_checkout.get()=="" or self.var_bill.get()=="" or self.var_days.get()=="":                                              
                messagebox.showerror("Error","all fields are requires",parent=self.root)
        else:
            try:   
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()    
                var="insert into booking values(:contact,:room_id,:checkin,:checkout,:rent,:Number_of_days)"
                cur.execute(var,(self.var_cust_id.get(),self.var_rno.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_bill.get(),self.var_days.get()))
                con.commit()    
                self.fetch_data()                
                cur2=con.cursor()
                cur2.execute('select * from booking')
                res=cur2.fetchall()
                for i in res:
                    print(i)   
                cur.close()
                cur2.close()  
                con.close()
                messagebox.showinfo("Success","Registered Successfully")
            except Exception as es:          
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

    def delete(self):
        if  self.var_rno.get()=="":
            messagebox.showerror('Error','Nothing to delete')
        else:
            try:
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor() 
                var_ref=input("enter Customer ID which you want to delete:")
                st="delete from booking where room_id='"+self.var_rno.get()+"' "
                cur.execute(st)
                con.commit()
                cur.close()
                messagebox.showinfo('Success','Successfully deleted')
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)
                
    def fetch_data(self):
        con=cx_Oracle.connect('scott/tiger')
        cur=con.cursor()    
        cur.execute("select * from booking")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for i in rows:
                self.hotel_table.insert("",END,values=i)
            con.commit()
        con.close()

    def update(self):
        con=cx_Oracle.connect('scott/tiger')
        cur=con.cursor()
        cur.execute("update booking set contact=:1,checkin=:2,checkout=:3,rent=:4,number_of_days=:5 where room_id=:6",(
                                                                                                self.var_cust_id.get(),
                                                                                                self.var_checkin.get(),
                                                                                                self.var_checkout.get(),
                                                                                                self.var_bill.get(),
                                                                                                self.var_days.get(),
                                                                                                self.var_rno.get()
                                                                                                ))                                                                                                                                                                                                                                                                      
        con.commit()
        self.fetch_data()
        cur.close()
        messagebox.showinfo('Success','Successfully Updated')

    def search(self):
        con=cx_Oracle.connect('scott/tiger')
        cur=con.cursor()
        cur.execute("select * from booking where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for i in rows:
                self.hotel_table.insert("",END,values=i)
            con.commit()
        con.close()        

# ROOM DETAILS CLASS
class Details:
    def __init__(self,root):
        self.root=root
        self.root.title('ROOM BOOKING DETAILS')
        self.root.geometry('1600x900+0+0')
        # background img      
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\7280.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        # frame
        frame=Frame(self.root,bg='peach puff')
        frame.place(x=780,y=100,width=800,height=550)
        booking_label=Label(frame,text="ROOM DETAILS",font=('times new roman',30,'bold'),bg="ghost white",fg="peach puff")
        booking_label.place(x=30,y=30)
        # Room Image
        img3=Image.open(r"D:\python proj\room_white.jpg")
        img3=img3.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        un=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        un.place(x=1150,y=100,width=390,height=180)
        # floor
        roomno=Label(frame,text="Room Number",font=('times new roman',15,'bold'),bg="white")
        roomno.place(x=80,y=100)
        self.roomno_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.roomno_entry.place(x=80,y=130,width=250)
        # room number
        floor=Label(frame,text="Floor",font=('times new roman',15,'bold'),bg="white")
        floor.place(x=80,y=170)
        self.floor_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.floor_entry.place(x=80,y=200,width=250)
        # category of room
        category=Label(frame,text="Select Category of Room",font=('times new roman',15,'bold'),bg="white")
        category.place(x=80,y=250)
        self.combo_category=ttk.Combobox(frame ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_category["values"]=("select","AC ","NON- AC")
        self.combo_category.place(x=80,y=280,width=250)
        self.combo_category.current(0)
        # status of room
        status=Label(frame,text="Status Of Room",font=('times new roman',15,'bold'),bg="white")
        status.place(x=80,y=330)
        self.combo_status=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
        self.combo_status["values"]=("select","OCCUPIED","AVAILABLE")
        self.combo_status.place(x=80,y=360,width=250)
        self.combo_status.current(0)
        # buttons
        but1=Button(frame,text="ADD",command=self.get_data,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        but1.place(x=500,y=200,width=100)
        b2=Button(frame,text="UPDATE",command=self.update,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b2.place(x=500,y=250,width=100)
        b3=Button(frame,text="DELETE",command=self.delete,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b3.place(x=500,y=300,width=100)

        # table frameid
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        detail_frame.place(x=0 ,y=100 ,width=813,height=550)  
        table_frame=Label(detail_frame,text="View details and search system",font=('times new roman',15,'bold'),bg="white",fg='plum')
        table_frame.place(x=10,y=20)

        # table frame
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='white')
        table_frame.place(x=0 ,y=100 ,width=818,height=400)      
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.hotel_table=ttk.Treeview(table_frame,columns=("room_id","floor","category","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)
        self.hotel_table.heading("room_id",text="Room Number") 
        self.hotel_table.heading("floor",text="Floor")                                                                                                                                                                    
        self.hotel_table.heading("category",text="Category of Room")                                                                                                                                                                 
        self.hotel_table.heading("status",text="Status of Room")                                                                                  
        self.hotel_table["show"]="headings"
        self.hotel_table.column("room_id",width=200)
        self.hotel_table.column("floor",width=200)
        self.hotel_table.column("category",width=200)
        self.hotel_table.column("status",width=200)
        self.hotel_table.pack(fill=BOTH,expand=1)                                                                               
        self.hotel_table.bind("<ButtonRelease-1>",self.get_cursur)
        self.fetch_data()

    def get_cursur(self,event=""):
        cursor_row=self.hotel_table.focus()
        content=self.hotel_table.item(cursor_row)
        row=content["values"]

    def get_data(self):
        if  self.roomno_entry.get()=="" or self.floor_entry.get()=="" or self.combo_category.get()=="" or self.combo_status.get()=="" :                                              
            messagebox.showerror("Error","all fields are requires",parent=self.root)
        else:
            try:   
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()    
                var="insert into detail values(:room_id,:floor,:category,:status)"
                cur.execute(var,(self.roomno_entry.get(),self.floor_entry.get(),self.combo_category.get(),self.combo_status.get()))
                con.commit()    
                self.fetch_data()                
                cur2=con.cursor()
                cur2.execute('select * from detail')
                res=cur2.fetchall()
                for i in res:
                    print(i)   
                cur.close()
                cur2.close()  
                con.close()
                messagebox.showinfo("Success","Registered Successfully")
            except Exception as es:                 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

    def delete(self):
        if  self.roomno_entry.get()=="":
            messagebox.showerror('Error','Nothing to delete')
        else:
            try:
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor() 
                st="delete from detail where room_id='"+self.roomno_entry.get()+"' "
                cur.execute(st)
                con.commit()
                cur.close()
                messagebox.showinfo('Success','Successfully deleted')
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

    def update(self):
        if self.roomno_entry.get()=="":
            messagebox.showerror("Error",'Nothing to update',parent=self.root)
        else:
            try:
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()
                cur.execute("update detail set floor=:1,category=:2,status=:3 where room_id=:4",(
                                                                                                            
                                                                                            self.floor_entry.get(),
                                                                                            self.combo_category.get(),
                                                                                            self.combo_status.get(),
                                                                                            self.roomno_entry.get()
                ))                                                                                                                                 
                con.commit()
                self.fetch_data()
                cur.close()
                messagebox.showinfo('Success','Successfully Updated')
            except Exception as es:
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

    def fetch_data(self):
        con=cx_Oracle.connect('scott/tiger')
        cur=con.cursor()    
        cur.execute("select * from detail")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.hotel_table.delete(*self.hotel_table.get_children())
            for i in rows:
                self.hotel_table.insert("",END,values=i)
            con.commit()
        con.close()

class Resturant:
    def __init__(self,root):
        self.root=root
        self.root.title('HOTEL RESTURENT')
        self.root.geometry('1600x900+0+0')
        # background color
        self.root.config(bg='orange')
        # background image 
        self.bg=ImageTk.PhotoImage(file=r"D:\python proj\food1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=220,y=13)
        # label
        lb=Label(self.root,text="RESTAURANTS",font=("Algerian",30,"bold"),bg="white",fg="orange",bd=4,relief=RIDGE)
        lb.place(x=500,y=5,width=450,height=70)
        # variable
        # beverages
        self.cold=IntVar()
        self.shake=IntVar()
        self.tea=IntVar()
        self.coffee=IntVar()
        self.mojito=IntVar()
        # snacks
        self.sandwich=IntVar()
        self.noddles=IntVar()
        self.pizza=IntVar()
        self.pasta=IntVar()
        self.fries=IntVar()
        # food
        self.dal=IntVar()
        self.chapati=IntVar()
        self.mushroom=IntVar()
        self.paneer=IntVar()
        self.man=IntVar()
        # total product price
        self.beverages_price=StringVar()
        self.snacks_price=StringVar()
        self.food_price=StringVar()
        # tax
        self.beverages_tax=StringVar()
        self.snacks_tax=StringVar()
        self.food_tax=StringVar()
        # customer
        self.c_name=StringVar()
        self.c_phn=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        # frame
        frame=Frame(self.root,bg='ghost white')
        frame.place(x=5,y=80,width=1510,height=650)
        # Customer detail frame 
        F1=LabelFrame(self.root,bd=10,text="Customer Details",font=("times new roman",15,"bold"),fg='black',bg='ghost white')
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font=("ariel",15)).grid(row=0,column=1,padx=10,pady=5)
        phn_lbl=Label(F1,text="Customer Phone Number",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        phn_txt=Entry(F1,width=15,textvariable=self.c_phn,font=("ariel",15)).grid(row=0,column=3,padx=10,pady=5)
        c_bill_lbl=Label(F1,text="Bill Number",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font=("ariel",15)).grid(row=0,column=5,padx=10,pady=5)
        bill_btn=Button(F1,text="SEARCH",command=self.find_bill,borderwidth=0,font=('times new roman',15,'bold'),fg='black',bg='white')
        bill_btn.place(x=1300,y=3,width=150)
        # beverages Frame
        F2=LabelFrame(self.root,bd=10,text="Beverages",font=("times new roman",15,"bold"),fg='black',bg='ghost white')
        F2.place(x=5,y=180,height=325,width=380)
        Cold_lbl=Label(F2,text="Cold Drink",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Cold_txt=Entry(F2,width=20,textvariable=self.cold,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=0,column=1,padx=10,pady=10)
        shake_lbl=Label(F2,text="Shake",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=1,column=0,padx=10,pady=10,sticky="w")
        shake_txt=Entry(F2,width=20,textvariable=self.shake,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=1,column=1,padx=10,pady=10)
        tea_lbl=Label(F2,text="Tea",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=2,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F2,width=20,textvariable=self.tea,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=2,column=1,padx=10,pady=10)
        Coffee_lbl=Label(F2,text="Coffee",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Coffee_txt=Entry(F2,width=20,textvariable=self.coffee,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=3,column=1,padx=10,pady=10)
        mojito_lbl=Label(F2,text="Mojito",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=4,column=0,padx=10,pady=10,sticky="w")
        mojito_txt=Entry(F2,width=20,textvariable=self.mojito,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=4,column=1,padx=10,pady=10)
        # Snacks Frame
        F3=LabelFrame(self.root,bd=10,text="Snacks",font=("times new roman",15,"bold"),fg='black',bg='ghost white')
        F3.place(x=400,y=180,height=325,width=380)
        sandwich_lbl=Label(F3,text="Sandwich",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=0,column=0,padx=10,pady=10,sticky="w")
        sandwich_txt=Entry(F3,width=20,textvariable=self.sandwich,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=0,column=1,padx=10,pady=10)
        noddles_lbl=Label(F3,text="Noodles",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=1,column=0,padx=10,pady=10,sticky="w")
        noddles_txt=Entry(F3,width=20,textvariable=self.noddles,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=1,column=1,padx=10,pady=10)
        Pizza_lbl=Label(F3,text="Pizza",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Pizza_txt=Entry(F3,width=20,textvariable=self.pizza,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=2,column=1,padx=10,pady=10)
        Pasta_lbl=Label(F3,text="Pasta",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Pasta_txt=Entry(F3,width=20,textvariable=self.pasta,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=3,column=1,padx=10,pady=10)
        Fries_lbl=Label(F3,text="Fries",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Fries_txt=Entry(F3,width=20,textvariable=self.fries,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=4,column=1,padx=10,pady=10)
        # food table
        F4=LabelFrame(self.root,bd=10,text="Food",font=("times new roman",15,"bold"),fg='black',bg='ghost white')
        F4.place(x=800,y=180,height=325,width=380)
        Dal_lbl=Label(F4,text="Dal",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Dal_txt=Entry(F4,width=20,textvariable=self.dal,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=0,column=1,padx=10,pady=10)
        chapati_lbl=Label(F4,text="Chapati",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=1,column=0,padx=10,pady=10,sticky="w")
        chapati_txt=Entry(F4,width=20,textvariable=self.chapati,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=1,column=1,padx=10,pady=10)
        mushroom_lbl=Label(F4,text="Mushroom",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=2,column=0,padx=10,pady=10,sticky="w")
        mushroom_txt=Entry(F4,width=20,textvariable=self.mushroom,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=2,column=1,padx=10,pady=10)
        Paneer_lbl=Label(F4,text="Shahi Paneer",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Paneer_txt=Entry(F4,width=20,textvariable=self.paneer,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=3,column=1,padx=10,pady=10)
        man_lbl=Label(F4,text="Manchurian",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=4,column=0,padx=10,pady=10,sticky="w")
        man_txt=Entry(F4,width=20,textvariable=self.man,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=4,column=1,padx=10,pady=10)
        # Bill Area
        F5=LabelFrame(self.root,bd=10,font=("times new roman",15,"bold"),fg='black',bg='white')
        F5.place(x=1200,y=180,height=325,width=330)
        bill_title=Label(F5,text="Bill Area",font=("times new roman",15,"bold"),bd=7).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        # Buttom frame
        F6=LabelFrame(self.root,bd=10,text="Bill Menu",font=("times new roman",15,"bold"),fg='black',bg='ghost white')
        F6.place(x=0,y=510,height=200,width=1525)
        bev_lbl=Label(F6,text="Total Beverages Price",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bev_txt=Entry(F6,width=20,textvariable=self.beverages_price,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=0,column=1,padx=10,pady=10)
        snake_lbl=Label(F6,text="Total Snacks Price ",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=1,column=0,padx=10,pady=10,sticky="w")
        snake_txt=Entry(F6,width=20,textvariable=self.snacks_price,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=1,column=1,padx=10,pady=10)
        food_lbl=Label(F6,text="Total Food Price",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=2,column=0,padx=10,pady=10,sticky="w")
        food_txt=Entry(F6,width=20,textvariable=self.food_price,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=2,column=1,padx=10,pady=10)
        bev_tax_lbl=Label(F6,text="Total Beveages Tax",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=0,column=2,padx=10,pady=10,sticky="w")
        bev_tax_txt=Entry(F6,width=20,textvariable=self.beverages_tax,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=0,column=3,padx=10,pady=10)
        snake_tax_lbl=Label(F6,text="Total Snacks Tax",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=1,column=2,padx=10,pady=10,sticky="w")
        snake_tax_txt=Entry(F6,width=20,textvariable=self.snacks_tax,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=1,column=3,padx=10,pady=10)
        food_tax_lbl=Label(F6,text="Total Food Tax",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=2,column=2,padx=10,pady=10,sticky="w")
        food_tax_txt=Entry(F6,width=20,textvariable=self.food_tax,font=("times new roman",15,"bold"),fg='black',bg='ghost white',bd=5).grid(row=2,column=3,padx=10,pady=10)
        btn_F=Frame(F6,bd=7)
        btn_F.place(x=900,width=600,height=130)
        total_btn=Button(btn_F,text="Total",command=self.total,bg="white",fg="black",pady=15,width=11,font=("times new roman",15,"bold")).grid(row=0,column=0,padx=5,pady=5)  
        gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="white",fg="black",pady=15,width=11,font=("times new roman",15,"bold")).grid(row=0,column=1,padx=5,pady=5)  
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="white",fg="black",pady=15,width=11,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=5,pady=5)  
        exit_btn=Button(btn_F,text="Exit",command=self.exit,bg="white",fg="black",pady=15,width=11,font=("times new roman",15,"bold")).grid(row=0,column=3,padx=5,pady=5)  
        self.welcome_bill()
    
    # total function
    def total(self):
        self.b_c_p=self.cold.get()*40
        self.b_s_p=self.shake.get()*80
        self.b_t_p=self.tea.get()*50
        self.b_co_p=self.coffee.get()*100
        self.b_m_p=self.mojito.get()*150
        self.total_beverages_price=(
                                    (self.b_c_p)+
                                    (self.b_s_p)+         
                                    (self.b_t_p)+         
                                    (self.b_co_p)+         
                                    (self.b_m_p)      
                                    )
        self.beverages_price.set("Rs. "+str(self.total_beverages_price))
        self.b_tax=round(self.total_beverages_price*0.05,2)
        self.beverages_tax.set("Rs. "+str(self.b_tax))
        self.s_s_p=self.sandwich.get()*80
        self.s_n_p=self.noddles.get()*80
        self.s_p_p=self.pizza.get()*350
        self.s_pa_p=self.pasta.get()*200
        self.s_f_p=self.fries.get()*90
        self.total_snacks_price=(
                                (self.s_s_p)+
                                (self.s_n_p)+         
                                (self.s_p_p)+         
                                (self.s_pa_p)+         
                                (self.s_f_p)      
                                )
        self.snacks_price.set("Rs. "+str(self.total_snacks_price))    
        self.s_tax=round(self.total_snacks_price*0.1,2)
        self.snacks_tax.set("Rs. "+str(self.s_tax))
        self.f_d_p=self.dal.get()*200
        self.f_c_p=self.chapati.get()*30
        self.f_m_p=self.mushroom.get()*350
        self.f_p_p=self.paneer.get()*300
        self.f_man_p=self.man.get()*350
        self.total_food_price=(
                                (self.f_d_p)+
                                (self.f_c_p)+         
                                (self.f_m_p)+         
                                (self.f_p_p)+         
                                (self.f_man_p)      
                            )
        self.food_price.set("Rs. "+str(self.total_food_price))
        self.f_tax=round(self.total_food_price*0.05,2)
        self.food_tax.set("Rs. "+str(self.f_tax))
        self.Total_bill= self.total_beverages_price+self.total_snacks_price+self.total_food_price+self.b_tax+self.s_tax+self.f_tax

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Our Resturant\n")
        self.txtarea.insert(END,f"\nBill Number\t\t\t:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name\t\t\t:{self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone  Number\t\t\t:{self.c_phn.get()}")
        self.txtarea.insert(END,f"\n========================================")
        self.txtarea.insert(END,f"\nItems\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n========================================")
  
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phn=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.beverages_price.get()=="Rs. 0.0" and self.snacks_price.get()=="Rs. 0.0" and self.food_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No item purchased")
        else:
            self.welcome_bill()
            # beverages
            if self.cold.get()!=0:
                self.txtarea.insert(END,f"\n Cold Drink\t\t{self.cold.get()}\t\t{self.b_c_p}")
            if self.shake.get()!=0:
                self.txtarea.insert(END,f"\n Shake\t\t{self.shake.get()}\t\t{self.b_s_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.b_t_p}")
            if self.coffee.get()!=0:
                self.txtarea.insert(END,f"\n Coffee\t\t{self.coffee.get()}\t\t{self.b_co_p}")
            if self.mojito.get()!=0:
                self.txtarea.insert(END,f"\nMojito\t\t{self.mojito.get()}\t\t{self.b_m_p}")
            # snacks
            if self.sandwich.get()!=0:
                self.txtarea.insert(END,f"\n Sandwich\t\t{self.sandwich.get()}\t\t{self.s_s_p}")
            if self.pizza.get()!=0:
                self.txtarea.insert(END,f"\n Pizza\t\t{self.pizza.get()}\t\t{self.s_p_p}")
            if self.pasta.get()!=0:
                self.txtarea.insert(END,f"\n Pasta\t\t{self.pasta.get()}\t\t{self.s_pa_p}")
            if self.fries.get()!=0:
                self.txtarea.insert(END,f"\n Fries\t\t{self.fries.get()}\t\t{self.s_f_p}")
            if self.noddles.get()!=0:
                self.txtarea.insert(END,f"\n Noddles\t\t{self.noddles.get()}\t\t{self.s_n_p}")
            # food
            if self.dal.get()!=0:
                self.txtarea.insert(END,f"\n Dal\t\t{self.dal.get()}\t\t{self.f_d_p}")
            if self.chapati.get()!=0:
                self.txtarea.insert(END,f"\n Chapati\t\t{self.chapati.get()}\t\t{self.f_c_p}")
            if self.paneer.get()!=0:
                self.txtarea.insert(END,f"\n Paneer\t\t{self.paneer.get()}\t\t{self.f_p_p}")
            if self.man.get()!=0:
                self.txtarea.insert(END,f"\n Manchurian\t\t{self.man.get()}\t\t{self.f_man_p}")
            if self.mushroom.get()!=0:
                self.txtarea.insert(END,f"\n Mushroom\t\t{self.mushroom.get()}\t\t{self.f_m_p}")
            self.txtarea.insert(END,f"\n------------------------------------")
            if self.beverages_tax.get()!="Rs.0.0":
                self.txtarea.insert(END,f"\nBeverages Tax\t\t{self.beverages_tax.get()}")
            if self.snacks_tax.get()!="Rs.0.0":
                self.txtarea.insert(END,f"\nSnacks Tax\t\t{self.snacks_tax.get()}")
            if self.food_tax.get()!="Rs.0.0":
                self.txtarea.insert(END,f"\nFood Tax\t\t{self.food_tax.get()}")
            self.txtarea.insert(END,f"\nTotal Bill   :\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END,f"\n------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
           self.bill_data=self.txtarea.get('1.0',END)
           f1=open("bills/"+str(self.bill_no.get())+".txt",'w')
           f1.write(self.bill_data)
           f1.close()
           messagebox.showinfo("Saved","Bill Saves Successfully")

        else:
           return

        if self.c_name.get()=="" or self.c_phn.get()==""  :                                              
                messagebox.showerror("Error","all fields are requires")
        else:   
            con=cx_Oracle.connect('scott/tiger')
            cur=con.cursor()    
            var="insert into rest values(:c_name,:c_phn,:c_id,:total_bill)"
            cur.execute(var,(self.c_name.get(),self.c_phn.get(),self.bill_no.get(),self.Total_bill))               
            cur2=con.cursor()
            cur2.execute('select * from rest')
            res=cur2.fetchall()
            for i in res:
                print(i)   
            cur.close()
            cur2.close()  
            con.close()
            messagebox.showinfo("Success","Registered Successfully")

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():          
                f1=open(f"bills/{i}",'r')                
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):
        # beverages
        self.cold.set(0)
        self.shake.set(0)
        self.tea.set(0)
        self.coffee.set(0)
        self.mojito.set(0)
        # snacks
        self.sandwich.set(0)
        self.noddles.set(0)
        self.pizza.set(0)
        self.pasta.set(0)
        self.fries.set(0)
        # food
        self.dal.set(0)
        self.chapati.set(0)
        self.mushroom.set(0)
        self.paneer.set(0)
        self.man.set(0)
        # total product price
        self.beverages_price.set("")
        self.snacks_price.set("")
        self.food_price.set("")
        # tax
        self.beverages_tax.set("")
        self.snacks_tax.set("")
        self.food_tax.set("")
        # customer
        self.c_name.set("")
        self.c_phn.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill
    def exit(self):
        op=messagebox.askyesno("EXIT","Do you reallu want to exit?")
        if op>0:
            self.root.destroy()

class bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing ")
        #variables
        self.billno=StringVar()
        z=random.randint(1000,9999)
        self.billno.set(z)
        self.cname=StringVar()
        self.contact=IntVar()
        self.email=StringVar()
        self.rno=StringVar()
        self.rent_var=StringVar()
        self.days_var=IntVar()
        self.search=StringVar()
        self.sub=StringVar()
        self.tax_var=StringVar()
        self.total_var=StringVar()
        #image1
        img=Image.open(r"D:\python proj\h11.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)
        #image2
        img1=Image.open(r"D:\python proj\h22.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lb1_img1=Label(self.root,image=self.photoimg1)
        lb1_img1.place(x=500,y=0,width=500,height=130)
        #image3
        img2=Image.open(r"D:\python proj\h33.jpeg")
        img2=img2.resize((520,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lb1_img2=Label(self.root,image=self.photoimg2)
        lb1_img2.place(x=1000,y=0,width=520,height=130)
        #image4
        img3=Image.open(r"D:\python proj\letter.jpeg")
        img3=img3.resize((300,150),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lb1_img3=Label(self.root,image=self.photoimg3)
        lb1_img3.place(x=0,y=135,width=300,height=150)
        #heading
        lb1_title1=Label(self.root,text="",font=("times new roman",35,"bold"),bg="black",fg="red")
        lb1_title1.place(x=300,y=135,width=1300,height=20)
        lb1_title=Label(self.root,text="BILLING",font=("times new roman",70,"bold"),bg="white",fg="red")
        lb1_title.place(x=300,y=160,width=1300,height=100)
        lb1_title2=Label(self.root,text="",font=("times new roman",35,"bold"),bg="black",fg="red")
        lb1_title2.place(x=300,y=250,width=1300,height=20)
        #main frame
        main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        main_frame.place(x=0,y=270,width=1530,height=500)
        #customer frame
        cust=LabelFrame(main_frame,text="CUSTOMER",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust.place(x=10,y=5,width=500,height=140)
        self.lb1_mob=Label(cust,text="Mobile No",font=("times new roman",12,"bold"),bg="white",fg="red")
        self.lb1_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(cust,textvariable=self.contact,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        self.lbname=Label(cust,text="Name",font=("times new roman",12,"bold"),bg="white",fg="red")
        self.lbname.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_name=ttk.Entry(cust,textvariable=self.cname,font=("times new roman",12,"bold"),width=24)
        self.entry_name.grid(row=1,column=1)
        self.lbemail=Label(cust,text="Email",font=("times new roman",12,"bold"),bg="white",fg="red")
        self.lbemail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entry_email=ttk.Entry(cust,textvariable=self.email,font=("times new roman",12,"bold"),width=24)
        self.entry_email.grid(row=2,column=1)
        #room frame
        room=LabelFrame(main_frame,text="ROOM INFORMATION",font=("times new roman",12,"bold"),bg="white",fg="red")
        room.place(x=520,y=5,width=450,height=140)
        self.lb1_roomno=Label(room,text="Room id",font=("times new roman",12,"bold"),bg="white",fg="red")
        self.lb1_roomno.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_roomno=ttk.Entry(room,textvariable=self.rno,font=("times new roman",12,"bold"),width=24)
        self.entry_roomno.grid(row=0,column=1)
        self.rent=Label(room,text="Room Rent",font=("times new roman",12,"bold"),bg="white",fg="red")
        self.rent.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_rent=ttk.Entry(room,textvariable=self.rent_var,font=("times new roman",12,"bold"),width=24)
        self.entry_rent.grid(row=1,column=1)
        self.days=Label(room,text="Number of Days",font=("times new roman",12,"bold"),bg="white",fg="red")
        self.days.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entry_days=ttk.Entry(room,textvariable=self.days_var,font=("times new roman",12,"bold"),width=24)
        self.entry_days.grid(row=2,column=1)
        #middle frame
        middleframe=Frame(self.root,bd=10)
        middleframe.place(x=11,y=420,width=963,height=250)
        img_2=Image.open(r"D:\python proj\bill.jpeg")
        img_2=img_2.resize((500,250),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        lb1_img2=Label(middleframe,image=self.photoimg_2)
        lb1_img2.place(x=0,y=0,width=500,height=250)
        img_3=Image.open(r"D:\python proj\bill.jpeg")
        img_3=img_3.resize((500,250),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        lb1_img3=Label(middleframe,image=self.photoimg_3)
        lb1_img3.place(x=500,y=0,width=500,height=250)
        #search
        searchframe=Frame(main_frame,bd=2,bg="white")
        searchframe.place(x=980,y=0,width=520,height=40)
        self.lbbill=Label(searchframe,font=("times new roman",12,"bold"),fg="white",bg="red",text="BILL ")
        self.lbbill.grid(row=0,column=0,sticky=W,padx=1)        
        #right bill area
        rightframe=LabelFrame(main_frame,text="BILL AREA",font=("times new roman",12,"bold"),bg="white",fg="red")
        rightframe.place(x=980,y=45,width=520,height=350)
        scroll_y=Scrollbar(rightframe,orient=VERTICAL)
        self.textarea=Text(rightframe,yscrollcommand=scroll_y.set,bg="white",fg="black",font=("times new roman",12))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #lower frame
        bottomframe=LabelFrame(main_frame,text="BILL COUNTER",font=("times new roman",12,"bold"),bg="white",fg="red")
        bottomframe.place(x=0,y=393,width=1530,height=100)
        self.subtotal=Label(bottomframe,text="Sub Total",font=('arial',12,'bold'),bg='white',bd=4)
        self.subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entrysubtotal=ttk.Entry(bottomframe,textvariable=self.sub,font=('arial',12,'bold'),width=24)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.tax=Label(bottomframe,text="Tax",font=('arial',12,'bold'),bg='white',bd=4)
        self.tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entrytax=ttk.Entry(bottomframe,textvariable=self.tax_var,font=('arial',12,'bold'),width=24)
        self.entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.amount=Label(bottomframe,text="Amount",font=('arial',12,'bold'),bg='white',bd=4)
        self.amount.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        self.entryamount=ttk.Entry(bottomframe,textvariable=self.total_var,font=('arial',12,'bold'),width=24)
        self.entryamount.grid(row=0,column=4,sticky=W,padx=5,pady=2)
        #button
        btnframe=Frame(bottomframe,bd=2,bg='white')
        btnframe.place(x=650,y=0)
        self.add=Button(btnframe,height=2,text="ADD",command=self.additem,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.add.grid(row=0,column=0)
        self.generatebill=Button(btnframe,height=2,text="GENERATE BILL",command=self.gen_bill,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.generatebill.grid(row=0,column=1)
        self.save=Button(btnframe,height=2,text="SAVE BILL",command=self.save_bill,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.save.grid(row=0,column=2)
        self.clear=Button(btnframe,height=2,text="SEARCH DETAILS",command=self.search_data,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.clear.grid(row=0,column=4)
        self.additem()        

    def additem(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t\t WELCOME \n")
        self.textarea.insert(END,f"\n BILL NUMBER \t\t\t{self.billno.get()}")
        self.textarea.insert(END,f"\n MOBILE NUMBER \t\t\t{self.contact.get()}")
        self.textarea.insert(END,f"\n CUSTOMER NAME \t\t\t{self.cname.get()}")
        self.textarea.insert(END,f"\n EMAIL \t\t\t{self.email.get()}")
        self.textarea.insert(END,"\n=======================================================")
        self.textarea.insert(END,f"\n ROOM NUMBER\t\t\tRENT")
        self.textarea.insert(END,"\n=======================================================")       
        self.l=[]
        tax=1
        self.n=int(self.rent_var.get())
        self.m=self.days_var.get()*self.n
        self.l.append(self.m)
        if self.rent_var.get()=="":
            messagebox.showerror("error")
        else:        
            self.textarea.insert(END,f"\n{self.rno.get()}\t\t\t{self.m}")
            self.sub.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_var.set(str('Rs.%.2f'%(sum(self.l)*18/100)))
            self.total_var.set(str('Rs.%.2f'%((sum(self.l))+((sum(self.l)*18/100)))))

    def gen_bill(self):
         if self.rent_var.get()=="":
             messagebox.showerror("ERROR,Please enter rent of room")
         else:
             text=self.textarea.get(10.0,(10.0+float(len(self.l))))
             self.additem()
             self.textarea.insert(END,"\n=======================================================")
             self.textarea.insert(END,f"\n SUB TOTAL \t\t\t{self.sub.get()}")
             self.textarea.insert(END,f"\n TAX AMOUNT \t\t\t{self.tax_var.get()}")
             self.textarea.insert(END,f"\n TOTAL AMOUNT \t\t\t{self.total_var.get()}")
             self.textarea.insert(END,"\n=======================================================") 

    def save_bill(self):
        if self.contact.get()=="" :                                              
                messagebox.showerror("Error","all fields are requires",parent=self.root)            
        else:
            try:   
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()    
                var="insert into bill values(:billno,:contact,:name,:email,:roomno,:rent,:days)"
                cur.execute(var,(self.billno.get(),self.contact.get(),self.cname.get(),self.email.get(),self.rno.get(),self.rent_var.get(),self.days_var.get()))
                con.commit()                                   
                cur2=con.cursor()
                cur2.execute('select * from bill')
                res=cur2.fetchall()
                for i in res:
                    print(i)   
                cur.close()
                cur2.close()  
                con.close()
                messagebox.showinfo("Success","Saved successfully",parent=self.root)
            except Exception as es:                     
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)   

    def search_data(self):        
            con=cx_Oracle.connect('scott/tiger')
            cur=con.cursor()
            nn=self.contact.get()
            n=self.contact.get()
            var="select room_id,rent,number_of_days,name,email from booking join customer using (contact)  where contact=:m"
            cur.execute(var,{'m':nn})
            rows=cur.fetchall()
            if len(rows)!=0:
                        for i in rows:
                            self.entry_roomno.insert("",i[0])
                            self.entry_rent.insert("",i[1])
                            self.entry_days.insert("",i[2])
                            self.entry_name.insert("",i[3])
                            self.entry_email.insert("",i[4])
                            con.commit()
            con.close()
main()