from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from pip import main


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title('Register Page')
        self.root.geometry('1600x800+0+0')

        self.bg=ImageTk.PhotoImage(file="hotelimg.jpg")
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        logo_img=Image.open(r'D:\python proj\logo.img')
        logo_img=logo_img.resize(60,60)
        self.photo_logo=ImageTk.PhotoImage(logo_img)



    #   title Image

        title_frame=Frame(self.root)
        title_frame.place(x=450,y=28,width=550,height=88)
        title_lbl=Label(title_frame,text='USER REGISTRATION FORM',font=('times new roman',20,'bold'))
        title_lbl.place(x=10,y=10)


    # information frame

        info_frame=Frame(self.root,bg='white')
        info_frame.place(x=450,y=110,width=550,height=600)




    





if __name__=="__main__":
    root=Tk()
    o=Register(root)
    root.mainloop()