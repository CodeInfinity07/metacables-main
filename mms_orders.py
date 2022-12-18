from tkinter import *
from tkinter import ttk
from random import randint
import pymysql
from ims_bill import Bill_App
import array as arr
import customtkinter

class Order:
    def __init__(self,root):
        self.root=root
        self.root.title("Meta Management System")
        self.root.geometry("1350x700+0+0")

        title=customtkinter.CTkLabel(self.root,text="Meta Management System",font=("Sawasdee",40,"bold"))
        title.pack(side=TOP,fill=X)

        #===========All Variables==============

        self.inv_id=StringVar()
        self.date=StringVar()
        self.amount=IntVar()
        self.is_paid=IntVar()
        self.cust_id = IntVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #=========Creating Menus for project=======================

        main_menu=Menu(self.root)
        self.root.config(menu=main_menu)

        fileMenu=Menu(main_menu)
        main_menu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Bill Section", command=self.openBill)
        fileMenu.add_command(label="Customer Section", command=self.openCustomerDetails)
        fileMenu.add_command(label="Stock Section", command=self.openStock)
        fileMenu.add_command(label="Daily Expenses", command=self.openDE)
        fileMenu.add_command(label="Raw Materials",command=self.RawMaterial)
        fileMenu.add_command(label="Employees",command=self.openEmployee)
        fileMenu.add_command(label="Payouts",command=self.openPayouts)
        fileMenu.add_command(label="Exit", command=exit)

        #==========Menu ends here===================================

        #============Stock Entry Frame===============>

        Manage_Frame=Frame(self.root)
        Manage_Frame.place(x=20,y=100,width=450,height=480)

        m_title=customtkinter.CTkLabel(Manage_Frame, text="Manage Stocks", font=("Sawasdee",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        cur.execute(f"select customer_name from registered_customers")
        rows=cur.fetchall()
        if len(rows) > 0:
            my_list = [r for r, in rows] 
            self.options = StringVar()
            self.options.set("")
            lbl_options=customtkinter.CTkLabel(Manage_Frame,text="Select Customer:",font=("Sawasdee",15,"bold")).grid(row=2,column=0,padx=20,pady=2,sticky="w")
            self.option_field = customtkinter.CTkOptionMenu(Manage_Frame, values=my_list, command=self.displayCustomer)
            self.option_field.grid(row=2,column=1)
            self.option_field['width'] = 15

        # lbl_item_no=customtkinter.CTkLabel(Manage_Frame, text="Item No:", font=("Sawasdee",20,"bold"))
        # lbl_item_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        # txt_item_no=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_no,font=("Sawasdee",10,"bold"))
        # txt_item_no.grid(row=1,column=1,pady=10,padx=8,sticky="w")

        # lbl_item_name=customtkinter.CTkLabel(Manage_Frame, text="Item Name:", font=("Sawasdee",20,"bold"))
        # lbl_item_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        # txt_item_name=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_name,font=("Sawasdee",10,"bold"))
        # txt_item_name.grid(row=2,column=1,pady=10,padx=8,sticky="w")

        # lbl_item_price=customtkinter.CTkLabel(Manage_Frame, text="Item Price:", font=("Sawasdee",20,"bold"))
        # lbl_item_price.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        # txt_item_price=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_price,font=("Sawasdee",10,"bold"))
        # txt_item_price.grid(row=3,column=1,pady=10,padx=8,sticky="w")

        # lbl_item_qty=customtkinter.CTkLabel(Manage_Frame, text="Item Quantity:", font=("Sawasdee",20,"bold"))
        # lbl_item_qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        # txt_item_qty=customtkinter.CTkEntry(Manage_Frame,textvariable=self.item_qty,font=("Sawasdee",10,"bold"))
        # txt_item_qty.grid(row=4,column=1,pady=10,padx=8,sticky="w")

        #===========Button Frame=============
        btn_Frame=Frame(Manage_Frame)
        btn_Frame.place(x=8,y=400,width=430)

        updatebtn=customtkinter.CTkButton(btn_Frame,command=self.update_data,text="Mark Paid",width=150).grid(row=0,column=1,padx=8,pady=10)


        #===========Detail Frame=====================

        Detail_Frame=Frame(self.root)
        Detail_Frame.place(x=500,y=100,width=830,height=580)


        # combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10 ,font=("Sawasdee",13,"bold"),state="readonly")
        # combo_search['values']=("Item No","Item Name")
        # combo_search.grid(row=0,column=1, padx=20,pady=10)

        # txt_Search=customtkinter.CTkEntry(Detail_Frame,textvariable=self.search_txt,width=20,font=("Sawasdee",10,"bold"))
        # txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        # searchbtn=customtkinter.CTkButton(Detail_Frame,command=self.search_data,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        # showallbtn=customtkinter.CTkButton(Detail_Frame,command=self.fetch_date,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #=============Table Frame===========

        Table_Frame=Frame(Detail_Frame)
        Table_Frame.place(x=10,y=30,width=795,height=520)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Stock_Table=ttk.Treeview(Table_Frame, column=("inv_id","date","amount","is_paid"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("inv_id",text="Bill ID")
        self.Stock_Table.heading("date",text="Transaction Date")
        self.Stock_Table.heading("amount",text="Amount")
        self.Stock_Table.heading("is_paid",text="Status")
        self.Stock_Table['show']='headings'
        self.Stock_Table.column("inv_id",width=100)
        self.Stock_Table.column("date",width=460)
        self.Stock_Table.column("amount",width=100)
        self.Stock_Table.column("is_paid",width=100)
        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.Stock_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def fetch_date(self, cust_id):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        cur.execute(f"select inv_id,date,amount,is_paid from sales_bill where customer_id = '{cust_id}'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                my_list = list(row)
                if(my_list[3] == 0):
                    my_list[3] = "UNPAID"
                else:
                    my_list[3] = "PAID"
                self.Stock_Table.insert('',END, values=my_list)
            con.commit()
        con.close()

    def clear(self):
        self.inv_id.set(0)
        self.date.set("")
        self.amount.set(0)
        self.is_paid.set(0)

    def get_cursor(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.inv_id.set(f'{row[0]}')
        self.date.set(row[1])
        self.amount.set(row[2])
        self.is_paid.set(row[3])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        statement=f"update sales_bill set is_paid=1 where inv_id='{self.inv_id.get()}'"
        cur.execute(statement)
        con.commit()
        self.fetch_date(self.cust_id.get())
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        cur.execute(f"delete from stocks where item_no='{self.item_no.get()}'")
        con.commit()
        con.close()
        self.fetch_date()
        self.clear()

    def displayCustomer(self, option):
        if self.Stock_Table.get_children():
            self.Stock_Table.delete(*self.Stock_Table.get_children())
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        cur.execute(f"select * from registered_customers where customer_name='{option}' limit 1")
        rows=cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                self.cust_id.set(row[0])
                self.fetch_date(row[0])

    def search_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main2")
        cur=con.cursor()
        if f'{self.search_by.get()}'=='Item No':
            statement=f"select * from stocks where item_no='{self.search_txt.get()}'"
        else:
            statement=f"select * from stocks where name='{self.search_txt.get()}'"
        cur.execute(statement)
        self.Stock_Table.delete(*self.Stock_Table.get_children())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
            con.commit()
        con.close()

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
