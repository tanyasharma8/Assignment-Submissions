from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from unicodedata import category
from PIL import Image,ImageTk
from matplotlib.pyplot import text
from numpy import number

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
        room_no.place(x=30,y=80)

        self.room_no_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.room_no_entry.place(x=30,y=110,width=250)

        # category of room

        category=Label(frame,text="Select Category of Room",font=('times new roman',15,'bold'),bg="white")
        category.place(x=30,y=150)

        self.combo_category=ttk.Combobox(frame ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_category["values"]=("select","AC ","NON- AC")
        self.combo_category.place(x=30,y=190,width=250)
        self.combo_category.current(0)

        # status of room

        status=Label(frame,text="Status Of Room",font=('times new roman',15,'bold'),bg="white")
        status.place(x=30,y=230)

        self.combo_status=ttk.Combobox(frame ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_status["values"]=("select","OCCUPIED","AVAILABLE")
        self.combo_status.place(x=30,y=270,width=250)
        self.combo_status.current(0)

        # price

        price=Label(frame,text=" Advance Price",font=('times new roman',15,'bold'),bg="white")
        price.place(x=30,y=310)

        self.price_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.price_entry.place(x=30,y=350,width=250)

        check_in=Label(frame,text="Check In",font=('times new roman',15,'bold'),bg="white")
        check_in.place(x=30,y=385)

        self.check_in_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.check_in_entry.place(x=30,y=415,width=250)

        check_out=Label(frame,text="Check out",font=('times new roman',15,'bold'),bg="white")
        check_out.place(x=30,y=460)

        self.check_out_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.check_out_entry.place(x=30,y=500,width=250)

        check_out=Label(frame,text="Number of Days",font=('times new roman',15,'bold'),bg="white")
        check_out.place(x=350,y=80)

        self.check_out_entry=Entry(frame,font=('times new roman',15,'bold'))
        self.check_out_entry.place(x=350,y=110,width=250)

      


        # function declaration

        def booking_data(self):
            if self.var_rno.get()=="" or self.var_category.get()=="" or self.var_status.get()=="" or self.var_price.get()=="":
                messagebox.showerror("Error","all fiels are required")
        
            else:
                messagebox.showinfo("Success","Welcome")          




       
        


root=Tk()
obj=Room_Booking(root)
root.mainloop()