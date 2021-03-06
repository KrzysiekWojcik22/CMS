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

    def insert_semi(self, Name_S, Group_S, Category_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S, Link_S,
                    Picture_S, Pdf_S):
        add_semi = (f"Insert Into Semiconductors(Name_S, Group_S, "
                    f"Category_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S, Link_S, Picture_S, Pdf_S) "
                    f"VALUES('{Name_S}','{Group_S}','{Category_S}','{Model_S}',"
                    f"'{Assembly_S}','{Size_S}','{Where_S}','{Quantity_S}','{Link_S}','{Picture_S}','{Pdf_S}')")
        self.__session.execute(add_semi)
        self.__connection.commit()

    def insert_passive(self, name, group, category, model, assembly, size, value, tolerance, wats, where, quantity,
                       link, picture):
        add_passive = (f"Insert Into CMS.Passive_elements(Name_P, Group_P,Category_P, Model_P, Assembly_P, Size_P, "
                       f"Value_P, Tolerance_P, Wats_P, Where_P, Quantity_P) VALUES('{name}','{group}','{category}',"
                       f"'{model}','{assembly}','{size}','{value}','{tolerance}','{wats}','{where}','{quantity}',"
                       f"'{link}', {picture})")

        self.__session.execute(add_passive)
        self.__connection.commit()

    def insert_opto(self, name, group, category, model, assembly, size, colour, wats, where, quantity, link):
        add_opto = (f"Insert Into CMS.Optoelectronics(Name_Op, Group_Op,Category_Op, Model_Op, Assembly_Op, Size_Op, "
                    f"Colour_Op, Wats_Op, Where_Op, Quantity_Op, Link_Op) "
                    f"VALUES('{name}','{group}','{category}','{model}', '{assembly}', '{size}','{colour}','{wats}',"
                    f"'{where}','{quantity}','{link}')")

        self.__session.execute(add_opto)
        self.__connection.commit()

    def insert_connectors(self, name, group, category, model, assembly, brand, where, quantity, link):
        add_connectors = (f"Insert Into CMS.Connectors(Name_C, Group_C,Category_C, Model_C, Assembly_C, Brand_C, "
                          f"Where_C, Quantity_C, Link_C) VALUES('{name}','{group}','{category}','{model}','{assembly}',"
                          f"'{brand}','{where}','{quantity}','{link}')")

        self.__session.execute(add_connectors)
        self.__connection.commit()
        return self.__session.lastrowid

    def insert_energy(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added successfully")
        return self.__session.lastrowid

    def insert_pc(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added successfully")
        return self.__session.lastrowid

    def insert_switches(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added successfully")
        return self.__session.lastrowid

    def insert_wires(self, name, group, category, colour, length, number_core, where, quantity, link):
        add_wires = (f"Insert Into CMS.Wires(Name_W, Group_W, Category_W, Colour_W, Length_W, Number_Core_W, Where_W, "
                     f"Quantity_W, Link_W) "
                     f"VALUES('{name}','{group}','{category}','{colour}','{length}','{number_core}','{where}',"
                     f"'{quantity}','{link}')")

        self.__session.execute(add_wires)
        self.__connection.commit()
        return self.__session.lastrowid

    def insert_mechanics(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S,
                         VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added successfully")
        return self.__session.lastrowid

    def insert_laboratory(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S,
                          VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added successfully")
        return self.__session.lastrowid

    def insert_others(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added successfully")
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

    def insert_create_new_account(self, User_name, User_email, User_supervisor, User_role, User_division,
                                  User_password):

        create_new_account = (f"Insert Into Users(User_name, User_email, "
                              f"User_supervisor, User_role,User_division, User_password) "
                              f"VALUES('{User_name}','{User_email}','{User_supervisor}','{User_role}','{User_division}','{User_password}')")

        self.__session.execute(create_new_account)
        self.__connection.commit()

    def show_users(self):
        showuser = ("Select * from CMS.Users")
        self.__session.execute(showuser)
        allrec = self.__session.fetchall()
        for row in allrec:
            print(row, '\n')
        self.__connection.commit()

    def insert_new_container(self, name, cas_number, size, unit, quantity, location, supplier, expiry_date, product_code
                             , link, photo, pdf):
        container = (f"Insert Into CMS.Containers(Name, CAS_Number,Size, Unit, Quantity, Location, Supplier, "
                     f"Expiry_Date, Product_Code, Link, Photo, Pdf) "
                     f"VALUES('{name}','{cas_number}','{size}','{unit}','{quantity}','{location}','{supplier}',"
                     f"'{expiry_date}','{product_code}','{link}','{photo}','{pdf}')")

        self.__session.execute(container)
        self.__connection.commit()
        return self.__session.lastrowid