

'''
class Icons:
    def __init__(self):
        from PIL import ImageTk, Image
        import tkinter as tk
        self.email_ic = ImageTk.PhotoImage(Image.open("ikoneczki\email.png"))
        self.emailL = tk.Label(self.root, image=self.email_ic, bg='red')
        self.emailL.photo = self.email_ic

        home_ic = ImageTk.PhotoImage(Image.open("ikoneczki\home.png"))
        homeL = tk.Label(self.root, image=home_ic)
        homeL.photo = home_ic

        add_ic = ImageTk.PhotoImage(Image.open("ikoneczki\plus.png"))
        addL = tk.Label(self.root, image=add_ic)
        addL.photo = add_ic

        delete_ic = ImageTk.PhotoImage(Image.open("ikoneczki\delete.png"))
        deleteL = tk.Label(self.root, image=delete_ic)
        deleteL.photo = delete_ic

        show_ic = ImageTk.PhotoImage(Image.open("ikoneczki\show.png"))
        showL = tk.Label(self.root, image=show_ic)
        showL.photo = show_ic

        chemistry_ic = ImageTk.PhotoImage(Image.open("ikoneczki\chemistry.png"))
        chemistryL = tk.Label(self.root, image=chemistry_ic)
        chemistryL.photo = chemistry_ic

        order_ic = ImageTk.PhotoImage(Image.open("ikoneczki\cart.png"))
        orderL = tk.Label(self.root, image=order_ic)
        orderL.photo = order_ic

        help_ic = ImageTk.PhotoImage(Image.open("ikoneczki\info.png"))
        helpL = tk.Label(self.root, image=help_ic)
        helpL.photo = help_ic
'''


class Icons:
    def __init__(self, master):
        from PIL import ImageTk, Image
        import tkinter as tk

        self.my_img = ImageTk.PhotoImage(Image.open("Ikona.png"))
        self.myLabel = tk.Label(master, image=self.my_img, bg='#004554')

        self.email_ic = ImageTk.PhotoImage(Image.open("ikoneczki\email.png"))
        self.email_L = tk.Label(master, image=self.email_ic, bg='red')
        self.email_L.photo = self.email_ic

        self.email_ic = ImageTk.PhotoImage(Image.open("ikoneczki\email.png"))
        self.email_L = tk.Label(master, image=self.email_ic, bg='red')
        self.email_L.photo = self.email_ic

        self.home_ic = ImageTk.PhotoImage(Image.open("ikoneczki\home.png"))
        self.homeL = tk.Label(master, image=self.home_ic)
        self.homeL.photo = self.home_ic

        self.add_ic = ImageTk.PhotoImage(Image.open("ikoneczki\plus.png"))
        self.addL = tk.Label(master, image=self.add_ic)
        self.addL.photo = self.add_ic

        self.delete_ic = ImageTk.PhotoImage(Image.open("ikoneczki\delete.png"))
        self.deleteL = tk.Label(master, image=self.delete_ic)
        self.deleteL.photo = self.delete_ic

        self.show_ic = ImageTk.PhotoImage(Image.open("ikoneczki\show.png"))
        self.showL = tk.Label(master, image=self.show_ic)
        self.showL.photo = self.show_ic

        self.chemistry_ic = ImageTk.PhotoImage(Image.open("ikoneczki\chemistry.png"))
        self.chemistryL = tk.Label(master, image=self.chemistry_ic)
        self.chemistryL.photo = self.chemistry_ic

        self.order_ic = ImageTk.PhotoImage(Image.open("ikoneczki\cart.png"))
        self.orderL = tk.Label(master, image=self.order_ic)
        self.orderL.photo = self.order_ic

        self.help_ic = ImageTk.PhotoImage(Image.open("ikoneczki\info.png"))
        self.helpL = tk.Label(master, image=self.help_ic)
        self.helpL.photo = self.help_ic

        self.ch_add_ic = ImageTk.PhotoImage(Image.open("ikoneczki\chem\ch_add.png"))
        self.ch_addL = tk.Label(master, image=self.ch_add_ic)
        self.ch_addL.photo = self.ch_add_ic









class TypeUsers:
    def __init__(self):
        self.TypeUsers = ["Default", "Admin"]

class UnderlineOn:
    def __init__(self,event):
        event.widget.config(underline=True)

class UnderLineOff:
    def __init__(self,event):
        event.widget.config(underline=False)

class Hover:
    def __init__(self ,event):
        event.widget.config(bg="red")


class Unhover:
    def __init__(self ,event):
        event.widget.config(bg='#0052cc')

class click:
    def __init__(self ,event):
        event.widget.config(bg="#52555E")


class zwolnienie:
    def __init__(self ,event):
        event.widget.config(bg='#3C3E45')


class GenerateNewPassword:
    def __init__(self):
        import random
        self.Letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*[]{}:;'"
        self.PasswordLength = 10
        self.Password = "".join(random.sample(self.Letters, self.PasswordLength))
        print(self.Password)

class PasswordMessage:
    def __init__(self,Password):
        self.New_Password = Password






'''
class MYSQL_Connection:
    import mysql.connector
    from mysql.connector import errorcode
    __instance = None

    __host = None
    __user = None
    __password = None
    __database = None

    __session = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Mysql, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    # Open connection with database
    def _open(self):
        try:
            cnx = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password,
                                          database=self.__database)
            self.__connection = cnx
            self.__session = cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print
                'Something is wrong with your user name or password'
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print
                'Database does not exists'
            else:
                print
                err

    def _close(self):
        self.__session.close()
        self.__connection.close()

    def insert(self, table, *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = kwargs.values()
            query += "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ") VALUES(" + ",".join(
                ["%s"] * len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"] * len(values)) + ")"
        self._open()
        self.__session.execute(query, values)
        self.__connection.commit()
        self._close()
        return self.__session.lastrowid

    def select(self, table, where=None, *args):
        result = None
        query = "SELECT "
        keys = args
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`" + key + "`"
            if i < l:
                query += ","
        query += " FROM %s" % table
        if where:
            query += " WHERE %" % where
        self._open()
        self.__session.execute(query)
        self.__connection.commit()
        for result in self.__session.stored_results():
            result = result.fetchall()
        self._close()
        return result

    def update(self, table, index, **kwargs):
        query = "UPDATE %s SET" % table
        keys = kwargs.keys()
        values = kwargs.values()
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`" + key + "`=%s"
            if i < l:
                query += ","
        query += " WHERE index=%d" % index
        self._open()
        self.__session.execute(query, values)
        self.__connection.commit()
        self._close()

    def delete(self, table, index):
        query = "DELETE FROM %s WHERE uuid=%d" % (table, index)
        self._open()
        self.__session.execute(query)
        self.__connection.commit()
        self._close()

    def call_store_procedure(self, name, *args):
        result_sp = None
        self._open()
        self.__session.callproc(name, args)
        self.__connection.commit()
        for result in self.__session.stored_results():
            result_sp = result.fetchall()
        self._close()
        return result_sp

'''




















