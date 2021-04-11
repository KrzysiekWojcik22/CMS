import mysql.connector
import tkinter as tk
from tkinter import messagebox
import yagmail
import datetime

def fAddComponent(self):
    MCategory = self.eCategory.get()
    if MCategory == "Semiconductors":
        Name = self.eName.get()
        Group = self.eGroup.get()
        SubCategory = self.eSubCategory.get()
        Model = self.eModel.get()
        Assembly = self.eAssembly.get()
        Size = self.eSize.get()
        Where = self.eWhere.get()
        Quantity = self.eQuintity.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="KrzysiekmySql12",
            database="sql-kurs"
        )
        mycursor = mydb.cursor()
        AddSemi = mycursor.execute(
            f"Insert Into semiconductors(Name_S, Group_S, SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
            f"VALUES('{Name}','{Group}','{SubCategory}','{Model}','{Assembly}','{Size}','{Where}','{Quantity}')")
        mycursor.execute(AddSemi)
        mydb.commit()
        mydb.close()
        tk.messagebox.showinfo("Info", "Item was added corectly")
        self.Add.destroy()

def fClearComponent(self):
    self.eName.delete(0, 'end')
    self.eCategory.delete(0, 'end')
    self.eGroup.delete(0, 'end')
    self.eAssembly.delete(0, 'end')
    self.eSize.delete(0, 'end')
    self.eCase.delete(0, 'end')
    self.eStorage.delete(0, 'end')
    self.eQuantity.delete(0, 'end')

def fUploadPDF(self):
    #input = filedialog.askopenfile(initialdir="/")
    print(input)

def fUploadLink(self):
    #input2 = filedialog.askopenfile(initialdir="/")
    print("input2")

def check(self):
        print(self.conf.get())

def sentorder(self):
    receiver = "krzysiu.w@spoko.pl"
    Message = self.eOrder.get(1.0, "end-1c")
    yag = yagmail.SMTP("krzysiekpython@gmail.com", password="krzysiek123")
    yag.send(
        to=receiver,
        subject="App_Order",
        contents=Message,
    )

    when = datetime.now()
    print(when)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="KrzysiekmySql12",
        database="sql-kurs"
    )
    mycursor = mydb.cursor()
    Add = mycursor.execute(
        f"Insert Into HistoryOrder(User_H,When_H,Status_H,Order_H) VALUES('123','{when}','New','{Message}')  ")
    mycursor.execute(Add)
    mydb.commit()
    mydb.close()
    tk.messagebox.showinfo("Info", "Request was sent corttly")

