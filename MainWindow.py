from tkinter import ttk, Menu
from AddEQ import AddComponent
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import *
import smtplib, ssl
from ShowEQ import ShowComponents
from tkinter import filedialog
from MakeOrder import CMakeOrder
from PIL import ImageTk , Image

class MainWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.overrideredirect(True)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        root_width = 1045
        root_height = 720
        center_x = int(screen_width / 2 - root_width / 2)
        center_y = int(screen_height / 2 - root_height / 2)
        self.root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        #self.root.resizable(False, False) # i tak nie działa xd
        self.root.attributes('-topmost', True)
        self.root.configure(bg='white')


        # self.root.bind("<Button-1>", self.startMove)
        # self.root.bind("<ButtonRelease-1>", self.stopMove)  # bindowanie klawiszy dla przesówania okienka
        # self.root.bind("<B1-Motion>", self.moving)

        ### Pasek Górny

        PasekGora = tk.Canvas(self.root, bg='grey', height=725, width=1050)  # Budowa tła niebieskie
        PasekGora.tag_raise(1)
        PasekGora.place(x=-2, y=-1.5)
        PasekGora.create_rectangle(0, 0, 1045, 56, fill='#004554', outline='#004554')
        PasekGora.create_rectangle(0, 57, 1050, 120, fill='blue', outline='blue')
        PasekGora.create_rectangle(0, 121, 200, 720, fill='blue', outline='blue')


        ### Ikona
        my_img = ImageTk.PhotoImage(Image.open("Ikona.png"))

        myLabel= tk.Label(self.root,image=my_img,bg='#004554')
        myLabel.photo = my_img
        #myLabel.config(bg="")
        myLabel.place(x=10,y=2.5, height=48, width=48)


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


        self.ProjectL = tk.Label(self.root, text='CMS',
                                  bg='#004554', fg='white', font=("Helvetica", 14))

        self.ProjectL.place(height=40, width=100, x=15, y=80)

        self.UsernameL = tk.Label(self.root, text='Krzysztof Wojcik',
                                  bg='#004554', fg='white', font=("Helvetica", 14))

        self.UsernameL.place(height=40,width=180, x=800, y=5)







        self.Designer = ttk.Label(self.root, text="Created by KW")
        self.Designer.place(height=80, width=100, x=15, y=665)



        self.AddComp = tk.Button(self.root, text='Add new EQ ', fg='white', bg='#0052cc',
                                 command=lambda: AddComponent())
        # self.AddComp.place(height=40, width=90, x=10, y=75)










        ### Obramowanie i przyciski funkcyjne dla modern flat gui



        Close = tk.Label(self.root, font=("Arial", 11), anchor=tk.CENTER, bg='#0052cc', text="X", cursor="hand2")
        Close.tkraise(aboveThis=PasekGora)
        Close.place(x=990, y=0, width=55, height=55)

        ###Funkcje dla ramki

        def hover(event):
            event.widget.config(bg="red")

        def unhover(event):
            event.widget.config(bg='#0052cc')

        Close.bind("<Enter>", hover)
        Close.bind("<Leave>", unhover)
        Close.bind("<Button-1>", self.exitProgram)

        PasekGora.bind("<Button-1>", self.startMove)
        PasekGora.bind("<ButtonRelease-1>", self.stopMove)
        PasekGora.bind("<B1-Motion>", self.moving)
        PasekGora.bind("<Double-Button-1>", self.minimize)
        PasekGora.bind("<Map>", self.frame_mapped)


        ### Tworzenie labelek z nazwami zmieniającymi kolor

        LHome = tk.Label(self.root, font=("Arial", 11), bg='white', text="Home", cursor="hand2")
        LHome.tkraise(aboveThis=PasekGora)
        LHome.place(x=15, y=150, width=120, height=40)

        LAddEq = tk.Label(self.root, font=("Arial", 11), bg='white', text="Add Equipment", cursor="hand2")
        LAddEq.tkraise(aboveThis=PasekGora)
        LAddEq.place(x=15, y=200, width=120, height=40)

        LDeleteEq = tk.Label(self.root, font=("Arial", 11), bg='white', text="Delete Equipment", cursor="hand2")
        LDeleteEq.tkraise(aboveThis=PasekGora)
        LDeleteEq.place(x=15, y=250, width=120, height=40)

        LShowEq = tk.Label(self.root, font=("Arial", 11), bg='white', text="Show Equipment", cursor="hand2")
        LShowEq.tkraise(aboveThis=PasekGora)
        LShowEq.place(x=15, y=300, width=120, height=40)

        LChemistry = tk.Label(self.root, font=("Arial", 11), bg='white', text="Chemistry", cursor="hand2")
        LChemistry.tkraise(aboveThis=PasekGora)
        LChemistry.place(x=15, y=350, width=120, height=40)

        LMakeOrder = tk.Label(self.root, font=("Arial", 11), bg='white', text="Make Order", cursor="hand2")
        LMakeOrder.tkraise(aboveThis=PasekGora)
        LMakeOrder.place(x=15, y=400, width=120, height=40)

        LHelp = tk.Label(self.root, font=("Arial", 11), bg='white', text="Help", cursor="hand2")
        LHelp.tkraise(aboveThis=PasekGora)
        LHelp.place(x=15, y=450, width=120, height=40)

        ### Potrzebuje ramki dla dodawania, show, order, chemistry,

        Home = tk.Frame(self.root, bg='yellow')
        Home.place(x=300, y=200, height=500, width=500)

        AddEq = tk.Frame(self.root, bg='red')
        DeleteEq = tk.Frame(self.root, bg='black')
        ShowEq = tk.Frame(self.root, bg='blue')
        Chemistry = tk.Frame(self.root, bg='pink')
        MakeOrder = tk.Frame(self.root, bg='green')

        ### Bindowanie klawiszy funkcyjnych

        def forgetFrames():
            Home.place_forget()
            AddEq.place_forget()
            DeleteEq.place_forget()
            ShowEq.place_forget()
            Chemistry.place_forget()
            MakeOrder.place_forget()

        def powrotkolorow(event):
            event.widget.config(fg='black')

        def klik(event):
            event.widget.config(bg="red")

        def zwolnienie(event):
            event.widget.config(bg='#0052cc')

        def aktywny(event):
            event.widget.config(fg='blue')

        def showHome(event):
            print("Work1")
            forgetFrames()
            aktywny(event)
            Home.place(x=300, y=200, height=500, width=500)

        def showAddEq(event):
            print("Work2")
            forgetFrames()
            powrotkolorow(event)
            aktywny(event)

            AddEq.place(x=199, y=118, height=590, width=850)

        def showDeleteEq(event):
            print("Work3")
            forgetFrames()
            DeleteEq.place(x=300, y=200, height=500, width=500)

        def showShowEq(event):
            print("Work4")
            forgetFrames()
            ShowEq.place(x=300, y=200, height=500, width=500)

        def showChemistry(event):
            print("Work5")
            forgetFrames()
            Chemistry.place(x=300, y=200, height=500, width=500)

        def showMakeOrder(event):
            print("Work6")
            forgetFrames()
            MakeOrder.place(x=300, y=200, height=500, width=500)

        def showHelp(event):
            print("Work7")

        LHome.bind("<Enter>", klik)
        LHome.bind("<Leave>", zwolnienie)
        LHome.bind("<Button-1>", showHome)

        LAddEq.bind("<Enter>", klik)
        LAddEq.bind("<Leave>", zwolnienie)
        LAddEq.bind("<Button-1>", showAddEq)

        LDeleteEq.bind("<Enter>", klik)
        LDeleteEq.bind("<Leave>", zwolnienie)
        LDeleteEq.bind("<Button-1>", showDeleteEq)

        LShowEq.bind("<Enter>", klik)
        LShowEq.bind("<Leave>", zwolnienie)
        LShowEq.bind("<Button-1>", showShowEq)

        LChemistry.bind("<Enter>", klik)
        LChemistry.bind("<Leave>", zwolnienie)
        LChemistry.bind("<Button-1>", showChemistry)

        LMakeOrder.bind("<Enter>", klik)
        LMakeOrder.bind("<Leave>", zwolnienie)
        LMakeOrder.bind("<Button-1>", showMakeOrder)

        LHelp.bind("<Enter>", klik)
        LHelp.bind("<Leave>", zwolnienie)
        LHelp.bind("<Button-1>", showHelp)

        ### Tworzenie widgetów w ramkach

        ### Home

        ### Add

        #create panded window for adding eq

        self.PadAdd1 = tk.PanedWindow(AddEq,bg="green", handlepad=True)
        self.PadAdd1.place(height=590, width=180, x=0, y=0)

        self.PadAdd2 = tk.PanedWindow(AddEq, bg = "yellow")
        self.PadAdd2.place(height=590, width=400, x=185,y=0)
        # tworze widzety dla paddAdd




        # Tworzenie widgetów dla Padd1

        self.TitlePad1 = tk.Label(self.PadAdd1, text="Options" )
        self.TitlePad1.place(width=80 ,height=40 ,x=5 ,y=5 )

        self.Sep1Padd1 = ttk.Separator(self.PadAdd1, orient='vertical')
        self.Sep1Padd1.place(width=40, x= 5, y = 50)







        self.AddComponent = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Add Equipment", cursor="hand2")
        self.AddComponent.place(width=80, height=40, x = 5, y = 10 )

        # Funkcje dla pad 1

        self.AddSemiconductors = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Semiconductors", cursor="hand2")
        self.AddSemiconductors.place(width=80, height=40, x = 5, y = 50 )

        self.AddPassiveElements = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="PassiveElements", cursor="hand2")
        self.AddPassiveElements.place(width=80, height=40, x = 5, y = 100 )

        self.AddOptoelectronic = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Optoelectronic", cursor="hand2")
        self.AddOptoelectronic.place(width=80, height=40, x = 5, y = 150 )

        self.AddConnectors = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Connectors", cursor="hand2")
        self.AddConnectors.place(width=80, height=40, x = 5, y = 60 )

        self.AddEnergySources = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="EnergySources", cursor="hand2")
        self.AddEnergySources.place(width=80, height=40, x = 5, y = 200 )

        self.AddPCAccesories = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="PCAccesories", cursor="hand2")
        self.AddPCAccesories.place(width=80, height=40, x = 5, y = 250 )

        self.AddSwitches = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Switches", cursor="hand2")
        self.AddSwitches.place(width=80, height=40, x = 5, y = 300 )

        self.AddWires = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Wires", cursor="hand2")
        self.AddWires.place(width=80, height=40, x = 5, y = 350 )

        self.AddMechanics = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Mechanics", cursor="hand2")
        self.AddMechanics.place(width=80, height=40, x = 5, y = 60 )

        self.AddLaboratory = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Laboratory", cursor="hand2")
        self.AddLaboratory.place(width=80, height=40, x = 5, y = 400 )

        self.AddOthers = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Others", cursor="hand2")
        self.AddOthers.place(width=80, height=40, x = 5, y = 450 )


        ### bindowanie klawiszy

        self.AddSemiconductors.bind("<Enter>", klik)
        self.AddSemiconductors.bind("<Leave>", zwolnienie)
        self.AddSemiconductors.bind("<Button-1>", showHelp)

        self.AddPassiveElements.bind("<Enter>", klik)
        self.AddPassiveElements.bind("<Leave>", zwolnienie)
        self.AddPassiveElements.bind("<Button-1>", showHelp)

        self.AddOptoelectronic.bind("<Enter>", klik)
        self.AddOptoelectronic.bind("<Leave>", zwolnienie)
        self.AddOptoelectronic.bind("<Button-1>", showHelp)

        self.AddConnectors.bind("<Enter>", klik)
        self.AddConnectors.bind("<Leave>", zwolnienie)
        self.AddConnectors.bind("<Button-1>", showHelp)

        self.AddEnergySources.bind("<Enter>", klik)
        self.AddEnergySources.bind("<Leave>", zwolnienie)
        self.AddEnergySources.bind("<Button-1>", showHelp)

        self.AddPCAccesories.bind("<Enter>", klik)
        self.AddPCAccesories.bind("<Leave>", zwolnienie)
        self.AddPCAccesories.bind("<Button-1>", showHelp)

        self.AddSwitches.bind("<Enter>", klik)
        self.AddSwitches.bind("<Leave>", zwolnienie)
        self.AddSwitches.bind("<Button-1>", showHelp)

        self.AddWires.bind("<Enter>", klik)
        self.AddWires.bind("<Leave>", zwolnienie)
        self.AddWires.bind("<Button-1>", showHelp)

        self.AddMechanics.bind("<Enter>", klik)
        self.AddMechanics.bind("<Leave>", zwolnienie)
        self.AddMechanics.bind("<Button-1>", showHelp)

        self.AddLaboratory.bind("<Enter>", klik)
        self.AddLaboratory.bind("<Leave>", zwolnienie)
        self.AddLaboratory.bind("<Button-1>", showHelp)

        self.AddOthers.bind("<Enter>", klik)
        self.AddOthers.bind("<Leave>", zwolnienie)
        self.AddOthers.bind("<Button-1>", showHelp)


        self.Help1 = tk.Label(self.PadAdd1, font=("Arial", 11), bg='white', text="Add Equipment", cursor="hand2")






        Categories = ["Semiconductors", "Passive Elements", "Optoelectronic", "Connectors",
                      "Energy Sources", "PC Accessories", "Switches", "Fans", "Wires",
                      "Mechanics", "Laboratory", "Others"]








        # Tworzenie widgetow dla padd2



        self.Semiconductors = tk.Frame(AddEq, bg="white")
        # self.Semiconductors.place(height=40, width=80, x=15, y=445)

        self.PassiveElements = tk.Frame(AddEq, bg="white")
        # self.PassiveElements.place(height=40, width=80, x=15, y=445)

        self.OptoElectronics = tk.Frame(AddEq, bg="white")
        # self.PassiveElements.place(height=40, width=80, x=15, y=445)

        self.Connectors = tk.Frame(AddEq, bg="white")
        # self.Connectors.place(height=40, width=80, x=15, y=445)

        self.EnergySources = tk.Frame(AddEq, bg="white")
        # self.EnergySources.place(height=40, width=80, x=15, y=445)

        self.PCAccessories = tk.Frame(AddEq, bg="white")
        # self.PCAccessories.place(height=40, width=80, x=15, y=445)

        self.Wires = tk.Frame(AddEq, bg="white")
        # self.Wires.place(height=40, width=80, x=15, y=445)

        self.Mechanics = tk.Frame(AddEq, bg="white")
        # self.Mechanics.place(height=40, width=80, x=15, y=445)

        self.Laboratory = tk.Frame(AddEq, bg="white")
        # self.Laboratory.place(height=40, width=80, x=15, y=445)

        self.Others = tk.Frame(AddEq, bg="white")
        # self.Others.place(height=40, width=80, x=15, y=445)

        Categories = ["Semiconductors", "Passive Elements", "Optoelectronic", "Connectors",
                      "Energy Sources", "PC Accessories", "Switches", "Fans", "Wires",
                      "Mechanics", "Laboratory", "Others"]

        ### Przyciski
        '''
        self.AddComponent = tk.Button(self.PadAdd1, text='Add', font=14, bg='#0052cc', fg='white', )
        self.AddComponent.place(height=40, width=80, x=15, y=445)

        self.ClearTables = tk.Button(self.PadAdd1, text='Clear', font=14, bg='#0052cc', fg='white')

        self.ClearTables.place(height=40, width=80, x=110, y=445)

        self.UploadPDF = tk.Button(AddEq, text='Add', font=14, bg='#0052cc', fg='white', )
        self.UploadPDF.place(height=40, width=80, x=15, y=445)

        self.UploadLink = tk.Button(AddEq, text='Add', font=14, bg='#0052cc', fg='white', )
        self.UploadLink.place(height=40, width=80, x=15, y=445)
        '''
        ###


        ### Delete

        ### Show

        ### Chemistry

        ### Make Order

        ### Help

        ### Tworzenie ramek na przyciski  funkcyjne

        ### Funkcje do pokazywanie ramek

        # self.menubar = Menu(self.root)
        # self.root.config(menu=self.menubar)
        '''
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
        '''


        '''
        self.AddComp = tk.Button(self.root, text='Show EQ', fg='white', bg='#0052cc', command=lambda: ShowComponents() )
        self.AddComp.place(height=40, width=90, x=10, y=125)

        self.AddComp = tk.Button(self.root, text='Delete EQ', fg='white', bg='#0052cc', command=lambda: AddComponent.add(self))
        self.AddComp.place(height=40, width=90, x=10, y=175)

        self.AddComp = tk.Button(self.root, text='Make Order', fg='white', bg='#0052cc', command=lambda: CMakeOrder())
        self.AddComp.place(height=40, width=90, x=10, y=225)

        self.AddComp = tk.Button(self.root, text='Help', fg='white', bg='#0052cc',  command=lambda: AddComponent.add(self))
        self.AddComp.place(height=40, width=90, x=10, y=275)


        self.AddComp = ttk.Button(self.root, text="<", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=700, y=485)

        self.AddComp = ttk.Button(self.root, text=">", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=880, y=485)

        self.AddComp = ttk.Button(self.root, text="INFO", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=790, y=485)

        self.Zastepcze = ttk.Button(self.root, text="Tutaj Obrazek", command=self.say_hi)
        self.Zastepcze.place(height=400, width=400, x=630, y=75)

        self.AddComp = ttk.Button(self.root, text="Export1", command=self.export1)
        self.AddComp.place(height=40, width=80, x=15, y=500)

        self.AddComp = ttk.Button(self.root, text="Export2", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=110, y=500)

        self.AddComp = ttk.Button(self.root, text="Export3", command=self.say_hi)
        self.AddComp.place(height=40, width=80, x=205, y=500)

        self.Kategoria = ttk.Entry(self.root, width=50)
        self.Kategoria.place(height=25, width=100, x=210, y=500)

        self.Typ = ttk.Entry(self.root, width=50)
        self.Typ.place(height=25, width=100, x=210, y=1000)

        self.Ilosc = ttk.Entry(self.root, width=50)
        self.Ilosc.place(height=25, width=100, x=210, y=1500)

        self.Where = ttk.Entry(self.root, width=50)
        self.Where.place(height=25, width=100, x=210, y=2000)

        self.Informacje = ttk.Label(self.root, text="Information:")
        self.Informacje.place(height=40, width=80, x=350, y=100)

        self.Informacje = ttk.Label(self.root, text="Fast Find:", )
        self.Informacje.place(height=40, width=80, x=120, y=100)

        self.Informacje = ttk.Label(self.root, text="Category:", )
        self.Informacje.place(height=40, width=80, x=120, y=400)

        self.Informacje = ttk.Label(self.root, text="Type:", )
        self.Informacje.place(height=40, width=80, x=120, y=90)

        self.Informacje = ttk.Label(self.root, text="Where:", )
        self.Informacje.place(height=40, width=80, x=120, y=140)

        self.Informacje = tk.Label(self.root, text="Quantity:", )
        self.Informacje.place(height=40, width=80, x=120, y=190)

        self.Informacje = ttk.Label(self.root, text="text")
        self.Informacje.place(height=40, width=80, x=500, y=190)
        '''

    def say_hi(self):
        print("hi there, everyone!")

    def export1(self):
        export = filedialog.asksaveasfile()
        print(export)

    def startMove(self, event):
        self.x = event.x
        self.y = event.y

    def stopMove(self, event):
        self.x = None
        self.y = None

    def moving(self, event):
        x = (event.x_root - self.x - self.root.winfo_rootx() + self.root.winfo_rootx())
        y = (event.y_root - self.y - self.root.winfo_rooty() + self.root.winfo_rooty())
        self.root.geometry("+%s+%s" % (x, y))

    def exitProgram(self, asdasd):
        self.root.destroy()

    def exitProgram(self, asdasd):
        self.root.destroy()

    def frame_mapped(self, e):
        print(self, e)
        self.root.update_idletasks()
        self.root.overrideredirect(True)
        self.root.state('normal')

    def minimize(self,asdasd):
        self.root.update_idletasks()
        self.root.overrideredirect(False)
        self.root.state('withdrawn')
        self.root.state('iconic')
