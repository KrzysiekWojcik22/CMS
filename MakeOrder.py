import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import smtplib, ssl
from tkinter import *
import random
import mysql.connector
import yagmail
from _datetime import datetime



class CMakeOrder:
    def __init__(self):

        self.Order = tk.Tk()  # tworzenie okna głównego
        self.Order.title('Order Menagement')  # ustawienie tytułu okna głównego
        screen_width = self.Order.winfo_screenwidth()
        screen_height = self.Order.winfo_screenheight()
        Login_width = 630
        Login_height = 400
        center_x = int(screen_width / 2 - Login_width / 2)
        center_y = int(screen_height / 2 - Login_height / 2)
        self.Order.geometry(f'{Login_width}x{Login_height}+{center_x}+{center_y}')
        self.Order.resizable(False, False)
        self.Order.attributes('-topmost')
        #photo = PhotoImage(file="komparator1.png")
        #self.Order.iconphoto(False, photo)
        self.Order.configure(bg='white')

        self.OrderTitle = tk.Label(self.Order, text='Order Menagement',
                                   bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.OrderTitle.place(height=55, width=630, x=0, y=0)

        self.OrderT = tk.Label(self.Order, text='Put your links with quantity of Items that you want to order',
                               bg='white', font=("Helvetica", 10))
        self.OrderT.place(height=55, width=480, x=15, y=60)

        self.eOrder = tk.Text(self.Order)
        self.eOrder.place(height=220,  width=600, x=15, y=100)

        self.SepOrd = ttk.Separator(self.Order, orient='horizontal')
        self.SepOrd.place(width=600, x=15, y=329)

        ttk.Style().configure('green/black.TCheckbutton', foreground='blue', background='white')

        self.conf = tk.IntVar()

        self.Confirmation = ttk.Checkbutton(self.Order, text="I accept the terms and conditions of orders ",
                                            style='green/black.TCheckbutton', variable=self.conf, command=lambda: CMakeOrder.check(self))
        self.Confirmation.place(height=40, width=400, x=15, y=345)

        self.BOrder = tk.Button(self.Order, text='Make Order', font=14, bg='#0052cc',
                                fg='white', command=lambda: CMakeOrder.sentorder(self))
        self.BOrder.place(height=40, width=100, x=515, y=345)

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
        Add = mycursor.execute(f"Insert Into HistoryOrder(User_H,When_H,Status_H,Order_H) VALUES('123','{when}','New','{Message}')  ")
        mycursor.execute(Add)
        mydb.commit()
        mydb.close()
        tk.messagebox.showinfo("Info", "Request was sent corttly")

