import mysql.connector
from mysql.connector import errorcode
from tkinter import messagebox
import MySQLdb


class ConnectDatabase:
    __host = None
    __user = None
    __password = None
    __database = None

    def __init__(self, host, port, user, password, database):

        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database

    def _open(self):
        try:
            mydb = MySQLdb.connect(host=self.__host, port=self.__port, user=self.__user,
                                   password=self.__password,
                                   db=self.__database)
            self.__connection = mydb
            self.__session = mydb.cursor()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")

    def _close(self):
        self.__session.close()
        self.__connection.close()

    def insert_semi(self, Name_S, Group_S, Category_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S, Link_S, Picture_S):
        AddSemi = (f"Insert Into Semiconductors(Name_S, Group_S, "
                   f"Category_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S, Link_S, Picture_S) "
                   f"VALUES('{Name_S}','{Group_S}','{Category_S}','{Model_S}',"
                   f"'{Assembly_S}','{Size_S}','{Where_S}','{Quantity_S}','{Link_S}','{Picture_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")

    def insert_pasive(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_opto(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_connectors(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S,
                          VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_energy(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_pc(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_switches(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_wires(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_mechanics(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S,
                         VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_laboratory(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S,
                          VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_others(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_make_order(self, user_h, when_h, status_h, order_h, order_title, order_details):
        Order = (f"Insert Into historyorder(User_H, When_H, "
                 f"Status_H, Order_H, Order_Title, Order_Details) "
                 f"VALUES('{user_h}','{when_h}','{status_h}','{order_h}',"
                 f"'{order_title}','{order_details}')")

        self.__session.execute(Order)
        self.__connection.commit()
        messagebox.showinfo("Order", "Your order was sent")
        return self.__session.lastrowid


    def insert_create_new_account(self, User_name, User_email, User_supervisor, User_role, User_division, User_password):
        Create_new_account = (f"Insert Into Users(User_name, User_email, "
                              f"User_supervisor, User_role,User_division, User_password) "
                              f"VALUES('{User_name}','{User_email}','{User_supervisor}','{User_role}','{User_division}','{User_password}')")

        self.__session.execute(Create_new_account)
        self.__connection.commit()
        messagebox.showinfo("Order", "Your order was sent")

