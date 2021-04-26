import mysql.connector
from mysql.connector import errorcode
from tkinter import messagebox


class ConnectDatabase:
    __host = None
    __user = None
    __password = None
    __database = None

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def _open(self):
        try:
            mydb = mysql.connector.connect(host=self.__host, user=self.__user,
                                           password=self.__password,
                                           database=self.__database)
            self.__connection = mydb
            self.__session = mydb.cursor()
            print("połaczyłem sie")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")

    def _close(self):
        self.__session.close()
        self.__connection.close()
        print("Zamknołem ")

    def insert_semi(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_pasive(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_opto(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_connectors(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_energy(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_pc(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_switches(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_wires(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_mechanics(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_laboratory(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid

    def insert_others(self, VName_S, VGroup_S, VSubCategory_S, VModel_S, VAssembly_S, VSize_S, VWhere_S, VQuantity_S ):
        AddSemi = (f"Insert Into semiconductors(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid
    '''
    def insert_make_order(self, user,when,stat):
        Order = (f"Insert Into historyorder(Name_S, Group_S, "
                   f"SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                   f"VALUES('{VName_S}','{VGroup_S}','{VSubCategory_S}','{VModel_S}',"
                   f"'{VAssembly_S}','{VSize_S}','{VWhere_S}','{VQuantity_S}')")
        self.__session.execute(AddSemi)
        self.__connection.commit()
        messagebox.showinfo("Add EQ", "Item was added sucesfully")
        return self.__session.lastrowid
    '''