from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import re
from matplotlib.pyplot import text
import pyttsx3




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('REGISTER')
        self.root.geometry('1600x900+0+0')


        # voice variable

        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)#1 for female voice(ID)
                
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
        register_label=Label(frame,text="REGISTER HERE",font=('times new roman',20,'bold'),bg="white",fg="blue")
        register_label.place(x=20,y=20)
        

        #label and entry

# first name
        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),bg="white")
        fname.place(x=50,y=100)

        fname_entry=Entry(frame,textvariable=self.var_fname,font=('times new roman',15,'bold'))
        fname_entry.place(x=50,y=130,width=250)
        
        # call back bind and validation register

        validate_name=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_name,'%P'))  #%P is screen formating

#  last name  
        lname=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg="white")
        lname.place(x=400,y=100)

        lname_entry=Entry(frame,textvariable=self.var_lname,font=('times new roman',15,'bold'))
        lname_entry.place(x=400,y=130,width=250)

        # callback bind nd validation

        validate_lname=self.root.register(self.checklastname)
        lname_entry.config(validate='key',validatecommand=(validate_lname,'%P'))  #%P is screen formating




# contact number
        contact=Label(frame,text="Contact Number",font=('times new roman',15,'bold'),bg="white")
        contact.place(x=50,y=160)

        contact_entry=Entry(frame,textvariable=self.var_contact,font=('times new roman',15,'bold'))
        contact_entry.place(x=50,y=190,width=250)

        validate_contact=self.root.register(self.checkcontact)
        contact_entry.config(validate='key',validatecommand=(validate_contact,'%P'))  #%P is screen formating


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

#     call back function
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
                return True
        else:
                messagebox.showerror('Invalid','Not allowed'+name[-1])

    def checklastname(self,name):
        if name.isalnum():
            return True
        if name==' ':
                return True
        else:
                messagebox.showerror('Invalid','No allowed'+name[-1])


    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
                return True
        else:
                messagebox.showerror('Invalid','No allowed')

#     def checkpassword(self,password):
#         if len(password)<=21
#             if re.match("^(?=.[0-9])(?=.[a-z])(?=.[A-Z](?=.*[^a-bA-B0-9]))",password):
#                 return True
#             else:
#                     message
#         else:
#                 messagebox.showerror('Invalid','No allowed'+name[-1])

    def validation(self):
            x=y=0
            if self.var_fname.get=="":
                    self.engine.say('please enter your name')
                    self.engine.runAndWait()
                    messagebox.showerror('Error','please enter your name',parent=self.root)









# function declarartion
# 
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" :
                messagebox.showerror("Error","all fiels are required")
        
        elif self.var_check.get()==0:
                messagebox.showerror("error","please agree terms and conditions")
        else:
                messagebox.showinfo("Success","Welcome")          

 
root=Tk()
obj=Register(root)
root.mainloop()