from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from unicodedata import category
from PIL import Image,ImageTk
from matplotlib.pyplot import text
# from numpy import number
import cx_Oracle

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
        roomno=Label(frame,text="Room NUMBER",font=('times new roman',15,'bold'),bg="white")
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

      
        b4=Button(frame,text="BILL",borderwidth=0,font=('times new roman',15,'bold'),fg='white',bg='black')
        b4.place(x=500,y=350,width=100)

        # table frameid
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        detail_frame.place(x=0 ,y=100 ,width=813,height=550) 


    
        table_frame=Label(detail_frame,text="View details and search system",font=('times new roman',15,'bold'),bg="white",fg='plum')
        table_frame.place(x=10,y=20)

        # table_frame=Label(detail_frame,text="Search By",font=('times new roman',12,'bold'),bg="red",fg='white')
        # table_frame.place(x=10,y=48)

        # search=Label(detail_frame,text="Select ",font=('times new roman',13,'bold'),bg="white")
        # search.place(x=90,y=48)

        # self.search_var=StringVar()

        # self.combo_search=ttk.Combobox(detail_frame,textvariable=self.search_var ,font=("times new roman",12,"bold"),state="readonly")
        # self.combo_search["values"]=("select","Room No")
        # self.combo_search.place(x=160,y=48,width=80)
        # self.combo_search.current(0)

        # self.txt_search=StringVar()
        # self.search_entry=Entry(detail_frame,textvariable=self.txt_search,font=('times new roman',13,'bold'))
        # self.search_entry.place(x=240,y=48,width=120)

        # b5=Button(detail_frame,text="SEARCH",borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        # b5.place(x=350,y=48,width=85)

        # b6=Button(detail_frame,text="SHOW ALL",borderwidth=0,font=('times new roman',11,'bold'),fg='white',bg='black')
        # b6.place(x=450,y=48,width=85)    

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
        # self.hotel_table.heading("rent",text="Room Rent")                                                                                  
        # self.hotel_table.heading("",text="City") 
        self.hotel_table["show"]="headings"

        self.hotel_table.column("room_id",width=200)
        self.hotel_table.column("floor",width=200)
        self.hotel_table.column("category",width=200)
        self.hotel_table.column("status",width=200)
        # self.hotel_table.column("rent",width=200)
        
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
            # try:
            con=cx_Oracle.connect('scott/tiger')
            cur=con.cursor()
            cur.execute("update detail set floor=:1,category=:2,status=:3 where room_id=:4",(
                                                                                                            # self.name_entry.get(),
                                                                                        self.floor_entry.get(),
                                                                                        self.combo_category.get(),
                                                                                        self.combo_status.get(),
                                                                                        # self.Checkout_entry.get(),
                                                                                        # self.Bill_entry.get(),
                                                                                        self.roomno_entry.get(),
                                                                                                            # self.aadhar_entry.get(),
                                                                                                            # self.City_entry.get(),
                                                                                                            # self.var_ref.get()
                                                                                                ))
                                                                                                                                    
                                                                                                                                
            con.commit()
            self.fetch_data()
            cur.close()
            messagebox.showinfo('Success','Successfully Updated')
            


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
     











root=Tk()
obj=Details(root)
root.mainloop()