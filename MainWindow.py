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
import Function as F



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
        PasekGora.create_rectangle(0, 57, 1050, 120, fill='#3C3E45', outline='#3C3E45')
        PasekGora.create_rectangle(0, 121, 200, 724, fill='#3C3E45', outline='#3C3E45')


        ### Ikona
        my_img = ImageTk.PhotoImage(Image.open("Ikona.png"))

        myLabel= tk.Label(self.root,image=my_img,bg='#004554')
        myLabel.photo = my_img
        #myLabel.config(bg="")
        myLabel.place(x=10,y=2.5, height=48, width=48)


        ### icony

        email_ic = ImageTk.PhotoImage(Image.open("ikoneczki\email.png"))
        emailL = tk.Label(self.root, image=email_ic, bg ='red' )
        emailL.photo = email_ic

        home_ic = ImageTk.PhotoImage(Image.open("ikoneczki\home.png"))
        homeL = tk.Label(self.root, image = home_ic)
        homeL.photo=home_ic

        add_ic = ImageTk.PhotoImage(Image.open("ikoneczki\plus.png"))
        addL = tk.Label(self.root, image = add_ic)
        addL.photo = add_ic

        delete_ic = ImageTk.PhotoImage(Image.open("ikoneczki\delete.png"))
        deleteL = tk.Label(self.root, image = delete_ic)
        deleteL.photo = delete_ic

        show_ic = ImageTk.PhotoImage(Image.open("ikoneczki\show.png"))
        showL = tk.Label(self.root, image = show_ic)
        showL.photo = show_ic

        chemistry_ic = ImageTk.PhotoImage(Image.open("ikoneczki\chemistry.png"))
        chemistryL = tk.Label(self.root, image = chemistry_ic)
        chemistryL.photo = chemistry_ic

        order_ic = ImageTk.PhotoImage(Image.open("ikoneczki\cart.png"))
        orderL = tk.Label(self.root, image = order_ic)
        orderL.photo = order_ic

        help_ic = ImageTk.PhotoImage(Image.open("ikoneczki\info.png"))
        helpL =  tk.Label(self.root, image = help_ic)
        helpL.photo = help_ic




       # testbutton = tk.Button(self.root, image=email_ic)
        #testbutton.place(width=80, height =40, x=10,y=200  )


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

        #bg='#3C3E45
        self.Designer = tk.Label(self.root, font=("Arial", 11), bg='#3C3E45', fg='white', text="Created by:\n Krzysztof Wójcik")
        self.Designer.place(height=60, width=140, x=15, y=655)




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

        LHome = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Home",anchor="w", cursor="hand2")
        LHome["compound"] = tk.LEFT
        LHome["image"] = home_ic
        LHome.tkraise(aboveThis=PasekGora)
        LHome.place(x=15, y=150, width=170, height=40)

        LAddEq = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Add Equipment",anchor="w",  cursor="hand2")
        LAddEq["compound"] = tk.LEFT
        LAddEq["image"] = add_ic
        LAddEq.tkraise(aboveThis=PasekGora)
        LAddEq.place(x=15, y=200, width=170, height=40)

        LDeleteEq = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white' , text="   Delete Equipment",anchor="w", cursor="hand2")
        LDeleteEq["compound"] = tk.LEFT
        LDeleteEq["image"] = delete_ic
        LDeleteEq.tkraise(aboveThis=PasekGora)
        LDeleteEq.place(x=15, y=250, width=170, height=40)

        LShowEq = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Show Equipment",anchor="w", cursor="hand2")
        LShowEq["compound"] = tk.LEFT
        LShowEq["image"] = show_ic
        LShowEq.tkraise(aboveThis=PasekGora)
        LShowEq.place(x=15, y=300, width=170, height=40)

        LChemistry = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Chemistry",anchor="w", cursor="hand2")
        LChemistry["compound"] = tk.LEFT
        LChemistry["image"] = chemistry_ic
        LChemistry.tkraise(aboveThis=PasekGora)
        LChemistry.place(x=15, y=350, width=170, height=40)

        LMakeOrder = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Make Order",anchor="w", cursor="hand2")
        LMakeOrder["compound"] = tk.LEFT
        LMakeOrder["image"] = order_ic
        LMakeOrder.tkraise(aboveThis=PasekGora)
        LMakeOrder.place(x=15, y=400, width=170, height=40)

        LHelp = tk.Label(self.root, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Help",anchor="w", cursor="hand2")
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
        MakeOrder = tk.Frame(self.root, bg=colortłaFramesAdd)

        ### Bindowanie klawiszy funkcyjnych

        def forgetFrames():
            Home.place_forget()
            AddEq.place_forget()
            DeleteEq.place_forget()
            ShowEq.place_forget()
            Chemistry.place_forget()
            MakeOrder.place_forget()

        def powrotkolorow(event):
            event.widget.config(fg='white')

        def klik(event):
            event.widget.config(bg="#52555E")

        def zwolnienie(event):
            event.widget.config(bg='#3C3E45')

        def aktywny(event):
            event.widget.config(fg='white')

        def showHome(event):
            print("Work1")
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
            MakeOrder.place(x=199, y=118, height=610, width=850)

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

        ###colory
        colortło1AddEq = '#404040'
        colortło2AddEq = '#737373'
        colorPrzyciskowAddEq = '#404040'

        self.PadAdd1 = tk.PanedWindow(AddEq,bg=colortło1AddEq, handlepad=True)
        self.PadAdd1.place(height=700, width=140, x=0, y=0)

        self.PadAdd2 = tk.PanedWindow(AddEq, bg = colortło2AddEq)
        self.PadAdd2.place(height=640, width=720, x=140, y=0)
        # tworze widzety dla paddAdd


        # Tworzenie widgetów dla Padd1

        self.TitlePad1 = tk.Label(self.PadAdd1, text="Options" )
       # self.TitlePad1.place(width=80 ,height=40 ,x=5 ,y=5 )

        self.Sep1Padd1 = ttk.Separator(self.PadAdd1, orient='horizontal')
        self.Sep1Padd1.place(width=130, x= 5, y = 40)

        self.AddComponent = tk.Label(self.PadAdd1, font=("Arial", 13), bg=colorPrzyciskowAddEq,fg='white', text="Choose a type")
        self.AddComponent.place(width=120, height=40, x = 5, y = 0 )



        # Funkcje dla pad 1






        self.AddSemiconductors = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',anchor="w",text="Semiconductors", cursor="hand2")
        self.AddSemiconductors.place(width=110, height=40, x = 15, y = 50 )

        self.AddPassiveElements = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white',anchor="w", text="PassiveElements", cursor="hand2")
        self.AddPassiveElements.place(width=110, height=40, x = 15, y = 100 )

        self.AddOptoelectronic = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white', anchor="w",text="Optoelectronic", cursor="hand2")
        self.AddOptoelectronic.place(width=110, height=40, x = 15, y = 150 )

        self.AddConnectors = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white',anchor="w", text="Connectors", cursor="hand2")
        self.AddConnectors.place(width=110, height=40, x = 15, y = 200 )

        self.AddEnergySources = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white',anchor="w", text="EnergySources", cursor="hand2")
        self.AddEnergySources.place(width=110, height=40, x = 15, y = 250 )

        self.AddPCAccesories = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white',anchor="w",text="PCAccesories", cursor="hand2")
        self.AddPCAccesories.place(width=110, height=40, x = 15, y = 300 )

        self.AddSwitches = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white',anchor="w", text="Switches", cursor="hand2")
        self.AddSwitches.place(width=110, height=40, x = 15, y = 350 )

        self.AddWires = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',anchor="w",text="Wires", cursor="hand2")
        self.AddWires.place(width=110, height=40, x = 15, y = 400 )

        self.AddMechanics = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white',anchor="w", text="Mechanics", cursor="hand2")
        self.AddMechanics.place(width=110, height=40, x = 15, y = 450 )

        self.AddLaboratory = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq,fg='white', anchor="w",text="Laboratory", cursor="hand2")
        self.AddLaboratory.place(width=110, height=40, x = 15, y = 500 )

        self.AddOthers = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',anchor="w",text="Others", cursor="hand2")
        self.AddOthers.place(width=110, height=40, x = 15, y = 550 )

        # Tworzenie widgetow dla padd2



        self.Semiconductors = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.PassiveElements = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.OptoElectronics = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.Connectors = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.EnergySources = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.PCAccessories = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.Switches = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.Wires = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.Mechanics = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.Laboratory = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)
        self.Others = tk.Frame(self.PadAdd2, bg=colortłaFramesAdd)

        # ZAKLADKI Do dodawania elementow

        # SEMICONDUCTORS

        # Przyciski
        self.AddComponent = tk.Button(self.Semiconductors, text='Add', font=14, bg='#0052cc', fg='white'
                                      )
        self.AddComponent.place(height=40, width=80, x=15, y=445)

        self.ClearComponent = tk.Button(self.Semiconductors, text='Clear', font=14, bg='#0052cc', fg='white',
                                      )
        self.ClearComponent.place(height=40, width=80, x=110, y=445)

        self.UploadLink = tk.Button(self.Semiconductors, text='Upload Link', font=14, bg='#0052cc', fg='white',
                                    )
        self.UploadLink.place(height=40, width=100, x=205, y=445)

        self.UploadPdf = tk.Button(self.Semiconductors, text='Upload PDF', font=14, bg='#0052cc', fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        #Labelki

        self.AddTitle = tk.Label(self.Semiconductors,font=("Arial", 20), text="Add new item:",anchor='w', bg=colortłaFramesAdd, fg ='white')
        self.AddTitle.place(height=40, width=280, x=10, y=10)


        self.lName = tk.Label(self.Semiconductors, text="Name:",bg=colortłaFramesAdd )
        self.lName.place(height=40, width=80, x=10, y=60)

        self.lGroup = tk.Label(self.Semiconductors, text="Group:",bg=colortłaFramesAdd)
        self.lGroup.place(height=40, width=80, x=10, y=100)

        self.lSubCategory = tk.Label(self.Semiconductors, text="SubCategory:",bg=colortłaFramesAdd)
        self.lSubCategory.place(height=40, width=80, x=10, y=140)

        self.lModel = tk.Label(self.Semiconductors, text="Model:",bg=colortłaFramesAdd)
        self.lModel.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Semiconductors, text="Assembly:",bg=colortłaFramesAdd)
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSize = tk.Label(self.Semiconductors, text="Size:",bg=colortłaFramesAdd)
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lWhere = tk.Label(self.Semiconductors, text="Where:",bg=colortłaFramesAdd)
        self.lWhere.place(height=40, width=80, x=10, y=300)

        self.lQuintity = tk.Label(self.Semiconductors, text="Quintity:",bg=colortłaFramesAdd)
        self.lQuintity.place(height=40, width=80, x=10, y=340)

        # Grupy i kategorie

        self.SizeComponents = ["0201", "0402", "0603", "0805", "1008", "1206", "1210"]

        self.SposobMontazu = ["THT", "SMD", ]

        self.grupa = ["Diodes", "Thyristors", "Triacs", "Diacs", "Transistors", "Integrated circuits"]

        self.subcategorysemi = ["Universal diodes", "Schottky diodes","Zener diodes","Transil diodes",
                                "Single phase bridge rectifiers","Three phase bridge rectifiers","Single thyristores",
                                "Thyristor modules","Unipolar transistors","Bipolar transistors",
                                "IGBT transistors and modules","Analog and mixed integrated circuits",
                                "Logic integrated circuits ","Microcontrollers and Microprocessors",
                                "Memories - integrated circuits","Peripheral integrated circuits",
                                "Voltage regulators","Others"]

        self.CasesTHT = ["DIP", "SDIP" , "TO" ]

        self.CasesSMD = ["SOJ", "SOIC", "PLCC", "QFP", "BGA"]

        #Wejscia

        self.eName = ttk.Entry(self.Semiconductors, width=50)
        self.eName.place(height=20, width=230, x=100, y=70)

        self.eGroup = ttk.Combobox(self.Semiconductors, values=self.grupa)
        self.eGroup.place(height=20, width=230, x=100, y=110)

        self.eSubCategory = ttk.Combobox(self.Semiconductors, values=self.subcategorysemi)
        self.eSubCategory.place(height=20, width=230, x=100, y=150)

        self.eModel = ttk.Entry(self.Semiconductors, width=50)
        self.eModel.place(height=20, width=230, x=100, y=190)

        self.eAssembly = ttk.Combobox(self.Semiconductors, values=self.SposobMontazu)
        self.eAssembly.place(height=20, width=230, x=100, y=230)

        self.eSize = ttk.Entry(self.Semiconductors, width=50)
        self.eSize.place(height=20, width=230, x=100, y=270)

        self.eWhere = ttk.Entry(self.Semiconductors, width=50)
        self.eWhere.place(height=20, width=230, x=100, y=310)

        self.eQuintity = ttk.Entry(self.Semiconductors, width=50)
        self.eQuintity.place(height=20, width=230, x=100, y=350)

        # Wejscia link i dokumenty i obrazy

        self.Link = tk.Label(self.Semiconductors, text="Tutaj będzie link",bg=colortłaFramesAdd)
        self.Link.place(height=40, width=180, x=360, y=340)

        self.Obraz = ttk.Button(self.Semiconductors, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width= 250, x=360, y = 70 )

       # self.Link = tk.Entry(self.Semiconductors, width=50)
       # self.Link.place(height=20, width=180, x=340, y=200)


        #PassiveElements

        #Przyciski
        self.AddPassive = tk.Button(self.PassiveElements, text='Add', font=14, bg='#0052cc', fg='white')
        self.AddPassive.place(height=40, width=80, x=15, y=520)

        self.ClearPassive = tk.Button(self.PassiveElements, text='Clear', font=14, bg='#0052cc', fg='white')
        self.ClearPassive.place(height=40, width=80, x=110, y=520)

        self.UploadLinkPassive = tk.Button(self.PassiveElements, text='Upload Link', font=14, bg='#0052cc', fg='white')
        self.UploadLinkPassive.place(height=40, width=100, x=205, y=520)

        self.UploadPdfPassive = tk.Button(self.PassiveElements, text='Upload PDF', font=14, bg='#0052cc', fg='white')
        self.UploadPdfPassive.place(height=40, width=100, x=320, y=520)

        #Labelki

        self.AddTitlePassive = tk.Label(self.PassiveElements, font=("Arial", 20), text="Add new item:", anchor='w',
                                 bg=colortłaFramesAdd, fg='white')
        self.AddTitlePassive.place(height=40, width=280, x=10, y=10)

        self.lNamePassive = tk.Label(self.PassiveElements, text="Name:", bg=colortłaFramesAdd)
        self.lNamePassive.place(height=40, width=80, x=10, y=60)

        self.lGroupPassive = tk.Label(self.PassiveElements, text="Group:", bg=colortłaFramesAdd)
        self.lGroupPassive.place(height=40, width=80, x=10, y=100)

        self.lSubCategoryPassive = tk.Label(self.PassiveElements, text="SubCategory:", bg=colortłaFramesAdd)
        self.lSubCategoryPassive.place(height=40, width=80, x=10, y=140)

        self.lModelPassive = tk.Label(self.PassiveElements, text="Model:", bg=colortłaFramesAdd)
        self.lModelPassive.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.PassiveElements, text="Assembly:", bg=colortłaFramesAdd)
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSizePassive = tk.Label(self.PassiveElements, text="Size:", bg=colortłaFramesAdd)
        self.lSizePassive.place(height=40, width=80, x=10, y=260)

        self.lValuePassive = tk.Label(self.PassiveElements, text="Value:", bg=colortłaFramesAdd)
        self.lValuePassive.place(height=40, width=80, x=10, y=300)

        self.lTolerancePassive = tk.Label(self.PassiveElements, text="Tolerance:", bg=colortłaFramesAdd)
        self.lTolerancePassive.place(height=40, width=80, x=10, y=340)

        self.lWatsPassive = tk.Label(self.PassiveElements, text="Wats:", bg=colortłaFramesAdd)
        self.lWatsPassive.place(height=40, width=80, x=10, y=380)

        self.lWherePassive = tk.Label(self.PassiveElements, text="Where:", bg=colortłaFramesAdd)
        self.lWherePassive.place(height=40, width=80, x=10, y=420)

        self.lQuintityPassive = tk.Label(self.PassiveElements, text="Quintity:", bg=colortłaFramesAdd)
        self.lQuintityPassive.place(height=40, width=80, x=10, y=460)

        ### Kategorie

        self.grupapassive = ["Resistors","Capacitors","Inductors","thermistors","Potentiometers","Encoders",
                                   "Quartz crystals and filters","EMI/EMC components","Varistors","Antennas"]

        self.subcategorypassive=["Precision resistors","Carbon THT resistors","Metal film THT resistors","Power resistors","Resistor networks","Trimmers", "Shaft potentiometers" ,"Slide potentiometers","Audio potentiometers"]

        self.sposobmontazupassive=["THT","SMD","CABLE"]

        #Wejscia

        self.eNamePassive = ttk.Entry(self.PassiveElements, width=50)
        self.eNamePassive.place(height=20, width=230, x=100, y=70)

        self.eGroupPassive = ttk.Combobox(self.PassiveElements, values=self.grupapassive)
        self.eGroupPassive.place(height=20, width=230, x=100, y=110)

        self.eSubCategoryPassive = ttk.Combobox(self.PassiveElements, values=self.subcategorypassive)
        self.eSubCategoryPassive.place(height=20, width=230, x=100, y=150)

        self.eModelPassive = ttk.Entry(self.PassiveElements, width=50)
        self.eModelPassive.place(height=20, width=230, x=100, y=190)

        self.eAssemblyPassive = ttk.Combobox(self.PassiveElements, values=self.sposobmontazupassive)
        self.eAssemblyPassive.place(height=20, width=230, x=100, y=230)

        self.eSizePassive = ttk.Entry(self.PassiveElements, width=50)
        self.eSizePassive.place(height=20, width=230, x=100, y=270)

        self.eValuePassive = ttk.Entry(self.PassiveElements, width=50)
        self.eValuePassive.place(height=20, width=230, x=100, y=310)

        self.eTolerancePassive = ttk.Entry(self.PassiveElements, width=50)
        self.eTolerancePassive.place(height=20, width=230, x=100, y=350)

        self.eWatsPassive = ttk.Entry(self.PassiveElements, width=50)
        self.eWatsPassive.place(height=20, width=230, x=100, y=390)

        self.eWherePassive = ttk.Entry(self.PassiveElements, width=50)
        self.eWherePassive.place(height=20, width=230, x=100, y=430)

        self.eQuintityPassive = ttk.Entry(self.PassiveElements, width=50)
        self.eQuintityPassive.place(height=20, width=230, x=100, y=470)

        #OptoElectronics

        #Przyciski

        # Labelki

        # Wejscia



        #Connectors

        #Przyciski
        # Labelki
        # Wejscia


        #EnergySources

        #Przyciski
        # Labelki
        # Wejscia

        #PCAccessories

        #Przyciski
        # Labelki
        # Wejscia


        #Switches

        #Przyciski
        # Labelki
        # Wejscia


        #Wires

        # Przyciski
        # Labelki
        # Wejscia


        #Mechanics

        # Przyciski
        # Labelki
        # Wejscia

        #Laboratory

        # Przyciski
        # Labelki
        # Wejscia

        #Others

        # Przyciski
        # Labelki
        # Wejscia

        ### CHOWANIE I POKAZYWANIE zakładek

        def forgetPadd2(event):
            self.Semiconductors.place_forget()
            self.PassiveElements.place_forget()
            self.OptoElectronics.place_forget()
            self.Connectors.place_forget()
            self.EnergySources.place_forget()
            self.PCAccessories.place_forget()
            self.Switches.place_forget()
            self.Wires.place_forget()
            self.Mechanics.place_forget()
            self.Laboratory.place_forget()
            self.Others.place_forget()

        def showSemiconductors(event):
            forgetPadd2(event)
            self.Semiconductors.place(height=590, width=695, x=5, y=5)
            print("1")

        def showPassiveElements(event):
            forgetPadd2(event)
            self.PassiveElements.place(height=590, width=695, x=5, y=5)
            print("2")

        def showOptoelectronic(event):
            forgetPadd2(event)
            self.OptoElectronics.place(height=590, width=695, x=5, y=5)
            print("3")

        def showConnectors(event):
            forgetPadd2(event)
            self.Connectors.place(height=590, width=695, x=5, y=5)
            print("4")

        def showEnergySources(event):
            forgetPadd2(event)
            self.EnergySources.place(height=590, width=695, x=5, y=5)
            print("5")

        def showPCAccessories(event):
            forgetPadd2(event)
            self.PCAccessories.place(height=590, width=695, x=5, y=5)
            print("6")

        def showSwitches(event):
            forgetPadd2(event)
            self.Switches.place(height=590, width=695, x=5, y=5)
            print("7")

        def showWires(event):
            forgetPadd2(event)
            self.Wires.place(height=590, width=695, x=5, y=5)
            print("8")

        def showMechanics(event):
            forgetPadd2(event)
            self.Mechanics.place(height=590, width=695, x=5, y=5)
            print("9")

        def showLaboratory(event):
            forgetPadd2(event)
            self.Laboratory.place(height=590, width=695, x=5, y=5)
            print("10")

        def showOthers(event):
            forgetPadd2(event)
            self.Others.place(height=590, width=695, x=5, y=5)
            print("11")

        ### bindowanie klawiszy

        self.AddSemiconductors.bind("<Enter>", klik)
        self.AddSemiconductors.bind("<Leave>", zwolnienie)
        self.AddSemiconductors.bind("<Button-1>", showSemiconductors)

        self.AddPassiveElements.bind("<Enter>", klik)
        self.AddPassiveElements.bind("<Leave>", zwolnienie)
        self.AddPassiveElements.bind("<Button-1>", showPassiveElements)

        self.AddOptoelectronic.bind("<Enter>", klik)
        self.AddOptoelectronic.bind("<Leave>", zwolnienie)
        self.AddOptoelectronic.bind("<Button-1>", showOptoelectronic)

        self.AddConnectors.bind("<Enter>", klik)
        self.AddConnectors.bind("<Leave>", zwolnienie)
        self.AddConnectors.bind("<Button-1>", showConnectors)

        self.AddEnergySources.bind("<Enter>", klik)
        self.AddEnergySources.bind("<Leave>", zwolnienie)
        self.AddEnergySources.bind("<Button-1>", showEnergySources)

        self.AddPCAccesories.bind("<Enter>", klik)
        self.AddPCAccesories.bind("<Leave>", zwolnienie)
        self.AddPCAccesories.bind("<Button-1>", showPCAccessories)

        self.AddSwitches.bind("<Enter>", klik)
        self.AddSwitches.bind("<Leave>", zwolnienie)
        self.AddSwitches.bind("<Button-1>", showSwitches)

        self.AddWires.bind("<Enter>", klik)
        self.AddWires.bind("<Leave>", zwolnienie)
        self.AddWires.bind("<Button-1>", showWires)

        self.AddMechanics.bind("<Enter>", klik)
        self.AddMechanics.bind("<Leave>", zwolnienie)
        self.AddMechanics.bind("<Button-1>", showMechanics)

        self.AddLaboratory.bind("<Enter>", klik)
        self.AddLaboratory.bind("<Leave>", zwolnienie)
        self.AddLaboratory.bind("<Button-1>", showLaboratory)

        self.AddOthers.bind("<Enter>", klik)
        self.AddOthers.bind("<Leave>", zwolnienie)
        self.AddOthers.bind("<Button-1>", showOthers)



        # ########################################################################################DELETE EQUIPMENT



        # #########################################################################################SHOW EQUIPMENT

        ### Stworzenie dwóch panel widnow

        self.ShowEQPad1 = tk.PanedWindow(ShowEq,bg="green", handlepad=True)
        self.ShowEQPad1.place(height=590, width=180, x=0, y=0)

        self.ShowEQPad2 = tk.PanedWindow(ShowEq,bg="yellow")
        self.ShowEQPad2.place(height=590, width=650, x=185, y=0)


        ### Stworzenie widgetów dla 1 panelu

        self.ShowSemiconductors = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Semiconductors",
                                          cursor="hand2")
        self.ShowSemiconductors.place(width=100, height=40, x=5, y=50)

        self.ShowPassiveElements = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="PassiveElements",
                                           cursor="hand2")
        self.ShowPassiveElements.place(width=100, height=40, x=5, y=100)

        self.ShowOptoelectronic = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Optoelectronic",
                                          cursor="hand2")
        self.ShowOptoelectronic.place(width=100, height=40, x=5, y=150)

        self.ShowConnectors = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Connectors", cursor="hand2")
        self.ShowConnectors.place(width=100, height=40, x=5, y=200)

        self.ShowEnergySources = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="EnergySources",
                                         cursor="hand2")
        self.ShowEnergySources.place(width=100, height=40, x=5, y=250)

        self.ShowPCAccesories = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="PCAccesories",
                                        cursor="hand2")
        self.ShowPCAccesories.place(width=100, height=40, x=5, y=300)

        self.ShowSwitches = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Switches", cursor="hand2")
        self.ShowSwitches.place(width=100, height=40, x=5, y=350)

        self.ShowWires = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Wires", cursor="hand2")
        self.ShowWires.place(width=100, height=40, x=5, y=400)

        self.ShowMechanics = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Mechanics", cursor="hand2")
        self.ShowMechanics.place(width=100, height=40, x=5, y=450)

        self.ShowLaboratory = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Laboratory", cursor="hand2")
        self.ShowLaboratory.place(width=100, height=40, x=5, y=500)

        self.ShowOthers = tk.Label(self.ShowEQPad1, font=("Arial", 10), bg='white', text="Others", cursor="hand2")
        self.ShowOthers.place(width=100, height=40, x=5, y=550)


        ### Stworzenie ramek dla 2 widgetu

        self.ShowSemiconductorsFrame = tk.Frame(self.ShowEQPad2, bg="white")
        self.ShowPassiveElementsFrame = tk.Frame(self.ShowEQPad2, bg="black")
        self.ShowOptoElectronicsFrame = tk.Frame(self.ShowEQPad2, bg="white")
        self.ShowConnectorsFrame = tk.Frame(self.ShowEQPad2, bg="black")
        self.ShowEnergySourcesFrame = tk.Frame(self.ShowEQPad2, bg="white")
        self.ShowPCAccessoriesFrame = tk.Frame(self.ShowEQPad2, bg="black")
        self.ShowSwitchesFrame = tk.Frame(self.ShowEQPad2, bg="white")
        self.ShowWiresFrame = tk.Frame(self.ShowEQPad2, bg="black")
        self.ShowMechanicsFrame = tk.Frame(self.ShowEQPad2, bg="white")
        self.ShowLaboratoryFrame = tk.Frame(self.ShowEQPad2, bg="black")
        self.ShowOthersFrame = tk.Frame(self.ShowEQPad2, bg="white")

        ### Dodaanie widgetow do zakładek
        ###








        ### Bindowanie i wyswietlanie zakładek
        def forgetShowEQPad2(event):
            self.ShowSemiconductorsFrame.place_forget()
            self.ShowPassiveElementsFrame.place_forget()
            self.ShowOptoElectronicsFrame.place_forget()
            self.ShowConnectorsFrame.place_forget()
            self.ShowEnergySourcesFrame.place_forget()
            self.ShowPCAccessoriesFrame.place_forget()
            self.ShowSwitchesFrame.place_forget()
            self.ShowWiresFrame.place_forget()
            self.ShowMechanicsFrame.place_forget()
            self.ShowLaboratoryFrame.place_forget()
            self.ShowOthersFrame.place_forget()

        def showShowSemiconductorsFrame(event):
            forgetShowEQPad2(event)
            self.ShowSemiconductorsFrame.place(height=500, width=640, x=5, y=5)
            print("1")

        def showShowPassiveElementsFrame(event):
            forgetShowEQPad2(event)
            self.ShowPassiveElementsFrame.place(height=500, width=640, x=5, y=5)
            print("2")

        def ShowOptoElectronicsFrame(event):
            forgetShowEQPad2(event)
            self.ShowOptoElectronicsFrame.place(height=500, width=640, x=5, y=5)
            print("3")

        def showShowConnectorsFrame(event):
            forgetShowEQPad2(event)
            self.ShowConnectorsFrame.place(height=500, width=640, x=5, y=5)
            print("4")

        def showShowEnergySourcesFrame(event):
            forgetShowEQPad2(event)
            self.ShowEnergySourcesFrame.place(height=500, width=640, x=5, y=5)
            print("5")

        def showShowPCAccessoriesFrame(event):
            forgetShowEQPad2(event)
            self.ShowPCAccessoriesFrame.place(height=500, width=640, x=5, y=5)
            print("6")

        def showShowSwitchesFrame(event):
            forgetShowEQPad2(event)
            self.ShowSwitches.place(height=500, width=640, x=5, y=5)
            print("7")

        def showShowWiresFrame(event):
            forgetShowEQPad2(event)
            self.ShowWiresFrame.place(height=500, width=640, x=5, y=5)
            print("8")

        def showShowMechanicsFrame(event):
            forgetShowEQPad2(event)
            self.ShowMechanicsFrame.place(height=500, width=640, x=5, y=5)
            print("9")

        def showShowLaboratoryFrame(event):
            forgetShowEQPad2(event)
            self.ShowLaboratoryFrame.place(height=500, width=640, x=5, y=5)
            print("10")

        def showShowOthersFrame(event):
            forgetShowEQPad2(event)
            self.ShowOthersFrame.place(height=500, width=640, x=5, y=5)
            print("11")

        ### bindowanie klawiszy

        self.ShowSemiconductors.bind("<Enter>", klik)
        self.ShowSemiconductors.bind("<Leave>", zwolnienie)
        self.ShowSemiconductors.bind("<Button-1>", showShowSemiconductorsFrame)

        self.ShowPassiveElements.bind("<Enter>", klik)
        self.ShowPassiveElements.bind("<Leave>", zwolnienie)
        self.ShowPassiveElements.bind("<Button-1>",showShowPassiveElementsFrame)

        self.ShowOptoelectronic.bind("<Enter>", klik)
        self.ShowOptoelectronic.bind("<Leave>", zwolnienie)
        self.ShowOptoelectronic.bind("<Button-1>", ShowOptoElectronicsFrame)

        self.ShowConnectors.bind("<Enter>", klik)
        self.ShowConnectors.bind("<Leave>", zwolnienie)
        self.ShowConnectors.bind("<Button-1>", showShowConnectorsFrame)

        self.ShowEnergySources.bind("<Enter>", klik)
        self.ShowEnergySources.bind("<Leave>", zwolnienie)
        self.ShowEnergySources.bind("<Button-1>", showShowEnergySourcesFrame)

        self.ShowPCAccesories.bind("<Enter>", klik)
        self.ShowPCAccesories.bind("<Leave>", zwolnienie)
        self.ShowPCAccesories.bind("<Button-1>", showShowPCAccessoriesFrame)

        self.ShowSwitches.bind("<Enter>", klik)
        self.ShowSwitches.bind("<Leave>", zwolnienie)
        self.ShowSwitches.bind("<Button-1>", showShowSwitchesFrame)

        self.ShowWires.bind("<Enter>", klik)
        self.ShowWires.bind("<Leave>", zwolnienie)
        self.ShowWires.bind("<Button-1>", showShowWiresFrame)

        self.ShowMechanics.bind("<Enter>", klik)
        self.ShowMechanics.bind("<Leave>", zwolnienie)
        self.ShowMechanics.bind("<Button-1>",showShowMechanicsFrame )

        self.ShowLaboratory.bind("<Enter>", klik)
        self.ShowLaboratory.bind("<Leave>", zwolnienie)
        self.ShowLaboratory.bind("<Button-1>", showShowLaboratoryFrame)

        self.ShowOthers.bind("<Enter>", klik)
        self.ShowOthers.bind("<Leave>", zwolnienie)
        self.ShowOthers.bind("<Button-1>",showShowOthersFrame )



        # ################################################################################################CHEMISTRY


        ############################################################################################### MAKEORDER


        # Przyciski
        self.conf = tk.IntVar()
        self.Confirmation = ttk.Checkbutton(MakeOrder, text="I accept the terms and conditions of orders ",
                                            style='green/black.TCheckbutton', variable=self.conf,
                                            )

        self.Confirmation.place(height=40, width=400, x=15, y=520)

        self.BOrder = tk.Button(MakeOrder, text='Make Order', font=14, bg='#0052cc',
                                fg='white', )
        self.BOrder.place(height=40, width=100, x=730, y=520)

        #Labelki

        self.OrderTitle = tk.Label(MakeOrder, text='Order Menagement',
                                   bg=colortłaFramesAdd, fg='white', font=("Helvetica", 20),anchor='w')
        self.OrderTitle.place(height=55, width=630, x=15, y=0)

        self.OrderT = tk.Label(MakeOrder, text='Write an order, put your items with quantity and links that you want to order:' ,anchor='w',
                               bg=colortłaFramesAdd, font=("Helvetica", 12))
        self.OrderT.place(height=55, width=520, x=15, y=60)

        self.SepOrd = ttk.Separator(MakeOrder, orient='horizontal')
        self.SepOrd.place(width=820, x=12.5, y=500)

        self.lNameoftheOrder = tk.Label(MakeOrder, text='Name of the order:', anchor='w',
                               bg=colortłaFramesAdd, font=("Helvetica", 12))
        self.lNameoftheOrder.place(height=60, width=160, x=15, y=100)

        #Wejscia

        self.eNameoftheOrder = tk.Text(MakeOrder)
        self.eNameoftheOrder.place(height=20, width=650, x=180, y=120)

        self.eOrder = tk.Text(MakeOrder)
        self.eOrder.place(height=320, width=815, x=15, y=160)

        ttk.Style().configure('green/black.TCheckbutton', foreground='blue', background=colortłaFramesAdd)



        # HELP
        #
        #
        #
        #
        #
        #





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
        ###werewrwer


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
