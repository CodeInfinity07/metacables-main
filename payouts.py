from tkinter import *
from tkinter import ttk
from random import randint
import pymysql
from ims_bill import Bill_App
from datetime import datetime
import customtkinter


class Payout:
    def __init__(self,root):
        global Manage_Frame
        self.root=root
        self.root.title("Meta Management System")
        self.root.geometry("1350x700+0+0")

        title=customtkinter.CTkLabel(self.root,text="Meta Management System",font=("Sawasdee",40,"bold"))
        title.pack(side=TOP,fill=X)

        #===========All Variables==============


        self.employee_id = IntVar()
        self.name = StringVar()
        self.amount=IntVar()
        self.employees = StringVar()
        self.date = StringVar()
        self.salary = IntVar()
        self.salary.set(0)


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
        fileMenu.add_command(label="Orders", command=self.openOrders)
        fileMenu.add_command(label="Raw Materials",command=self.RawMaterial)
        fileMenu.add_command(label="Employees",command=self.openEmployee)
        fileMenu.add_command(label="Exit", command=exit)

        #==========Menu ends here===================================

        #============Stock Entry Frame===============>

        Manage_Frame=Frame(self.root)
        Manage_Frame.place(x=20,y=100,width=450,height=480)

        m_title=customtkinter.CTkLabel(Manage_Frame, text="Manage Payouts", font=("Sawasdee",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_item_color=customtkinter.CTkLabel(Manage_Frame, text="Employee Name:", font=("Sawasdee",20,"bold"))
        lbl_item_color.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        lbl_item_name=customtkinter.CTkLabel(Manage_Frame, text="Payout Amount:", font=("Sawasdee",20,"bold"))
        lbl_item_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_item_name=customtkinter.CTkEntry(Manage_Frame,textvariable=self.amount,font=("Sawasdee",10,"bold"))
        txt_item_name.grid(row=2,column=1,pady=10,padx=8,sticky="w")

        g5_lbl=customtkinter.CTkLabel(Manage_Frame,text="Remaining Salary:",font=("Sawasdee",16,"bold")).grid(row=3,column=0,padx=20,pady=10,sticky="w")
        g5_txt=customtkinter.CTkLabel(Manage_Frame,textvariable=self.salary,font=("Sawasdee",16,"bold")).grid(row=3,column=1,padx=10,pady=10,stick="w")


        self.get_employees()

        
        

        #===========Button Frame=============
        btn_Frame=Frame(Manage_Frame)
        btn_Frame.place(x=8,y=400,width=430)

        Addbtn=customtkinter.CTkButton(btn_Frame,command=self.add_payout,text="Issue",width=150).grid(row=0,column=0,padx=8,pady=10)
        updatebtn=customtkinter.CTkButton(btn_Frame,command=self.clear_salary,text="Clear Salary",width=150).grid(row=0,column=1,padx=8,pady=10)
        # deletebtn=customtkinter.CTkButton(btn_Frame,command=self.delete_data,text="Delete",width=5).grid(row=0,column=2,padx=8,pady=10)
        # Clearbtn=customtkinter.CTkButton(btn_Frame,command=self.clear,text="Clear",width=5).grid(row=0,column=3,padx=8,pady=10)



        # #===========Detail Frame=====================

        Detail_Frame=Frame(self.root)
        Detail_Frame.place(x=500,y=100,width=830,height=580)

        # lbl_Search=customtkinter.CTkLabel(Detail_Frame,text="Search By",font=("Sawasdee",20,"bold"))
        # lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

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
        self.Stock_Table=ttk.Treeview(Table_Frame, column=("id","amount","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("id",text="ID") 
        self.Stock_Table.heading("amount",text="Amount")
        self.Stock_Table.heading("date",text="Date")

        self.Stock_Table['show']='headings'
        self.Stock_Table.column("id",width=50)
        self.Stock_Table.column("amount",width=100)
        self.Stock_Table.column("date",width=100)

        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.fetch_date()
        self.Stock_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_payout(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"insert into payouts (employee_id,amount,date) values ('{self.employee_id.get()}',{self.amount.get()},'{datetime.today().strftime('%Y-%m-%d')}')"
        cur.execute(statement)
        con.commit()
        self.fetch_employee_payout(self.employee_id.get())
        self.clear()
        con.close()

    def get_employees(self):
        global Manage_Frame, dict_options
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"select * from employee"
        cur.execute(statement)
        my_employees = cur.fetchall()
        con.commit()
        dict_options = dict()
        for row in my_employees:
            dict_options[row[0]] = row[1]
        self.employees.set("")
        self.color_option_field = customtkinter.CTkOptionMenu(Manage_Frame, values = list(dict_options.values()), command=self.fetch_payouts)
        self.color_option_field.grid(row=1,column=1)
        con.close()

    def fetch_payouts(self, value):
        global dict_options
        if self.Stock_Table.get_children():
            self.Stock_Table.delete(*self.Stock_Table.get_children())
        for i,j in dict_options.items():
            if j==value:
                position = int(i)
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"select id,amount,date from payouts where employee_id={position}"
        self.employee_id.set(position)
        cur.execute(statement)
        rows = cur.fetchall()
        cur.execute(f"select salary from employee where id = {position}")
        salary_rows=cur.fetchall()
        for r in salary_rows:
            self.salary.set(r[0])
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
                date_check = datetime.strptime(row[2], "%Y-%m-%d")
                if date_check.month == datetime.now().month:
                    fetch = self.salary.get() - row[1]
                self.salary.set(fetch)
            con.commit()
        con.close()

    def fetch_employee_payout(self, position):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"select id,amount,date from payouts where employee_id={position}"
        self.employee_id.set(position)
        cur.execute(statement)
        rows = cur.fetchall()
        cur.execute(f"select salary from employee where id = {position}")
        salary_rows=cur.fetchall()
        for r in salary_rows:
            self.salary.set(r[0])
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
                date_check = datetime.strptime(row[2], "%Y-%m-%d")
                if date_check.month == datetime.now().month:
                    fetch = self.salary.get() - row[1]
                self.salary.set(fetch)
            con.commit()
        con.close()

    def fetch_date(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        cur.execute("select id,amount,date from payouts")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.employee_id.set(0)
        self.name.set("")
        self.amount.set(0)

    def get_cursor(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.employee_id.set(row[0])
        self.name.set(row[1])


    def clear_salary(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        statement=f"insert into payouts (employee_id,amount,date) values ('{self.employee_id.get()}',{self.salary.get()},'{datetime.today().strftime('%Y-%m-%d')}')"
        cur.execute(statement)
        con.commit()
        self.fetch_employee_payout(self.employee_id.get())
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
        cur=con.cursor()
        cur.execute(f"delete from employee where id='{self.employee_id.get()}'")
        con.commit()
        con.close()
        self.fetch_date()
        self.clear()

    # def search_data(self):
    #     con=pymysql.connect(host="localhost",user="ryzon",password="zain0980",database="meta_main")
    #     cur=con.cursor()
    #     if f'{self.search_by.get()}'=='Item No':
    #         statement=f"select * from stocks where item_no='{self.search_txt.get()}'"
    #     else:
    #         statement=f"select * from stocks where name='{self.search_txt.get()}'"
    #     cur.execute(statement)
    #     self.Stock_Table.delete(*self.Stock_Table.get_children())
    #     rows=cur.fetchall()
    #     if len(rows)!=0:
    #         self.Stock_Table.delete(*self.Stock_Table.get_children())
    #         for row in rows:
    #             self.Stock_Table.insert('',END, values=row)
    #         con.commit()
    #     con.close()

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
    
