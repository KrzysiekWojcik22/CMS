from tkinter import ttk, Menu
from AddEQ import AddComponent
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import *
import smtplib, ssl
from tkinter import filedialog
from PIL import ImageTk, Image
import Function as F
from categories import EquipmentCategoriesPassiveElements
import classes as cl

Color = cl.ColoursMainWindow()




class MainWindow:
    def __init__(self, master):
        master = tk.Toplevel()
        # master.overrideredirect(True)
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        root_width = 1045
        root_height = 720
        center_x = int(screen_width / 2 - root_width / 2)
        center_y = int(screen_height / 2 - root_height / 2)
        master.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        master.attributes('-topmost', True)
        master.configure(bg=Color.MainBackground)
        self.root = master
        PasekGora = tk.Canvas(self.root, bg='grey', height=725, width=1050)  # Budowa tła niebieskie
        PasekGora.tag_raise(1)
        PasekGora.place(x=-2, y=-1.5)
        PasekGora.create_rectangle(0, 0, 1045, 56, fill='#004554', outline='#004554')
        PasekGora.create_rectangle(0, 57, 1050, 120, fill='#3C3E45', outline='#3C3E45')
        PasekGora.create_rectangle(0, 121, 200, 724, fill='#3C3E45', outline='#3C3E45')

        ### Ikona
        my_img = ImageTk.PhotoImage(Image.open("Ikona.png"))
        myLabel = tk.Label(self.root, image=my_img, bg='#004554')
        myLabel.photo = my_img
        myLabel.place(x=10, y=2.5, height=48, width=48)

        ### icony

        email_ic = ImageTk.PhotoImage(Image.open("ikoneczki\email.png"))
        emailL = tk.Label(self.root, image=email_ic, bg='red')
        emailL.photo = email_ic

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

        ## Głowny interfejs
        self.rootTitle = tk.Label(self.root, text='Component Database Management',
                                  bg='#004554', fg='white', font=("Helvetica", 14))
        self.rootTitle.place(height=55, width=400, x=60, y=0)

        ### Separatory

        self.rootSep = ttk.Separator(self.root, orient='vertical')
        self.rootSep.place(width=150, x=15, y=130)

        self.rootSep2 = ttk.Separator(self.root, orient='vertical')
        self.rootSep2.place(width=150, x=15, y=650)

        ### glowne labelki

        self.ProjectL = tk.Label(self.root, font=("Arial", 40), bg='#3C3E45', fg='white', text="CMS")

        self.ProjectL.place(height=60, width=120, x=15, y=62.5)

        self.UsernameL = tk.Label(self.root, text='Krzysztof Wojcik',
                                  bg='#004554', fg='white', font=("Helvetica", 14))

        self.UsernameL.place(height=40, width=180, x=800, y=5)

        self.Designer = tk.Label(self.root, font=("Arial", 11), bg='#3C3E45', fg='white',
                                 text="Created by:\n Krzysztof Wójcik")
        self.Designer.place(height=60, width=140, x=15, y=655)

        ### Obramowanie i przyciski funkcyjne dla modern flat gui

        Close = tk.Label(self.root, font=("Arial", 11), anchor=tk.CENTER, bg='#0052cc', text="X", cursor="hand2")
        Close.tkraise(aboveThis=PasekGora)
        Close.place(x=990, y=0, width=55, height=55)

        ###Funkcje dla ramki

        Close.bind("<Enter>", cl.Hover)
        Close.bind("<Leave>", cl.Unhover)
        Close.bind("<Button-1>", )

        ### Tworzenie labelek z nazwami zmieniającymi kolor

        LHome = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Home", anchor="w",
                         cursor="hand2")
        LHome["compound"] = tk.LEFT
        LHome["image"] = home_ic
        LHome.tkraise(aboveThis=PasekGora)
        LHome.place(x=15, y=150, width=170, height=40)

        LAddEq = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Add Equipment", anchor="w",
                          cursor="hand2")
        LAddEq["compound"] = tk.LEFT
        LAddEq["image"] = add_ic
        LAddEq.tkraise(aboveThis=PasekGora)
        LAddEq.place(x=15, y=200, width=170, height=40)

        LDeleteEq = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Delete Equipment",
                             anchor="w", cursor="hand2")
        LDeleteEq["compound"] = tk.LEFT
        LDeleteEq["image"] = delete_ic
        LDeleteEq.tkraise(aboveThis=PasekGora)
        LDeleteEq.place(x=15, y=250, width=170, height=40)

        LShowEq = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Show Equipment",
                           anchor="w", cursor="hand2")
        LShowEq["compound"] = tk.LEFT
        LShowEq["image"] = show_ic
        LShowEq.tkraise(aboveThis=PasekGora)
        LShowEq.place(x=15, y=300, width=170, height=40)

        LChemistry = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Chemistry", anchor="w",
                              cursor="hand2")
        LChemistry["compound"] = tk.LEFT
        LChemistry["image"] = chemistry_ic
        LChemistry.tkraise(aboveThis=PasekGora)
        LChemistry.place(x=15, y=350, width=170, height=40)

        LMakeOrder = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Make Order", anchor="w",
                              cursor="hand2")
        LMakeOrder["compound"] = tk.LEFT
        LMakeOrder["image"] = order_ic
        LMakeOrder.tkraise(aboveThis=PasekGora)
        LMakeOrder.place(x=15, y=400, width=170, height=40)

        LHelp = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Help", anchor="w",
                         cursor="hand2")
        LHelp["compound"] = tk.LEFT
        LHelp["image"] = help_ic
        LHelp.tkraise(aboveThis=PasekGora)
        LHelp.place(x=15, y=450, width=170, height=40)

        ### Potrzebuje ramki dla dodawania, show, order, chemistry,

        colortłaFramesAdd = '#808080'

        Home = tk.Frame(self.root, bg='yellow')
        Home.place(x=300, y=200, height=500, width=500)
        AddEq = tk.Frame(self.root, bg='red')
        DeleteEq = tk.Frame(self.root, bg='black')
        ShowEq = tk.Frame(self.root, bg='blue')
        Chemistry = tk.Frame(self.root, bg='pink')

        ### Bindowanie klawiszy funkcyjnych

        def forgetFrames():
            Home.place_forget()
            AddEq.place_forget()
            DeleteEq.place_forget()
            ShowEq.place_forget()
            Chemistry.place_forget()

        def powrotkolorow(event):
            event.widget.config(fg='white')

        def zwolnienie(event):
            event.widget.config(bg='#3C3E45')

        def aktywny(event):
            event.widget.config(fg='white')

        def showHome(event):
            print("Work1")


            AddEquipmentFirst(master=self.root)
            forgetFrames()
            aktywny(event)
            Home.place(x=199, y=118, height=590, width=850)

        def showAddEq(event):
            print("Work2")
            forgetFrames()
            powrotkolorow(event)
            aktywny(event)

            AddEq.place(x=199, y=118, height=610, width=850)

        def showDeleteEq(event):
            print("Work3")
            forgetFrames()
            DeleteEq.place(x=199, y=118, height=610, width=850)

        def showShowEq(event):
            print("Work4")
            forgetFrames()
            ShowEq.place(x=199, y=118, height=610, width=850)

        def showChemistry(event):
            print("Work5")
            forgetFrames()
            Chemistry.place(x=199, y=118, height=610, width=850)

        def showMakeOrder(event):
            print("Work6")
            forgetFrames()
            MakeOrder(master=self.root)
            #  MakeOrder()

        def showHelp(event):
            print("Work7")

        LHome.bind("<Enter>", cl.click)
        LHome.bind("<Leave>", cl.zwolnienie)
        LHome.bind("<Button-1>", showHome)

        LAddEq.bind("<Enter>", cl.click)
        LAddEq.bind("<Leave>", zwolnienie)
        LAddEq.bind("<Button-1>", showAddEq)

        LDeleteEq.bind("<Enter>", cl.click)
        LDeleteEq.bind("<Leave>", zwolnienie)
        LDeleteEq.bind("<Button-1>", showDeleteEq)

        LShowEq.bind("<Enter>", cl.click)
        LShowEq.bind("<Leave>", zwolnienie)
        LShowEq.bind("<Button-1>", showShowEq)

        LChemistry.bind("<Enter>", cl.click)
        LChemistry.bind("<Leave>", zwolnienie)
        LChemistry.bind("<Button-1>", showChemistry)

        LMakeOrder.bind("<Enter>", cl.click)
        LMakeOrder.bind("<Leave>", zwolnienie)
        LMakeOrder.bind("<Button-1>", showMakeOrder)

        ### showMakeOrder

        LHelp.bind("<Enter>", cl.click)
        LHelp.bind("<Leave>", zwolnienie)
        LHelp.bind("<Button-1>", showHelp)


