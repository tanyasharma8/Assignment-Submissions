from tkinter import *
from  PIL  import Image,ImageTk


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
        img1=img1.resize((1550,180),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        un=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        un.place(x=0,y=0,width=1550,height=180)

    # image 2

        img2=Image.open(r"D:\python proj\h1.jpg")
        img2=img2.resize((230,180),Image.Resampling.LANCZOS)
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
        custbtn=Button(frame_menu,text="CUSTOMER",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='Gold',bg='black',activeforeground='black',activebackground='black')
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

root=Tk()
obj=hotelmanagement(root)
root.mainloop()
