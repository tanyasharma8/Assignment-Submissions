from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import cx_Oracle
import random




class Room_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title('ROOM BOOKING')
        self.root.geometry('1600x900+0+0')
        
        # variable declaration
        
        self.var_rno=StringVar()
        self.var_category=StringVar()
        self.var_status=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_bill=StringVar()
        self.var_price=StringVar()
        self.var_ref=StringVar()
          
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
        # self.bg1=ImageTk.PhotoImage(file=r"D:\python proj\img2.jpg")
        # left_lbl=LabelFrame(image=self.bg1)
        # left_lbl.place(x=820,y=100,width=700,height=550)
        # frame=Frame(self.root,bd=10)
        # frame.place(x=820,y=100,width=700,height=550)

        # img1=Image.open(r"D:\python proj\images.jpg")
        # img1=img1.resize((100,100))
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lblimg1=Label(image=self.photoimage1,bg='black',borderwidth=0)
        # lblimg1.place(x=830,y=100,width=700,height=550)

        # label

        booking_label=Label(frame,text="ROOM BOOKING DETAILS",font=('times new roman',30,'bold'),bg="ghost white",fg="plum")
        booking_label.place(x=30,y=30)

        # label and entry
        # room number
        cust_id=Label(frame,text="Customer ID",font=('times new roman',15,'bold'),bg="white")
        cust_id.place(x=80,y=100)

        self.cust_id_entry=Entry(frame,textvariable=self.var_ref,font=('times new roman',15,'bold'))
        self.cust_id_entry.place(x=80,y=130,width=250)

        # category of room

        # category=Label(frame,text="Select Category of Room",font=('times new roman',15,'bold'),bg="white")
        # category.place(x=80,y=170)

        # self.combo_category=ttk.Combobox(frame ,font=("times new roman",15,"bold"),state="readonly")
        # self.combo_category["values"]=("select","AC ","NON- AC")
        # self.combo_category.place(x=80,y=200,width=250)
        # self.combo_category.current(0)

        # status of room

        # status=Label(frame,text="Status Of Room",font=('times new roman',15,'bold'),bg="white")
        # status.place(x=80,y=250)

        # self.combo_status=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
        # self.combo_status["values"]=("select","OCCUPIED","AVAILABLE")
        # self.combo_status.place(x=80,y=280,width=250)
        # self.combo_status.current(0)

        # price

        # price=Label(frame,text="Advance",font=('times new roman',15,'bold'),bg="white")
        # price.place(x=80,y=320)

        # self.price_entry=Entry(frame,font=('times new roman',15,'bold'))
        # self.price_entry.place(x=80,y=350,width=250)

        
        roomno=Label(frame,text="Room Number",font=('times new roman',15,'bold'),bg="white")
        roomno.place(x=80,y=170)

        roomno_entry=Entry(frame,textvariable=self.var_rno,font=('times new roman',15,'bold'))
        roomno_entry.place(x=80,y=200,width=250)

        Checkin=Label(frame,text="Check In",font=('times new roman',15,'bold'),bg="white")
        Checkin.place(x=80,y=250)

        Checkin_entry=Entry(frame,textvariable=self.var_checkin,font=('times new roman',15,'bold'))
        Checkin_entry.place(x=80,y=280,width=250)

        Checkout=Label(frame,text="Check Out",font=('times new roman',15,'bold'),bg="white")
        Checkout.place(x=350,y=100)

        Checkout_entry=Entry(frame,textvariable=self.var_checkout,font=('times new roman',15,'bold'))
        Checkout_entry.place(x=350,y=130,width=250)

        Bill=Label(frame,text="Room Rent",font=('times new roman',15,'bold'),bg="white")
        Bill.place(x=350,y=170)

        Bill_entry=Entry(frame,textvariable=self.var_bill,font=('times new roman',15,'bold'))
        Bill_entry.place(x=350,y=200,width=250)

        but1=Button(frame,text="ADD",command=self.get_data,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        but1.place(x=10,y=430,width=100)

        b2=Button(frame,text="UPDATE",command=self.update,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b2.place(x=150,y=430,width=100)

        b3=Button(frame,text="DELETE",command=self.delete,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b3.place(x=300,y=430,width=100)

        # b4=Button(frame,text="RESET",borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        # b4.place(x=450,y=430,width=100)          

        # b4=Button(frame,text="BILL",command=self.user_window6,borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        # b4.place(x=450,y=430,width=100)

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        detail_frame.place(x=0 ,y=100 ,width=818,height=550) 


    
        table_frame=Label(detail_frame,text="View details",font=('times new roman',15,'bold'),bg="grey",fg='black')
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

        self.hotel_table=ttk.Treeview(table_frame,columns=("cust_id","room_id","checkin","checkout","rent"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)
        self.hotel_table.heading("cust_id",text="Customer Id") 
        self.hotel_table.heading("room_id",text="Room No")                                                                                  
                                                                                          
        self.hotel_table.heading("checkin",text="Check In")                                                                                                                                                                 
        self.hotel_table.heading("checkout",text="Check Out")                                                                                  
        self.hotel_table.heading("rent",text="Room Rent")                                                                                  
        # self.hotel_table.heading("",text="City") 
        self.hotel_table["show"]="headings"

        self.hotel_table.column("cust_id",width=200)
        self.hotel_table.column("room_id",width=200)
        self.hotel_table.column("checkin",width=200)
        self.hotel_table.column("checkout",width=200)
        self.hotel_table.column("rent",width=200)
        # self.hotel_table.column("Post",width=100)
        # self.hotel_table.column("aadhar",width=100)
        # self.hotel_table.column("City",width=100)


        self.hotel_table.pack(fill=BOTH,expand=1)                                                                               
        self.hotel_table.bind("<ButtonRelease-1>",self.get_cursur)
        self.fetch_data()

    def get_cursur(self,event=""):
        cursor_row=self.hotel_table.focus()
        content=self.hotel_table.item(cursor_row)
        row=content["values"]    
        self.var_ref.set(row[0]),
        self.var_rno.set(row[1]),
        self.var_checkin.set(row[2]),
        self.var_checkout.set(row[3])
        self.var_bill.set(row[4])
        # self.var_post.set(row[5]),
        # self.var_aadhar.set(row[6]),
        # self.var_city.set(row[7])


        
    def get_data(self):
        if self.cust_id_entry.get()=="" or self.var_rno.get()=="" or self.var_checkin.get()=="" or self.var_checkout.get()=="" or self.var_bill.get()=="" :                                              
            messagebox.showerror("Error","all fields are requires",parent=self.root)
        else:
            try:   
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()    
                var="insert into booking values(:cust_no,:room_id,:checkin,:checkout,:rent)"
                cur.execute(var,(self.cust_id_entry.get(),self.var_rno.get(),self.var_checkin.get(),self.var_checkout.get(),self.var_bill.get()))
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
                # var_ref=input("enter Customer ID which you want to delete:")
                st="delete from booking where room_id='"+self.var_rno.get()+"' "
                cur.execute(st)
                con.commit()
                cur.close()
                messagebox.showinfo('Success','Successfully deleted')
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)



            

# cust_no,:room_id,:checkin,:checkout,:rent
    def update(self):
        if self.var_rno.get()=="":
            messagebox.showerror("Error",'Nothing to update',parent=self.root)
        else:
            try:
                con=cx_Oracle.connect('scott/tiger')
                cur=con.cursor()
                cur.execute("update booking set cust_no=:1,checkin=:2,checkout=:3,rent=:4 where room_id=:5",(
                                                                                                        # self.name_entry.get(),
                                                                                                        self.cust_id_entry.get(),
                                                                                                        self.var_checkin.get(),
                                                                                                        self.var_checkout.get(),
                                                                                                        self.var_bill.get(),
                                                                                                        self.var_rno.get(),
                                                                                                        # self.aadhar_entry.get(),
                                                                                                        # self.City_entry.get(),
                                                                                                        # self.var_ref.get()
                                                                                                        ))                                                                                                                                                                                                                                                                      
                con.commit()
                self.fetch_data()
                cur.close()
                messagebox.showinfo('Success','Successfully Updated')
            except Exception as es: 
                messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

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





        
                    
root=Tk()
obj=Room_Booking(root)
root.mainloop()