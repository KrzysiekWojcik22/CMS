import tkinter as tk
from _datetime import datetime
import yagmail
from tkinter import ttk
from tkinter import messagebox
import Colors as Col
import DataBaseOperation


Color = Col.ColoursMainWindow()


class MakeOrder:
    def __init__(self, master, *args):
        self.Make_Order = tk.Frame(master, bg=Color.WidgetBackground)
        self.Make_Order.place(x=0, y=0, height=620, width=850)

        self.conf = tk.BooleanVar()
        self.conf.set(False)
        ttk.Style().configure('green/black.TCheckbutton', foreground='blue',
                              background=Color.WidgetBackground, font=("Helvetica", 12))

        self.Confirmation = ttk.Checkbutton(self.Make_Order, text="I accept the terms and conditions of orders ",
                                            style='green/black.TCheckbutton', variable=self.conf)
        self.Confirmation.place(height=40, width=400, x=15, y=520)

        self.BOrder = tk.Button(self.Make_Order, text='Make Order', font=14, bg='#0052cc',
                                fg=Color.WidgetForegrounds, command=lambda: self.process_order())
        self.BOrder.place(height=40, width=100, x=730, y=520)

        # Label

        self.Order_Title = tk.Label(self.Make_Order, text='Order Management',
                                    fg=Color.WidgetForegrounds, bg=Color.WidgetBackground,
                                    font=("Helvetica", 20), anchor='w')
        self.Order_Title.place(height=55, width=630, x=15, y=0)

        self.OrderT = tk.Label(self.Make_Order,
                               text='Write an order, put your items with quantity and links that you want to order:',
                               anchor='w',
                               font=("Helvetica", 12), bg=Color.WidgetBackground)
        self.OrderT.place(height=55, width=520, x=15, y=60)

        self.SepOrd = ttk.Separator(self.Make_Order, orient='horizontal')
        self.SepOrd.place(width=820, x=12.5, y=500)

        self.lName_of_the_Order = tk.Label(self.Make_Order, text='Name of the order:', anchor='w',
                                           bg=Color.WidgetBackground,
                                           font=("Helvetica", 12))
        self.lName_of_the_Order.place(height=60, width=160, x=15, y=100)

        # Enters

        self.elName_of_the_Order = tk.Text(self.Make_Order)
        self.elName_of_the_Order.place(height=20, width=650, x=180, y=120)

        self.eOrder = tk.Text(self.Make_Order)
        self.eOrder.place(height=320, width=815, x=15, y=160)

        self.when = datetime.now()

    def process_order(self):
        self.check_order()
        self.send_email()
        self.order_to_database()
        tk.messagebox.showinfo("Info", "Order was sent correctly")

    def check_order(self):
        check = self.conf.get()
        if check:
            self.Tutul = self.elName_of_the_Order.get(1.0, "end-1c")
            self.Zawartosc = self.eOrder.get(1.0, "end-1c")
            self.elName_of_the_Order.delete('1.0', 'end')
            self.eOrder.delete('1.0', 'end')
        elif not check:
            tk.messagebox.showerror("Error", "You must accept the terms of the orders")

    def send_email(self):
        receiver = "krzysiu.w@spoko.pl"
        Message = self.Zawartosc
        yag = yagmail.SMTP("krzysiekpython@gmail.com", password="krzysiek123")
        yag.send(
            to=receiver,
            subject="App_Order",
            contents=Message,
        )

    def order_to_database(self):
        User = 'Krzysiek'
        Details = "Tak" #self.eOrder.get(1.0, tk.END)
        Title = "Tak" #self.elName_of_the_Order.get(1.0, tk.END)
        DataBaseOperation.ConnectDatabase.__init__(self, host='localhost', user='root', password='KrzysiekmySql12', database="sql-kurs")
        DataBaseOperation.ConnectDatabase._open(self)
        DataBaseOperation.ConnectDatabase.insert_make_order(self, user_h=User, when_h=self.when, status_h='', order_h='', order_title=self.Tutul, order_details=self.Zawartosc)
        DataBaseOperation.ConnectDatabase._close(self)
