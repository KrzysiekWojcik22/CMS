import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import smtplib, ssl
from tkinter import *
import random
import mysql.connector


class ShowComponents:
    def __init__(self):
        self.show = tk.Tk()
        self.show.title('DataBase Management System')
        screen_width = self.show.winfo_screenwidth()
        screen_height = self.show.winfo_screenheight()
        root_width = 1045
        root_height = 720
        center_x = int(screen_width / 2 - root_width / 2)
        center_y = int(screen_height / 2 - root_height / 2)
        self.show.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        self.show.resizable(False, False)
        self.show.attributes('-topmost')
        #photo1 = PhotoImage(file="ikona.png")
        #self.root.iconphoto(False, photo1)
        self.menubar = Menu(self.show)
        self.show.config(menu=self.menubar)
        file_menu = Menu(
            self.menubar,
            tearoff=0
        )
        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...')
        file_menu.add_command(label='Close')
        file_menu.add_separator()
        sub_menu = Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Keyboard Shortcuts')
        sub_menu.add_command(label='Color Themes')

        # add the File menu to the menubar
        file_menu.add_cascade(
            label="Preferences",
            menu=sub_menu
        )

        # add Exit menu item
        file_menu.add_separator()
        file_menu.add_command(
            label='Exit',

        )

        self.menubar.add_cascade(
            label="File",
            menu=file_menu,
            underline=0
        )
        # create the Help menu
        help_menu = Menu(
            self.menubar,
            tearoff=0
        )

        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')

        # add the Help menu to the menubar
        self.menubar.add_cascade(
            label="Help",
            menu=help_menu,
            underline=0
        )

        self.show.configure(bg='#EEEEEE')

        self.rootTitle = tk.Label(self.show, text='Component Database Management',
                                  bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.rootTitle.place(height=55, width=1045, x=0, y=0)

        self.ChoseYourCategory = tk.Label(self.show, text="Chose your Category:")
        self.ChoseYourCategory.place(height=40, width=140, x=15, y=60)

        self.TotalItems = tk.Label(self.show, text="Total Equipment in Database :")
        self.TotalItems.place(height=40, width=180, x=190, y=60)

        self.In = tk.Label(self.show, text="In")
        self.In.place(height=40, width=40, x=360, y=60)

        self.Categories = tk.Label(self.show, text="Categories:")
        self.Categories.place(height=40, width=80, x=400, y=60)

        self.showSep = ttk.Separator(self.show, orient='horizontal')
        self.showSep.place(width=510, x=15, y=105)

        self.Semiconductors = ttk.Checkbutton(self.show, text="Semiconductors" )
        self.Semiconductors.place(height=30, width=110, x=15, y=120)

        self.PassiveElements = ttk.Checkbutton(self.show, text="Passive Elements")
        self.PassiveElements.place(height=30, width=120, x=130, y=120)

        self.Optoelectronics =ttk.Checkbutton(self.show, text="Optoelectronics" )
        self.Optoelectronics.place(height=30, width=120, x=15, y=145)

        self.Connectors = ttk.Checkbutton(self.show, text="Connectors" )
        self.Connectors.place(height=30, width=120, x=130, y=145)

        self.EnergySources = ttk.Checkbutton(self.show, text="Energy Sources")
        self.EnergySources.place(height=30, width=120, x=15, y=170)

        self.PCAccessories = ttk.Checkbutton(self.show, text="PC Accessories")
        self.PCAccessories.place(height=30, width=120, x=130, y=170)

        self.Fuses = ttk.Checkbutton(self.show, text="Fuses" )
        self.Fuses.place(height=30, width=120, x=245, y=120)

        self.Switches = ttk.Checkbutton(self.show, text="Switches" )
        self.Switches.place(height=30, width=120, x=245, y=145)

        self.Fans = ttk.Checkbutton(self.show, text="Fans" )
        self.Fans.place(height=30, width=120, x=245, y=170)

        self.Wires = ttk.Checkbutton(self.show, text="Wires" )
        self.Wires.place(height=30, width=120, x=320, y=120)

        self.Mechanics = ttk.Checkbutton(self.show, text="Mechanics")
        self.Mechanics.place(height=30, width=120, x=320, y=145)

        self.Enclosures = ttk.Checkbutton(self.show, text="Enclosures" )
        self.Enclosures.place(height=30, width=120, x=320, y=170)

        self.Laboratory = ttk.Checkbutton(self.show, text="Laboratory")
        self.Laboratory.place(height=30, width=120, x=405, y=120)

        self.Others = ttk.Checkbutton(self.show, text="Others")
        self.Others.place(height=30, width=120, x=405, y=145)

        self.CheckSep = ttk.Separator(self.show, orient='horizontal')
        self.CheckSep.place(width=510, x=15, y=215)

        self.ItemSep = ttk.Separator(self.show, orient='vertical')
        self.ItemSep.place(height=515, x=530, y=60)

        self.ItemInfo = tk.Label(self.show, text='Item Info', fg='black', bg='#EEEEEE')
        self.ItemInfo.place(height=40, width=140, x=550, y=60)

        self.ItemID = tk.Label(self.show, text='ID', fg='black', bg='#EEEEEE')
        self.ItemID.place(height=40, width=40, x=650, y=60)

        self.Name = tk.Label(self.show, text='Here Item New', fg='black', bg='#EEEEEE')
        self.Name.place(height=40, width=140, x=700, y=60)

        self.ItemPicture = tk.Button(self.show, text='HerePictures', fg='blue', bg='white')
        self.ItemPicture.place(height=440, width=440, x=570, y=105)

        self.Link = tk.Button(self.show, text='Link', fg='white', bg='#0052cc',font = 14)
        self.Link.place(height=40, width=100, x=570, y=560)

        self.DownloadDS = tk.Button(self.show, text='DataSheet', fg='white', bg='#0052cc',font = 14)
        self.DownloadDS.place(height=40, width=100, x=570, y=615)

        self.Take = tk.Button(self.show, text='Take', fg='white', bg='#0052cc',font = 14)
        self.Take.place(height=40, width=100, x=685, y=560)

        self.Give = tk.Button(self.show, text='Give', fg='white', bg='#0052cc',font = 14)
        self.Give.place(height=40, width=100, x=685, y=615)

        self.Quantity = tk.Entry(self.show, width=50)
        self.Quantity.place(height=30, width=90, x=800, y=565)







def sayhi(self):
    print("Hi")



def show(self):
        top = tk.Tk()
        top.title('Add new equipment')
        top.geometry("300x500")



        self.lName = ttk.Label(top, text="Name:", )
        self.lName.place(height=40, width=80, x=10, y=10)

        self.lCategory = ttk.Label(top, text="Category:", )
        self.lCategory.place(height=40, width=80, x=10, y=60)

        self.lGroup = ttk.Label(top, text="Group:", )
        self.lGroup.place(height=40, width=80, x=10, y=110)

        self.lAssembly = ttk.Label(top, text="Assembly:", )
        self.lAssembly.place(height=40, width=80, x=10, y=160)

        self.lCase = ttk.Label(top, text="Case:", )
        self.lCase.place(height=40, width=80, x=10, y=210)

        self.lSize = ttk.Label(top, text="Size:", )
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lStorage = ttk.Label(top, text="Storage:", )
        self.lStorage.place(height=40, width=80, x=10, y=310)

        self.lQuantity = ttk.Label(top, text="Quantity:", )
        self.lQuantity.place(height=40, width=80, x=10, y=360)

        SizeComponents = ["0201", "0402", "0603", "0805", "1008", "1206", "1210"]
        Categories = ["Semiconductor", ]
        SposobMontazu = ["THT", "SMD"]
        # CasesTHT = ["DIP", "SDIP" , "TO" ]
        CasesSMD = ["SOJ", "SOIC", "PLCC", "QFP", "BGA"]
        grupa = ["1"]

        self.eName = ttk.Entry(top, width=50)
        self.eName.place(height=20, width=180, x=100, y=20)

        self.eCategory = ttk.Combobox(top, values=Categories)
        self.eCategory.place(height=20, width=180, x=100, y=70)

        self.eGroup = ttk.Combobox(top, values=grupa)
        self.eGroup.place(height=20, width=180, x=100, y=120)

        self.eAssembly = ttk.Combobox(top, values=SposobMontazu)
        self.eAssembly.place(height=20, width=180, x=100, y=170)

        self.eCase = ttk.Combobox(top, values=CasesSMD)
        self.eCase.place(height=20, width=180, x=100, y=220)

        self.eSize = ttk.Combobox(top, values=SizeComponents)
        self.eSize.place(height=20, width=180, x=100, y=270)

        self.eStorage = ttk.Combobox(top, values=CasesSMD)
        self.eStorage.place(height=20, width=180, x=100, y=320)

        self.eQuantity = ttk.Entry(top, width=50)
        self.eQuantity.place(height=20, width=180, x=100, y=370)




