from tkinter import *
from tkinter import ttk
from random import randint
import pymysql
from datetime import datetime
from ims_bill import Bill_App
from tkcalendar import Calendar
import customtkinter

class Daily:
    def __init__(self,root):
        self.root=root
        self.root.title("Meta Management System")
        self.root.geometry("1350x700+0+0")

        title=customtkinter.CTkLabel(self.root,text="Meta Management System",font=("Sawasdee",40,"bold"))
        title.pack(side=TOP,fill=X)

        #===========All Variables==============

        self.expense_id=StringVar()
        self.expense_name = StringVar()
        self.expense_cost=IntVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #=========Creating Menus for project=======================

        main_menu=Menu(self.root)
        self.root.config(menu=main_menu)

        fileMenu=Menu(main_menu)
        main_menu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Bill Section", command=self.openBill)
        fileMenu.add_command(label="Stock Section", command=self.openStock)
        fileMenu.add_command(label="Customer Section", command=self.openCustomerDetails)
        fileMenu.add_command(label="Orders", command=self.openOrders)
        fileMenu.add_command(label="Raw Materials",command=self.RawMaterial)
        fileMenu.add_command(label="Employees",command=self.openEmployee)
        fileMenu.add_command(label="Payouts",command=self.openPayouts)
        fileMenu.add_command(label="Exit", command=exit)

        #==========Menu ends here===================================

        #============Stock Entry Frame===============>

        Manage_Frame=Frame(self.root)
        Manage_Frame.place(x=20,y=100,width=450,height=480)

        m_title=customtkinter.CTkLabel(Manage_Frame, text="Manage Customers", font=("Sawasdee",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_expense_name=customtkinter.CTkLabel(Manage_Frame, text="Expense Name:", font=("Sawasdee",20,"bold"))
        lbl_expense_name.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_expense_name=customtkinter.CTkEntry(Manage_Frame,textvariable=self.expense_name,font=("Sawasdee",10,"bold"))
        txt_expense_name.grid(row=1,column=1,pady=10,padx=8,sticky="w")

        lbl_expense_cost=customtkinter.CTkLabel(Manage_Frame, text="Expense Cost:", font=("Sawasdee",20,"bold"))
        lbl_expense_cost.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_expense_cost=customtkinter.CTkEntry(Manage_Frame,textvariable=self.expense_cost,font=("Sawasdee",10,"bold"))
        txt_expense_cost.grid(row=2,column=1,pady=10,padx=8,sticky="w")


        #===========Button Frame=============
        btn_Frame=Frame(Manage_Frame)
        btn_Frame.place(x=8,y=400,width=430)

        Addbtn=customtkinter.CTkButton(btn_Frame,command=self.add_expense,text="Add",width=90).grid(row=0,column=0,padx=8,pady=10)
        updatebtn=customtkinter.CTkButton(btn_Frame,command=self.update_data,text="Update",width=90).grid(row=0,column=1,padx=8,pady=10)
        deletebtn=customtkinter.CTkButton(btn_Frame,command=self.delete_data,text="Delete",width=90).grid(row=0,column=2,padx=8,pady=10)
        Ordersbtn=customtkinter.CTkButton(btn_Frame,command=self.clear,text="Orders",width=90).grid(row=0,column=3,padx=8,pady=10)



        #===========Detail Frame=====================

        Detail_Frame=Frame(self.root)
        Detail_Frame.place(x=500,y=100,width=830,height=580)

        lbl_Search=customtkinter.CTkLabel(Detail_Frame,text="Pick Date: ",font=("Sawasdee",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        self.cal = Calendar(Detail_Frame, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)

        self.cal.grid(row=0,column=1, padx=20,pady=10)
        showallbtn=customtkinter.CTkButton(Detail_Frame,command=self.fetch_date,text="Fetch",width=10).grid(row=0,column=4,padx=10,pady=10)

        # combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10 ,font=("Sawasdee",13,"bold"),state="readonly")
        # combo_search['values']=("Name","Contact")
        # combo_search.grid(row=0,column=1, padx=20,pady=10)

        # txt_Search=customtkinter.CTkEntry(Detail_Frame,textvariable=self.search_txt,width=20,font=("Sawasdee",10,"bold"))
        # txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        # searchbtn=customtkinter.CTkButton(Detail_Frame,command=self.search_data,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        # showallbtn=customtkinter.CTkButton(Detail_Frame,command=self.fetch_date,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #=============Table Frame===========

        Table_Frame=Frame(Detail_Frame)
        Table_Frame.place(x=10,y=190,width=795,height=350)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Customer_Table=ttk.Treeview(Table_Frame, column=("id","expense_name","expense_cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Customer_Table.xview)
        scroll_y.config(command=self.Customer_Table.yview)


        self.Customer_Table.heading("id",text="ID")
        self.Customer_Table.heading("expense_name",text="Expense Name")
        self.Customer_Table.heading("expense_cost",text="Expense Cost")
        self.Customer_Table['show']='headings'
        self.Customer_Table.column("id",width=100)
        self.Customer_Table.column("expense_name",width=100)
        self.Customer_Table.column("expense_cost",width=460)
        self.Customer_Table.pack(fill=BOTH,expand=1)
        self.fetch_date()
        self.Customer_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_expense(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"insert into daily_expenses (expense_name, expense_cost, date) values ('{self.expense_name.get()}','{self.expense_cost.get()}', '{datetime.today().strftime('%m/%d/%y')}')"
        cur.execute(statement)
        con.commit()
        self.fetch_date()
        self.clear()
        con.close()

    def fetch_date(self):
        self.Customer_Table.delete(*self.Customer_Table.get_children())
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        t_date = self.cal.get_date()
        cur.execute(f"select * from daily_expenses where date = '{t_date}'")
        rows=cur.fetchall()
        if len(rows)!=0:
            for row in rows:
                self.Customer_Table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.expense_id.set(0)
        self.expense_name.set("")
        self.expense_cost.set(0)

    def get_cursor(self,ev):
        cursor_row=self.Customer_Table.focus()
        contents=self.Customer_Table.item(cursor_row)
        row=contents['values']
        self.expense_id.set(row[0])
        self.expense_name.set(row[1])
        self.expense_cost.set(row[2])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"update daily_expenses set expense_name='{self.expense_name.get()}', expense_cost={self.expense_cost.get()} where id={self.expense_id.get()}"
        cur.execute(statement)
        con.commit()
        self.fetch_date()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        cur.execute(f"delete from daily_expenses where id='{self.expense_id.get()}'")
        con.commit()
        con.close()
        self.fetch_date()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        if f'{self.search_by.get()}'=='Name':
            statement=f"select * from daily_expenses where expense_name='{self.search_txt.get()}'"
        else:
            statement=f"select * from daily_expenses where expense_cost='{self.search_txt.get()}'"
        cur.execute(statement)
        self.Customer_Table.delete(*self.Customer_Table.get_children())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Customer_Table.delete(*self.Customer_Table.get_children())
            for row in rows:
                self.Customer_Table.insert('',END, values=row)
            con.commit()
        con.close()

    def openBill(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Bill_App(self.root)

    def openCustomerDetails(self):
        from mms_customer import Customer
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Customer(self.root)

    def openStock(self):
        from ims_stock import Stock
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Stock(self.root)

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
    
