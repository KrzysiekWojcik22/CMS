import tkinter as tk
from tkinter import ttk
import classes as cl

Color = cl.ColoursMainWindow()


class AddEquipmentFirst:
    def __init__(self, master):
        self.Add_EQ = tk.Frame(master, bg="red")
        self.Add_EQ.place(x=0, y=0, height=610, width=850)
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

        self.Sep1Pad1 = ttk.Separator(self.PadAdd1, orient='horizontal')
        self.Sep1Pad1.place(width=130, x=5, y=40)

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

        self.AddOptoelectronic = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',
                                          anchor="w", text="Optoelectronic", cursor="hand2")
        self.AddOptoelectronic.place(width=110, height=40, x=15, y=150)

        self.AddConnectors = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white', anchor="w",
                                      text="Connectors", cursor="hand2")
        self.AddConnectors.place(width=110, height=40, x=15, y=200)

        self.AddEnergySources = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',
                                         anchor="w", text="EnergySources", cursor="hand2")
        self.AddEnergySources.place(width=110, height=40, x=15, y=250)

        self.AddPCAccesories = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white',
                                        anchor="w", text="PCAccesories", cursor="hand2")
        self.AddPCAccesories.place(width=110, height=40, x=15, y=300)

        self.AddSwitches = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white', anchor="w",
                                    text="Switches", cursor="hand2")
        self.AddSwitches.place(width=110, height=40, x=15, y=350)

        self.AddWires = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white', anchor="w",
                                 text="Wires", cursor="hand2")
        self.AddWires.place(width=110, height=40, x=15, y=400)

        self.AddMechanics = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white', anchor="w",
                                     text="Mechanics", cursor="hand2")
        self.AddMechanics.place(width=110, height=40, x=15, y=450)

        self.AddLaboratory = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white', anchor="w",
                                      text="Laboratory", cursor="hand2")
        self.AddLaboratory.place(width=110, height=40, x=15, y=500)

        self.AddOthers = tk.Label(self.PadAdd1, font=("Arial", 10), bg=colorPrzyciskowAddEq, fg='white', anchor="w",
                                  text="Others", cursor="hand2")
        self.AddOthers.place(width=110, height=40, x=15, y=550)

        ##################################

        self.AddSemiconductors.bind("<Enter>", cl.click)
        self.AddSemiconductors.bind("<Leave>", cl.zwolnienie)
        self.AddSemiconductors.bind("<Button-1>", lambda x: self.add_semiconductors())

        self.AddPassiveElements.bind("<Enter>", cl.click)
        self.AddPassiveElements.bind("<Leave>", cl.zwolnienie)
        self.AddPassiveElements.bind("<Button-1>", lambda x: self.add_passive_elements())

        self.AddOptoelectronic.bind("<Enter>", cl.click)
        self.AddOptoelectronic.bind("<Leave>", cl.zwolnienie)
       # self.AddOptoelectronic.bind("<Button-1>", showOptoelectronic)

        self.AddConnectors.bind("<Enter>", cl.click)
        self.AddConnectors.bind("<Leave>", cl.zwolnienie)
       # self.AddConnectors.bind("<Button-1>", showConnectors)

        self.AddEnergySources.bind("<Enter>", cl.click)
        self.AddEnergySources.bind("<Leave>", cl.zwolnienie)
       # self.AddEnergySources.bind("<Button-1>", showEnergySources)

        self.AddPCAccesories.bind("<Enter>", cl.click)
        self.AddPCAccesories.bind("<Leave>", cl.zwolnienie)
       # self.AddPCAccesories.bind("<Button-1>", showPCAccessories)

        self.AddSwitches.bind("<Enter>", cl.click)
        self.AddSwitches.bind("<Leave>", cl.zwolnienie)
        #self.AddSwitches.bind("<Button-1>", showSwitches)

        self.AddWires.bind("<Enter>", cl.click)
        self.AddWires.bind("<Leave>", cl.zwolnienie)
       # self.AddWires.bind("<Button-1>", cl.showWires)

        self.AddMechanics.bind("<Enter>", cl.click)
        self.AddMechanics.bind("<Leave>", cl.zwolnienie)
       # self.AddMechanics.bind("<Button-1>", showMechanics)

        self.AddLaboratory.bind("<Enter>", cl.click)
        self.AddLaboratory.bind("<Leave>", cl.zwolnienie)
        #self.AddLaboratory.bind("<Button-1>", showLaboratory)

        self.AddOthers.bind("<Enter>", cl.click)
        self.AddOthers.bind("<Leave>", cl.zwolnienie)
        #self.AddOthers.bind("<Button-1>", showOthers)

    def add_semiconductors(self):
        AddEquipmentSemiconductors(master=self.PadAdd2)

    def add_passive_elements(self):
        AddEquipmentPassiveElements(master=self.PadAdd2)

    def add_connectors(self):
        print("Hello")

    def add_energy_sources(self):
        print("Hello")

    def add_wires(self):
        print("Hello")