class MakeOrder:
    def __init__(self, master):
        self.Make_Order = tk.Frame(master, bg="blue")
        self.Make_Order.place(x=199, y=118, height=610, width=850)

        self.conf = tk.IntVar()
        self.Confirmation = ttk.Checkbutton(self.Make_Order, text="I accept the terms and conditions of orders ",
                                            style='green/black.TCheckbutton', variable=self.conf)
        self.Confirmation.place(height=40, width=400, x=15, y=520)

        self.BOrder = tk.Button(self.Make_Order, text='Make Order', font=14, bg='#0052cc',
                                fg='white', )
        self.BOrder.place(height=40, width=100, x=730, y=520)

        # Labelki

        self.Order_Title = tk.Label(self.Make_Order, text='Order Menagement',
                                    fg='white', font=("Helvetica", 20), anchor='w')
        self.Order_Title.place(height=55, width=630, x=15, y=0)

        self.OrderT = tk.Label(self.Make_Order,
                               text='Write an order, put your items with quantity and links that you want to order:',
                               anchor='w',
                               font=("Helvetica", 12))
        self.OrderT.place(height=55, width=520, x=15, y=60)

        self.SepOrd = ttk.Separator(self.Make_Order, orient='horizontal')
        self.SepOrd.place(width=820, x=12.5, y=500)

        self.lName_of_the_Order = tk.Label(self.Make_Order, text='Name of the order:', anchor='w',
                                           font=("Helvetica", 12))
        self.lName_of_the_Order.place(height=60, width=160, x=15, y=100)

        # Wejscia

        self.elName_of_the_Order = tk.Text(self.Make_Order)
        self.elName_of_the_Order.place(height=20, width=650, x=180, y=120)

        self.eOrder = tk.Text(self.Make_Order)
        self.eOrder.place(height=320, width=815, x=15, y=160)

        ttk.Style().configure('green/black.TCheckbutton', foreground='blue')
