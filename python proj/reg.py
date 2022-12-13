from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from matplotlib.pyplot import text
import cx_Oracle
import random




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('REGISTER')
        self.root.geometry('1600x900+0+0')
        
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        # #variables
        # self.var_fname=StringVar()
        # self.var_lname=StringVar()
        # self.var_contact=StringVar()
        # self.var_email=StringVar()
        # self.var_sex=StringVar()
        # self.var_address=StringVar()
        # self.var_aadhar=StringVar()
        # self.var_city=StringVar()
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
        register_label=Label(frame,text="REGISTER HERE",font=('times new roman',20,'bold'),bg="white",fg="blue")
        register_label.place(x=20,y=20)
        

        #label and entry
# first name
        cno=Label(frame,text="Customer NO.",font=('times new roman',15,'bold'),bg="white")
        cno.place(x=50,y=100)

        cno_entry=Entry(frame,textvariable=self.var_ref,font=('times new roman',15,'bold'))
        cno_entry.place(x=50,y=130,width=250)


#  last name  
        name=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg="white")
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
        Post=Label(frame,text="Post_code",font=('times new roman',15,'bold'),bg="white")
        Post.place(x=400,y=220)

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


        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='grey')
        detail_frame.place(x=510 ,y=570 ,width=800,height=350) 


    
        table_frame=Label(detail_frame,text="View details and search system",font=('times new roman',12,'bold'),bg="grey",fg='black')
        table_frame.place(x=10,y=20)

        table_frame=Label(detail_frame,text="Search By",font=('times new roman',12,'bold'),bg="blue",fg='white')
        table_frame.place(x=10,y=48)

        search=Label(detail_frame,text="Select ",font=('times new roman',13,'bold'),bg="white")
        search.place(x=90,y=48)

        self.combo_search=ttk.Combobox(detail_frame ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_search["values"]=("select","Contact","Cust_id")
        self.combo_search.place(x=160,y=48,width=80)
        self.combo_search.current(0)

        self.search_entry=Entry(detail_frame,font=('times new roman',13,'bold'))
        self.search_entry.place(x=240,y=48,width=120)

        b5=Button(detail_frame,text="SEARCH",borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        b5.place(x=350,y=48,width=85)

        b6=Button(detail_frame,text="SHOW ALL",borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        b6.place(x=450,y=48,width=85)                     

        # table frame

        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg='white')
        table_frame.place(x=10 ,y=80 ,width=800,height=150)
        
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
        self.hotel_table.heading("Post",text="Post Code")                                                                                  
        self.hotel_table.heading("aadhar",text="Aadhar No")                                                                                  
        self.hotel_table.heading("City",text="City") 
        self.hotel_table["show"]="headings"

        self.hotel_table.column("cno",width=100)
        self.hotel_table.column("name",width=100)
        self.hotel_table.column("contact",width=100)
        self.hotel_table.column("email",width=100)
        self.hotel_table.column("sex",width=100)
        self.hotel_table.column("Post",width=100)
        self.hotel_table.column("aadhar",width=100)
        self.hotel_table.column("City",width=100)


        self.hotel_table.pack(fill=BOTH,expand=1)                                                                               

        self.fetch_data()


#  function declarartion  
 
    def register_data(self):
        if  self.contact_entry.get()=="" or self.email_entry.get()=="" or self.combo_sexA.get()=="" or self.aadhar_entry.get()=="" or self.post_entry.get()=="" or self.City_entry.get()=="":
            messagebox.showerror("Error","all fields are requires",parent=self.root)
        elif self.var_check==0:
            messagebox.showerror("Error",'Please agree terms and conditions')
        else:   
            con=cx_Oracle.connect('scott/tiger')
            cur=con.cursor()    
            var="insert into customer values(:cno,:name,:contact,:email,:sex,:post,:addhar,:city)"
            cur.execute(var,(self.name_entry.get(),self.contact_entry.get(),self.email_entry.get(),self.combo_sexA.get(),self.post_entry.get(),self.aadhar_entry.get(),self.City_entry.get()))
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


root=Tk()                                                                                  
obj=Register(root)
root.mainloop()