class AddEquipmentSemiconductors:
    def __init__(self, master):
        self.Add_Semi = tk.Frame(master, bg="red")
        self.Add_Semi.place(x=0, y=0, height=610, width=850)

        self.AddComponent = tk.Button(self.Add_Semi, text='Add', font=14, bg='#0052cc', fg='white'
                                    )
        self.AddComponent.place(height=40, width=80, x=15, y=445)

        self.ClearComponent = tk.Button(self.Add_Semi, text='Clear', font=14, bg='#0052cc', fg='white',
                                    )
        self.ClearComponent.place(height=40, width=80, x=110, y=445)

        self.UploadLink = tk.Button(self.Add_Semi, text='Upload Link', font=14, bg='#0052cc', fg='white',
                                    )
        self.UploadLink.place(height=40, width=100, x=205, y=445)

        self.UploadPdf = tk.Button(self.Add_Semi, text='Upload PDF', font=14, bg='#0052cc', fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        # Labelki

        self.AddTitle = tk.Label(self.Add_Semi, font=("Arial", 20), text="Add new item:", anchor='w',
                                 bg="green", fg='white')
        self.AddTitle.place(height=40, width=280, x=10, y=10)

        self.lName = tk.Label(self.Add_Semi, text="Name:", bg="green")
        self.lName.place(height=40, width=80, x=10, y=60)

        self.lGroup = tk.Label(self.Add_Semi, text="Group:", bg="green")
        self.lGroup.place(height=40, width=80, x=10, y=100)

        self.lSubCategory = tk.Label(self.Add_Semi, text="SubCategory:", bg="green")
        self.lSubCategory.place(height=40, width=80, x=10, y=140)

        self.lModel = tk.Label(self.Add_Semi, text="Model:", bg="green")
        self.lModel.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Add_Semi, text="Assembly:", bg="green")
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSize = tk.Label(self.Add_Semi, text="Size:", bg="green")
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lWhere = tk.Label(self.Add_Semi, text="Where:", bg="green")
        self.lWhere.place(height=40, width=80, x=10, y=300)

        self.lQuintity = tk.Label(self.Add_Semi, text="Quintity:",  bg="green")
        self.lQuintity.place(height=40, width=80, x=10, y=340)

        # Entry

        self.eName = ttk.Entry(self.Add_Semi, width=50)
        self.eName.place(height=20, width=230, x=100, y=70)

        self.eGroup = ttk.Combobox(self.Add_Semi, )#values=self.grupa)
        self.eGroup.place(height=20, width=230, x=100, y=110)

        self.eSubCategory = ttk.Combobox(self.Add_Semi, )#values=self.subcategorysemi)
        self.eSubCategory.place(height=20, width=230, x=100, y=150)

        self.eModel = ttk.Entry(self.Add_Semi, width=50)
        self.eModel.place(height=20, width=230, x=100, y=190)

        self.eAssembly = ttk.Combobox(self.Add_Semi, )#values=self.SposobMontazu)
        self.eAssembly.place(height=20, width=230, x=100, y=230)

        self.eSize = ttk.Entry(self.Add_Semi, width=50)
        self.eSize.place(height=20, width=230, x=100, y=270)

        self.eWhere = ttk.Entry(self.Add_Semi, width=50)
        self.eWhere.place(height=20, width=230, x=100, y=310)

        self.eQuintity = ttk.Entry(self.Add_Semi, width=50)
        self.eQuintity.place(height=20, width=230, x=100, y=350)

        # Wejscia link i dokumenty i obrazy

        self.Link = tk.Label(self.Add_Semi, text="Tutaj będzie link", bg="green")
        self.Link.place(height=40, width=180, x=360, y=340)

        self.Obraz = ttk.Button(self.Add_Semi, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=360, y=70)


