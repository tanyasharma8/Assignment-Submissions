from re import I
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from matplotlib.pyplot import text
from pyparsing import common_html_entity
from setuptools import Command
import math,random
import os
import cx_Oracle

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
        lb=Label(self.root,text="RESTURANT",font=("Algerian",30,"bold"),bg="white",fg="orange",bd=4,relief=RIDGE)
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

        noddles_lbl=Label(F3,text="Noddles",font=("times new roman",15,"bold"),fg='black',bg='ghost white').grid(row=1,column=0,padx=10,pady=10,sticky="w")
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
        # self.beverages_tax.set("Rs. "+str(round((self.total_beverages_price*0.05)),2))
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
        # self.snacks_tax.set("Rs. "+str(round(self.total_snacks_price*0.05),2))
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
        # self.food_tax.set("Rs. "+str(round(self.total_food_price*0.05),2))
        self.f_tax=round(self.total_food_price*0.05,2)
        self.food_tax.set("Rs. "+str(self.f_tax))
   
        self.Total_bill= self.total_beverages_price+self.total_snacks_price+self.total_food_price+self.b_tax+self.s_tax+self.f_tax
                            

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Our Resturant\n")
        self.txtarea.insert(END,f"\nBill Number    :{self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name  :{self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone  Number  :{self.c_phn.get()}")
        self.txtarea.insert(END,f"\n####################################")
        self.txtarea.insert(END,f"\nItems\t\tQTY\tPrice")
        self.txtarea.insert(END,f"\n####################################")


    
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
            #elif self.var_check==0:
             #   messagebox.showerror("Error",'Please agree terms and conditions')
        else:
            # try:   
            con=cx_Oracle.connect('scott/tiger')
            cur=con.cursor()    
            var="insert into rest values(:c_name,:c_phn,:c_id,:total_bill)"
            cur.execute(var,(self.c_name.get(),self.c_phn.get(),self.bill_no.get(),self.Total_bill))
            con.commit()    
            # self.fetch_data()                
            cur2=con.cursor()
            cur2.execute('select * from rest')
            res=cur2.fetchall()
            for i in res:
                print(i)   
            cur.close()
            cur2.close()  
            con.close()
            messagebox.showinfo("Success","Registered Successfully")
            # except Exception as es:
            #     messagebox.showinfo("error","Registered UnSuccessfully")


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
            messagebox.showerror("Error","Invalis Bill Number")

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
    

root=Tk()
obj=Resturant(root)
root.mainloop()