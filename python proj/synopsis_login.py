from logging import root
from tkinter import *
from PIL import Image,ImageTk
# from matplotlib import Image

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1600x900+0+0')
        self.root.title('Login Screen')

        # Background Image

        self.Back_img=ImageTk.PhotoImage(file=r"D:\python proj\hotelimg.jpg")
        label_img=Label(self.root,image=self.Back_img)
        label_img.place(x=0,y=0,relwidth=1,relheight=1)

        # Frame at the top for heading

        frame=Frame(self.root,bg='black')
        frame.place(x=10,y=10,width=1500,height=100)

        # Hotel Management Text AT top Frame

        get_text=Label(frame,text='HOTEL MANAGEMENT SYSTEM',font=('Times New Roman',30,'bold'),fg='White',bg='black')
        get_text.place(x=450,y=20)

        # Frame for Login

        frame2=Frame(self.root,bg='black')
        frame2.place(x=520,y=250,width=500,height=450)

        # login Image in Frame 2

        img=Image.open(r"D:\python proj\loginb2.jpg")
        img.resize((100,100),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        label_img2=Label(frame2,image=self.photoimage,bg='black',borderwidth=0)
        label_img2.place(x=160,y=10,width=200,height=100)

        # Username

        User_lbl=Label(frame2,text="Username",font=('Times New Roman',20,'bold'),bg='white',fg='black')
        User_lbl.place(x=30,y=130)

        # text_area

        txt_area=Entry(frame2,font=('Times New Roman',20,'bold'),bg='white',fg='black')
        txt_area.place(x=180,y=130,height=35,width=300)

        #Password

        pass_lbl=Label(frame2,text="Password",font=('Times New Roman',20,'bold'),bg='white',fg='black')
        pass_lbl.place(x=30,y=200)

        # text_area

        pass_area=Entry(frame2,font=('Times New Roman',20,'bold'),bg='white',fg='black')
        pass_area.place(x=180,y=200,height=35,width=300)
        
        # Login Button

        loginbtn=Button(frame2,text="LogIn",font=("times new romen",15,'bold'),bd=3,relief=RIDGE,fg='white',bg='grey',activeforeground='white',activebackground='grey')
        loginbtn.place(x=180,y=300,width=120,height=35)



root=Tk()
obj=Login(root)
root.mainloop()