class AddEquipmentPassiveElements:
    def __init__(self, master):
        print("dwa")
        self.Add_Semi = tk.Frame(master, bg="white")
        self.Add_Semi.place(x=0, y=0, height=610, width=850)

        self.AddPassive = tk.Button(self.Add_Semi, text='Add', font=14, bg='#0052cc', fg='white')
        self.AddPassive.place(height=40, width=80, x=15, y=520)

        self.ClearPassive = tk.Button(self.Add_Semi, text='Clear', font=14, bg='#0052cc', fg='white')
        self.ClearPassive.place(height=40, width=80, x=110, y=520)

        self.UploadLinkPassive = tk.Button(self.Add_Semi, text='Upload Link', font=14, bg='#0052cc', fg='white')
        self.UploadLinkPassive.place(height=40, width=100, x=205, y=520)

        self.UploadPdfPassive = tk.Button(self.Add_Semi, text='Upload PDF', font=14, bg='#0052cc', fg='white')
        self.UploadPdfPassive.place(height=40, width=100, x=320, y=520)

        # Labelki

        self.AddTitlePassive = tk.Label(self.Add_Semi, font=("Arial", 20), text="Add new item:", anchor='w',
                                        bg="yellow", fg='white')
        self.AddTitlePassive.place(height=40, width=280, x=10, y=10)

        self.lNamePassive = tk.Label(self.Add_Semi, text="Name:", bg="yellow")
        self.lNamePassive.place(height=40, width=80, x=10, y=60)

        self.lGroupPassive = tk.Label(self.Add_Semi, text="Group:", bg="yellow")
        self.lGroupPassive.place(height=40, width=80, x=10, y=100)

        self.lSubCategoryPassive = tk.Label(self.Add_Semi, text="SubCategory:", bg="yellow")
        self.lSubCategoryPassive.place(height=40, width=80, x=10, y=140)

        self.lModelPassive = tk.Label(self.Add_Semi, text="Model:", bg="yellow")
        self.lModelPassive.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Add_Semi, text="Assembly:", bg="yellow")
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSizePassive = tk.Label(self.Add_Semi, text="Size:", bg="yellow")
        self.lSizePassive.place(height=40, width=80, x=10, y=260)

        self.lValuePassive = tk.Label(self.Add_Semi, text="Value:", bg="yellow")
        self.lValuePassive.place(height=40, width=80, x=10, y=300)

        self.lTolerancePassive = tk.Label(self.Add_Semi, text="Tolerance:", bg="yellow")
        self.lTolerancePassive.place(height=40, width=80, x=10, y=340)

        self.lWatsPassive = tk.Label(self.Add_Semi, text="Wats:", bg="yellow")
        self.lWatsPassive.place(height=40, width=80, x=10, y=380)

        self.lWherePassive = tk.Label(self.Add_Semi, text="Where:", bg="yellow")
        self.lWherePassive.place(height=40, width=80, x=10, y=420)

        self.lQuintityPassive = tk.Label(self.Add_Semi, text="Quintity:", bg="yellow")
        self.lQuintityPassive.place(height=40, width=80, x=10, y=460)


        # Wejscia

        self.eNamePassive = ttk.Entry(self.Add_Semi, width=50)
        self.eNamePassive.place(height=20, width=230, x=100, y=70)

        self.eGroupPassive = ttk.Combobox(self.Add_Semi, )
        self.eGroupPassive.place(height=20, width=230, x=100, y=110)

        self.eSubCategoryPassive = ttk.Combobox(self.Add_Semi, )
        self.eSubCategoryPassive.place(height=20, width=230, x=100, y=150)

        self.eModelPassive = ttk.Entry(self.Add_Semi, width=50)
        self.eModelPassive.place(height=20, width=230, x=100, y=190)

        self.eAssemblyPassive = ttk.Combobox(self.Add_Semi,)
        self.eAssemblyPassive.place(height=20, width=230, x=100, y=230)

        self.eSizePassive = ttk.Entry(self.Add_Semi, width=50)
        self.eSizePassive.place(height=20, width=230, x=100, y=270)

        self.eValuePassive = ttk.Entry(self.Add_Semi, width=50)
        self.eValuePassive.place(height=20, width=230, x=100, y=310)

        self.eTolerancePassive = ttk.Entry(self.Add_Semi, width=50)
        self.eTolerancePassive.place(height=20, width=230, x=100, y=350)

        self.eWatsPassive = ttk.Entry(self.Add_Semi, width=50)
        self.eWatsPassive.place(height=20, width=230, x=100, y=390)

        self.eWherePassive = ttk.Entry(self.Add_Semi, width=50)
        self.eWherePassive.place(height=20, width=230, x=100, y=430)

        self.eQuintityPassive = ttk.Entry(self.Add_Semi, width=50)
        self.eQuintityPassive.place(height=20, width=230, x=100, y=470)
