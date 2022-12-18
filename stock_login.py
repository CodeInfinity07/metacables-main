from tkinter import *
from tkinter import messagebox
from ims_stock import Stock
import pymysql
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Meta Management System")
        self.root.geometry("1350x700+0+0")

        #===========All images=============#
        self.bg_icon=customtkinter.CTkImage(Image.open("images/bg.png"))
        self.user_icon=customtkinter.CTkImage(Image.open("images/man-user.png"))
        self.pass_icon=customtkinter.CTkImage(Image.open("images/password.png"))
        self.logo_icon=customtkinter.CTkImage(Image.open("images/logo.png"),size=(150,150))

        #===========Variables=============#
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=customtkinter.CTkLabel(self.root,image=self.bg_icon).pack()

        title=customtkinter.CTkLabel(self.root,text="Meta Management System",font=("Sawasdee",40,"bold"))
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=customtkinter.CTkFrame(self.root)
        Login_Frame.place(x=450,y=250)

        logolbl=customtkinter.CTkLabel(Login_Frame,image=self.logo_icon).grid(row=0,columnspan=2,pady=20)

        lbluser=customtkinter.CTkLabel(Login_Frame,text=" Username",image=self.user_icon,compound=LEFT,font=("Sawasdee",20,"bold")).grid(row=1,column=0,padx=20)
        txtuser=Entry(Login_Frame,textvariable=self.uname,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=customtkinter.CTkLabel(Login_Frame,text=" Password",image=self.pass_icon,compound=LEFT,font=("Sawasdee",20,"bold")).grid(row=2,column=0,padx=20)
        txtpass=Entry(Login_Frame,show="*",textvariable=self.pass_,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=customtkinter.CTkButton(Login_Frame,command=self.login,text="Login",width=15,font=("Sawasdee",14,"bold")).grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required")
            return
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        statement=f"select * from users where username='{self.uname.get()}' and pass='{self.pass_.get()}'"
        cur.execute(statement)
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showerror("Error","Invalid username or password")
            return
        messagebox.showinfo("Successful","Welcome ")
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Stock(self.root)
        con.commit()
        con.close()

root=customtkinter.CTk()
obb=login_system(root)
root.mainloop()
