from tkinter import *
import tkinter.messagebox as messagebox
import cx_Oracle as oracle


def insert():
    id=e_id.get()
    name=e_name.get()
    if(e_id.get()==""):
        print("error")
    else:
        conn=oracle.connect('scott/tiger')
        cursor=conn.cursor()
        cursor.execute("insert into sam values(' "+id+"','"+name+"')")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        conn.close()

        
def delete():
    if(e_id.get()==""):
        print("error")
    else:
        conn=oracle.connect('scott/tiger')
        cursor=conn.cursor()
        cursor.execute("delete from  sam where id=' "+e_id.get()+"'")
        cursor.execute("commit")
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        conn.close()
              
def update():
    id=e_id.get()
    name=e_name.get()
    if(e_id.get()==""):
        print("error")
    else:
        conn=oracle.connect('scott/tiger')
        cursor=conn.cursor()
        cursor.execute("update sam set name=' "+name+"'where id='"+id+"'")
        cursor.execute("commit")
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        conn.close()
root=Tk()
root.geometry("600x300")
root.title("connectivity")

id=Label(root,text="enter id",font=('bold',10))
id.place(x=20,y=30)
name=Label(root,text="enter name",font=('bold',10))
name.place(x=20,y=60)

e_id=Entry()
e_id.place(x=150,y=30)
e_name=Entry()
e_name.place(x=150,y=60)

insert=Button(root,text="insert",font=("bold",10),bg="white",command=insert)
insert.place(x=20,y=140)

delete=Button(root,text="delete",font=("bold",10),bg="white",command=delete)
delete.place(x=70,y=140)

update=Button(root,text="update",font=("bold",10),bg="white",command=update)
update.place(x=130,y=140)



root.mainloop()
