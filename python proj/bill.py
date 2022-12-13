from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import cx_Oracle
import random 


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
        self.rno=IntVar()
        self.rent_var=IntVar()
        self.days_var=IntVar()
        self.search=StringVar()
        self.sub=StringVar()
        self.tax_var=StringVar()
        self.total_var=StringVar()
               
        #image1
        img=Image.open(r"D:\python proj\hotel.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)

        #image2
        img1=Image.open(r"D:\python proj\hotel.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lb1_img1=Label(self.root,image=self.photoimg1)
        lb1_img1.place(x=500,y=0,width=500,height=130)

        #image3
        img2=Image.open(r"D:\python proj\hotel.jpg")
        img2=img2.resize((520,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lb1_img2=Label(self.root,image=self.photoimg2)
        lb1_img2.place(x=1000,y=0,width=520,height=130)
      
        #image4
        img3=Image.open(r"D:\python proj\hotel.jpg")
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

        img_2=Image.open(r"D:\python proj\hotel.jpg")
        img_2=img_2.resize((500,250),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lb1_img2=Label(middleframe,image=self.photoimg_2)
        lb1_img2.place(x=0,y=0,width=500,height=250)
        
        img_3=Image.open(r"D:\python proj\hotel.jpg")
        img_3=img_3.resize((500,250),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
    
        lb1_img3=Label(middleframe,image=self.photoimg_3)
        lb1_img3.place(x=500,y=0,width=500,height=250)


        #search
        searchframe=Frame(main_frame,bd=2,bg="white")
        searchframe.place(x=980,y=0,width=520,height=40)
        self.lbbill=Label(searchframe,font=("times new roman",12,"bold"),fg="white",bg="red",text="BILL NUMBER")
        self.lbbill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_entry_search=ttk.Entry(searchframe,font=("arial",10,"bold"),width=24)
        self.txt_entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.btnsearch=Button(searchframe,height=0,text="SEARCH",font=("arial",15,"bold"),bg="orangered",fg="white",width=15)
        self.btnsearch.grid(row=0,column=2)
                  
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
        self.add=Button(btnframe,height=2,text="ADD",command=self.additem,font=("arial",15,"bold"),bg="orangered",fg="white",width=10,cursor="hand2")
        self.add.grid(row=0,column=0)

        self.generatebill=Button(btnframe,height=2,text="GENERATE BILL",command=self.gen_bill,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.generatebill.grid(row=0,column=1)

        self.save=Button(btnframe,height=2,text="SAVE BILL",command=self.save_bill,font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.save.grid(row=0,column=2)

        self.clear=Button(btnframe,height=2,text="CLEAR",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.clear.grid(row=0,column=4)

        self.exit=Button(btnframe,height=2,text="EXIT",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.exit.grid(row=0,column=6)
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
        self.n=self.rent_var.get()
        self.m=self.days_var.get()*self.n
        self.l.append(self.m)
        if self.rent_var.get()=="":
            messagebox.showerror("error")
        else:
        
            self.textarea.insert(END,f"\n{self.rno.get()}\t\t\t{self.m}")
            self.sub.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_var.set(str('Rs.%.2f'%((((sum(self.l))-(self.rent_var.get()))*tax)/100)))
            self.total_var.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.rent_var.get()))*tax)/100)))))
        

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
                  var="insert into bill1 values(:contact,:name,:email,:totalrent)"
                  cur.execute(var,(self.contact.get(),self.cname.get(),self.email.get(),self.total_var.get()))
                  con.commit()    
                  self.fetch_data()                
                  cur2=con.cursor()
                  cur2.execute('select * from bill1')
                  res=cur2.fetchall()
                  for i in res:
                      print(i)   
                  cur.close()
                  cur2.close()  
                  con.close()
                  messagebox.showinfo("Success","Saved successfully")
            except Exception as es:
                     
                      messagebox.showerror('Error',f'Error due to :{str(es)}',parent=self.root)

root=Tk()
obj=bill(root)
root.mainloop()

