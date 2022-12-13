from tkinter import *
from tkinter import ttk
from random import randint
from ims_bill import Bill_App
import customtkinter
import pymysql
from datetime import datetime

customtkinter.set_default_color_theme("green") 

class Stock:
    def __init__(self,root):
        self.root=root
        self.root.title("Meta Management System")
        self.root.geometry("1350x700+0+0")

        title=customtkinter.CTkLabel(self.root,text="Meta Management System",font=("Sawasdee",40,"bold"))
        title.pack(side=TOP,fill=X)

        #===========All Variables==============


        self.item_no = IntVar()
        self.item_name=StringVar()
        self.item_qty=IntVar()
        self.item_qty.set(0)
        self.item_price=IntVar()
        self.item_guage = StringVar()
        self.item_color = StringVar()
        self.expense = IntVar()


        self.item_id=StringVar()
        self.stock_quantity=StringVar()

        #=========Creating Menus for project=======================

        main_menu=Menu(self.root)
        self.root.config(menu=main_menu)

        fileMenu=Menu(main_menu)
        main_menu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Bill Section", command=self.openBill)
        fileMenu.add_command(label="Customer Section", command=self.openCustomerDetails)
        fileMenu.add_command(label="Stock Section", command=self.openStock)
        fileMenu.add_command(label="Daily Expenses", command=self.openDE)
        fileMenu.add_command(label="Orders", command=self.openOrders)
        fileMenu.add_command(label="Raw Materials",command=self.RawMaterial)
        fileMenu.add_command(label="Employees",command=self.openEmployee)
        fileMenu.add_command(label="Payouts",command=self.openPayouts)
        fileMenu.add_command(label="Exit", command=exit)

        #==========Menu ends here===================================

        #============Stock Entry Frame===============>

        Manage_Frame=customtkinter.CTkFrame(self.root)
        Manage_Frame.place(x=20,y=100,width=450,height=480)

        m_title=customtkinter.CTkLabel(Manage_Frame, text="Manage Stocks", font=("Sawasdee",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_item_color=customtkinter.CTkLabel(Manage_Frame, text="Item Color:", font=("Sawasdee",20,"bold"))
        lbl_item_color.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_item_color=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_color,font=("Sawasdee",10,"bold"))
        txt_item_color.grid(row=1,column=1,pady=10,padx=8,sticky="w")

        lbl_item_name=customtkinter.CTkLabel(Manage_Frame, text="Item Name:", font=("Sawasdee",20,"bold"))
        lbl_item_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_item_name=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_name,font=("Sawasdee",10,"bold"))
        txt_item_name.grid(row=2,column=1,pady=10,padx=8,sticky="w")

        lbl_item_price=customtkinter.CTkLabel(Manage_Frame, text="Item Price:", font=("Sawasdee",20,"bold"))
        lbl_item_price.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_item_price=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_price,font=("Sawasdee",10,"bold"))
        txt_item_price.grid(row=3,column=1,pady=10,padx=8,sticky="w")

        lbl_item_guage=customtkinter.CTkLabel(Manage_Frame, text="Item Guage:", font=("Sawasdee",20,"bold"))
        lbl_item_guage.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_item_guage=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_guage,font=("Sawasdee",10,"bold"))
        txt_item_guage.grid(row=4,column=1,pady=10,padx=8,sticky="w")

        g5_lbl=customtkinter.CTkLabel(Manage_Frame,text="In Stock:",font=("Sawasdee",16,"bold")).grid(row=5,column=0,padx=20,pady=10,sticky="w")
        g5_txt=customtkinter.CTkLabel(Manage_Frame,textvariable=self.item_qty,font=("Sawasdee",16,"bold")).grid(row=5,column=1,padx=10,pady=10,stick="w")


        

        #===========customtkinter.CTkButton Frame=============
        btn_Frame=customtkinter.CTkFrame(Manage_Frame)
        btn_Frame.place(x=8,y=400,width=430)

        Addbtn=customtkinter.CTkButton(btn_Frame,command=self.add_stock,text="Add",width=90).grid(row=0,column=0,padx=8,pady=10)
        updatebtn=customtkinter.CTkButton(btn_Frame,command=self.update_data,text="Update",width=90).grid(row=0,column=1,padx=8,pady=10)
        deletebtn=customtkinter.CTkButton(btn_Frame,command=self.delete_data,text="Delete",width=90).grid(row=0,column=2,padx=8,pady=10)
        Clearbtn=customtkinter.CTkButton(btn_Frame,command=self.clear,text="Clear",width=90).grid(row=0,column=3,padx=8,pady=10)



        #===========Detail Frame=====================

        Detail_Frame=customtkinter.CTkFrame(self.root)
        Detail_Frame.place(x=500,y=100,width=830,height=580)

        lbl_Search=customtkinter.CTkLabel(Detail_Frame,text="Select Item",font=("Sawasdee",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=customtkinter.CTkComboBox(Detail_Frame, variable=self.item_id,values=self.getItems(), width=100 ,font=("Sawasdee",13,"bold"))
        combo_search.grid(row=0,column=1, padx=20,pady=10)

        txt_Search=customtkinter.CTkEntry(Detail_Frame,textvariable=self.stock_quantity,width=120,font=("Sawasdee",10,"bold"))
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        txt_Search=customtkinter.CTkEntry(Detail_Frame,textvariable=self.expense,width=120,font=("Sawasdee",10,"bold"))
        txt_Search.grid(row=0,column=2,pady=10,padx=145,sticky="w")

        searchbtn=customtkinter.CTkButton(Detail_Frame,command=self.restock,text="Restock",width=10).grid(row=0,column=3,padx=10,pady=10)

        #=============Table Frame===========

        Table_Frame=customtkinter.CTkFrame(Detail_Frame)
        Table_Frame.place(x=10,y=70,width=795,height=490)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Stock_Table=ttk.Treeview(Table_Frame, column=("item_no","item_name","price","color","guage"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("item_no",text="ID")
        self.Stock_Table.heading("item_name",text="Item Name")
        self.Stock_Table.heading("price",text="Price")
        self.Stock_Table.heading("color",text="Color")
        self.Stock_Table.heading("guage",text="Guage")
        self.Stock_Table['show']='headings'
        self.Stock_Table.column("item_no",width=100)
        self.Stock_Table.column("item_name",width=360)
        self.Stock_Table.column("price",width=100)
        self.Stock_Table.column("color",width=100)
        self.Stock_Table.column("guage",width=100)
        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.fetch_date()
        self.Stock_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_stock(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"insert into stocks (name,price,color,guage) values ('{self.item_name.get()}',{self.item_price.get()},'{self.item_color.get()}','{self.item_guage.get()}')"
        cur.execute(statement)
        con.commit()
        self.fetch_date()
        self.clear()
        con.close()

    def getItems(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"select item_no from stocks"
        cur.execute(statement)
        rows = cur.fetchall()
        item_list = list()
        for r in rows:
            item_list.append(str(r[0]))
        con.commit()
        con.close()
        return item_list

    def fetch_date(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        cur.execute("select item_no,name,price,color,guage from stocks")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.item_no.set(str(randint(1,1000)))
        self.item_name.set("")
        self.item_price.set(0)
        self.item_qty.set(0)

    def get_cursor(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_price.set(row[2])
        self.item_color.set(row[3])
        self.item_guage.set(row[4])
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"select quantity from inventory where item_id = {row[0]}"
        cur.execute(statement)
        rows = cur.fetchall()
        total_quantity = 0
        for r in rows:
            total_quantity = total_quantity + r[0]

        self.item_qty.set(total_quantity)
        con.commit()
        con.close()

    def update_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"update stocks set item_no='{self.item_no.get()}', price={self.item_price.get()},name='{self.item_name.get()}',color='{self.item_color.get()}',guage='{self.item_guage.get()}' where item_no={self.item_no.get()}"
        cur.execute(statement)
        con.commit()
        self.fetch_date()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        cur.execute(f"delete from stocks where item_no='{self.item_no.get()}'")
        con.commit()
        con.close()
        self.fetch_date()
        self.clear()

    def restock(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"insert into inventory (item_id,quantity,expense,date) values ({self.item_id.get()},{self.stock_quantity.get()},{self.expense.get()},'{datetime.today().strftime('%Y-%m-%d')}')"
        cur.execute(statement)
        con.commit()
        con.close()
        self.get_cursor(0)

    def openStock(self):
        from ims_stock import Stock
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Stock(self.root)

    def openBill(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Bill_App(self.root)

    def openCustomerDetails(self):
        from mms_customer import Customer
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Customer(self.root)

    def openDE(self):
        from mms_daily import Daily
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Daily(self.root)

    def openOrders(self):
        from mms_orders import Order
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Order(self.root)

    def RawMaterial(self):
        from mms_raw_materials import Raw
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Raw(self.root)

    def openEmployee(self):
        from employee import Employee
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Employee(self.root)

    def openPayouts(self):
        from payouts import Payout
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Payout(self.root)
    