size = 0
count = 0
class AddEquipmentFirst:
    def __init__(self, master):
        self.Add_EQ = tk.Frame(master, bg="red")
        self.Add_EQ.place(x=199, y=118, height=610, width=850)

        ###colory
        colortło1AddEq = '#404040'
        colortło2AddEq = '#737373'
        colorPrzyciskowAddEq = '#404040'



        self.PadAdd1 = tk.PanedWindow(self.Add_EQ, bg=colortło1AddEq, handlepad=True)
        self.PadAdd1.place(height=700, width=140, x=0, y=0)

        self.PadAdd2 = tk.PanedWindow(self.Add_EQ, bg="blue")
        self.PadAdd2.place(height=640, width=720, x=140, y=0)

        # Tworzenie widgetów dla Padd1

        self.TitlePad1 = tk.Label(self.PadAdd1, text="Options")
        # self.TitlePad1.place(width=80 ,height=40 ,x=5 ,y=5 )

        self.Sep1Padd1 = ttk.Separator(self.PadAdd1, orient='horizontal')
        self.Sep1Padd1.place(width=130, x=5, y=40)

        self.AddComponent = tk.Label(self.PadAdd1, font=("Arial", 13), bg=colorPrzyciskowAddEq, fg='white',
                                     text="Choose a type")
        self.AddComponent.place(width=120, height=40, x=5, y=0)

        # Funkcje dla pad 1

        self.AddSemiconductors = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',
                                          anchor="w", text="Semiconductors", cursor="hand2")
        self.AddSemiconductors.place(width=110, height=40, x=15, y=50)

        self.AddPassiveElements = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',
                                           anchor="w", text="PassiveElements", cursor="hand2")
        self.AddPassiveElements.place(width=110, height=40, x=15, y=100)

        self.AddOptoelectronic = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',
                                          anchor="w", text="Optoelectronic", cursor="hand2")
        self.AddOptoelectronic.place(width=110, height=40, x=15, y=150)

        self.AddSemiconductors.bind("<Button-1>", lambda x: self.expand())

        self.AddPassiveElements.bind("<Button-1>",self.Add3)


    def Add2(self,x):
       AddEquipmentSecond(master=self.PadAdd2)

    def expand(self):
        global size, count
        if count < 850:
            size += 1
            print(size)
            self.AddSemiconductors.place(width=110, height=size, x=15, y=50)
            count += 1
            self.Add_EQ.after(100, self.expand)



    def Add3(self,x):
        AddEQuipmentThird(master=self.PadAdd2)

class AddSemi:
    def __init__(self):
        print("asddas")


class AddEquipmentSecond:
    def __init__(self, master):
        print("dwa")


        self.Add_Semi = tk.Frame(master, bg="red")
        self.Add_Semi.place(x=0, y=0, height=610, width=850)

        self.Semiconductors = tk.Frame(self.Add_Semi, bg="black")

        self.AddComponent = tk.Button(self.Add_Semi, text='Add', font=14, bg='#0052cc', fg='white',command = self.expand
                                      )
        self.AddComponent.place(height=40, width=80, x=0, y=0)

    def expand(self):
        global size, count
        if count < 850:
            size += 1
            print(size)
            self.AddComponent.place(height=40, width=size, x=0, y=0)
            count += 1
            self.Add_Semi.after(100, self.expand)

class AddEQuipmentThird:
    def __init__(self, master):
        print("dwa")
        self.Add_Semi = tk.Frame(master, bg="white")
        self.Add_Semi.place(x=0, y=0, height=610, width=850)

        self.Semiconductors = tk.Frame(self.Add_Semi, bg="black")

        self.AddComponent = tk.Button(self.Add_Semi, text='Add', font=14, bg='#0052cc', fg='white'
                                      )
        self.AddComponent.place(height=40, width=80, x=0, y=0)
