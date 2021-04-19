import tkinter as tk
from tkinter import ttk
import classes as cl
import Colors as Col

Color = Col.ColoursMainWindow()


class AddEquipmentFirst:
    def __init__(self, master):
        self.Add_EQ = tk.Frame(master)
        self.Add_EQ.place(x=0, y=0, height=610, width=850)

        self.PadAdd1 = tk.PanedWindow(self.Add_EQ, bg=Color.FrameMenu, handlepad=True)
        self.PadAdd1.place(height=700, width=140, x=0, y=0)

        self.PadAdd2 = tk.PanedWindow(self.Add_EQ, bg=Color.FrameBackground)
        self.PadAdd2.place(height=640, width=720, x=140, y=0)

        # Tworzenie widgetów dla Padd1

        self.Sep1Pad1 = ttk.Separator(self.PadAdd1, orient='horizontal')
        self.Sep1Pad1.place(width=130, x=5, y=40)

        self.AddComponent = tk.Label(self.PadAdd1, font=("Arial", 13), bg=Color.Buttons_Background, fg='white',
                                     text="Choose a type")
        self.AddComponent.place(width=120, height=40, x=5, y=0)

        # Funkcje dla pad 1

        self.AddSemiconductors = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                          anchor="w", text="Semiconductors", cursor="hand2")
        self.AddSemiconductors.place(width=110, height=40, x=15, y=50)

        self.AddPassiveElements = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                           anchor="w", text="PassiveElements", cursor="hand2")
        self.AddPassiveElements.place(width=110, height=40, x=15, y=100)

        self.AddOptoelectronic = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                          anchor="w", text="Optoelectronic", cursor="hand2")
        self.AddOptoelectronic.place(width=110, height=40, x=15, y=150)

        self.AddOptoelectronic = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                          anchor="w", text="Optoelectronic", cursor="hand2")
        self.AddOptoelectronic.place(width=110, height=40, x=15, y=150)

        self.AddConnectors = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                      anchor="w", text="Connectors", cursor="hand2")
        self.AddConnectors.place(width=110, height=40, x=15, y=200)

        self.AddEnergySources = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                         anchor="w", text="EnergySources", cursor="hand2")
        self.AddEnergySources.place(width=110, height=40, x=15, y=250)

        self.AddPCAccesories = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                        anchor="w", text="PCAccesories", cursor="hand2")
        self.AddPCAccesories.place(width=110, height=40, x=15, y=300)

        self.AddSwitches = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                    anchor="w", text="Switches", cursor="hand2")
        self.AddSwitches.place(width=110, height=40, x=15, y=350)

        self.AddWires = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                 anchor="w", text="Wires", cursor="hand2")
        self.AddWires.place(width=110, height=40, x=15, y=400)

        self.AddMechanics = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                     anchor="w", text="Mechanics", cursor="hand2")
        self.AddMechanics.place(width=110, height=40, x=15, y=450)

        self.AddLaboratory = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                      anchor="w", text="Laboratory", cursor="hand2")
        self.AddLaboratory.place(width=110, height=40, x=15, y=500)

        self.AddOthers = tk.Label(self.PadAdd1, font=("Arial", 10), bg=Color.Buttons_Background, fg='white',
                                  anchor="w", text="Others", cursor="hand2")
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
        self.AddConnectors.bind("<Button-1>", lambda x: self.add_connectors())

        self.AddEnergySources.bind("<Enter>", cl.click)
        self.AddEnergySources.bind("<Leave>", cl.zwolnienie)
        self.AddEnergySources.bind("<Button-1>", lambda x: self.add_energy_sources())

        self.AddPCAccesories.bind("<Enter>", cl.click)
        self.AddPCAccesories.bind("<Leave>", cl.zwolnienie)
       # self.AddPCAccesories.bind("<Button-1>", showPCAccessories)

        self.AddSwitches.bind("<Enter>", cl.click)
        self.AddSwitches.bind("<Leave>", cl.zwolnienie)
        #self.AddSwitches.bind("<Button-1>", showSwitches)

        self.AddWires.bind("<Enter>", cl.click)
        self.AddWires.bind("<Leave>", cl.zwolnienie)
        self.AddWires.bind("<Button-1>", lambda x: self.add_wires())

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
        AddConnectors(master=self.PadAdd2)

    def add_energy_sources(self):
        print("Hello")
        AddEnergySources(master=self.PadAdd2)

    def add_wires(self):
        AddWires(master=self.PadAdd2)


class AddEquipmentSemiconductors:
    def __init__(self, master):
        self.Add_Semi = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Semi.place(x=0, y=0, height=610, width=850)

        self.AddComponent = tk.Button(self.Add_Semi, text='Add', font=14, bg=Color.WidgetButtons, fg='white'
                                    )
        self.AddComponent.place(height=40, width=80, x=15, y=445)

        self.ClearComponent = tk.Button(self.Add_Semi, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                    )
        self.ClearComponent.place(height=40, width=80, x=110, y=445)

        self.UploadLink = tk.Button(self.Add_Semi, text='Upload Link', font=14, bg=Color.WidgetButtons, fg='white',
                                    )
        self.UploadLink.place(height=40, width=100, x=205, y=445)

        self.UploadPdf = tk.Button(self.Add_Semi, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        # Labelki

        self.AddTitle = tk.Label(self.Add_Semi, font=("Arial", 20), text="Add new item:", anchor='w',
                                 bg=Color.FrameBackground, fg='white')
        self.AddTitle.place(height=40, width=280, x=10, y=10)

        self.lName = tk.Label(self.Add_Semi, text="Name:", bg=Color.FrameBackground)
        self.lName.place(height=40, width=80, x=10, y=60)

        self.lGroup = tk.Label(self.Add_Semi, text="Group:", bg=Color.FrameBackground)
        self.lGroup.place(height=40, width=80, x=10, y=100)

        self.lSubCategory = tk.Label(self.Add_Semi, text="SubCategory:", bg=Color.FrameBackground)
        self.lSubCategory.place(height=40, width=80, x=10, y=140)

        self.lModel = tk.Label(self.Add_Semi, text="Model:", bg=Color.FrameBackground)
        self.lModel.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Add_Semi, text="Assembly:", bg=Color.FrameBackground)
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSize = tk.Label(self.Add_Semi, text="Size:", bg=Color.FrameBackground)
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lWhere = tk.Label(self.Add_Semi, text="Where:", bg=Color.FrameBackground)
        self.lWhere.place(height=40, width=80, x=10, y=300)

        self.lQuintity = tk.Label(self.Add_Semi, text="Quantity:",  bg=Color.FrameBackground)
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

        self.Link = tk.Label(self.Add_Semi, text="Tutaj będzie link", bg=Color.FrameBackground)
        self.Link.place(height=40, width=180, x=360, y=340)

        self.Obraz = ttk.Button(self.Add_Semi, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=360, y=70)


class AddEquipmentPassiveElements:
    def __init__(self, master):
        self.Add_Passive = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Passive.place(x=0, y=0, height=610, width=850)

        self.AddPassive = tk.Button(self.Add_Passive, text='Add', font=14, bg=Color.Buttons_Background,
                                    fg='white')
        self.AddPassive.place(height=40, width=80, x=15, y=520)

        self.ClearPassive = tk.Button(self.Add_Passive, text='Clear', font=14, bg=Color.Buttons_Background,
                                      fg='white')
        self.ClearPassive.place(height=40, width=80, x=110, y=520)

        self.UploadLinkPassive = tk.Button(self.Add_Passive, text='Upload Link', font=14, bg=Color.Buttons_Background,
                                           fg='white')
        self.UploadLinkPassive.place(height=40, width=100, x=205, y=520)

        self.UploadPdfPassive = tk.Button(self.Add_Passive, text='Upload PDF', font=14, bg=Color.Buttons_Background,
                                          fg='white')
        self.UploadPdfPassive.place(height=40, width=100, x=320, y=520)

        # Labelki

        self.AddTitlePassive = tk.Label(self.Add_Passive, font=("Arial", 20), text="Add new item:", anchor='w',
                                        bg=Color.FrameBackground, fg='white')
        self.AddTitlePassive.place(height=40, width=280, x=10, y=10)

        self.lNamePassive = tk.Label(self.Add_Passive, text="Name:", bg=Color.FrameBackground)
        self.lNamePassive.place(height=40, width=80, x=10, y=60)

        self.lGroupPassive = tk.Label(self.Add_Passive, text="Group:", bg=Color.FrameBackground)
        self.lGroupPassive.place(height=40, width=80, x=10, y=100)

        self.lSubCategoryPassive = tk.Label(self.Add_Passive, text="SubCategory:", bg=Color.FrameBackground)
        self.lSubCategoryPassive.place(height=40, width=80, x=10, y=140)

        self.lModelPassive = tk.Label(self.Add_Passive, text="Model:", bg=Color.FrameBackground)
        self.lModelPassive.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Add_Passive, text="Assembly:", bg=Color.FrameBackground)
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSizePassive = tk.Label(self.Add_Passive, text="Size:", bg=Color.FrameBackground)
        self.lSizePassive.place(height=40, width=80, x=10, y=260)

        self.lValuePassive = tk.Label(self.Add_Passive, text="Value:", bg=Color.FrameBackground)
        self.lValuePassive.place(height=40, width=80, x=10, y=300)

        self.lTolerancePassive = tk.Label(self.Add_Passive, text="Tolerance:", bg=Color.FrameBackground)
        self.lTolerancePassive.place(height=40, width=80, x=10, y=340)

        self.lWatsPassive = tk.Label(self.Add_Passive, text="Wats:", bg=Color.FrameBackground)
        self.lWatsPassive.place(height=40, width=80, x=10, y=380)

        self.lWherePassive = tk.Label(self.Add_Passive, text="Where:", bg=Color.FrameBackground)
        self.lWherePassive.place(height=40, width=80, x=10, y=420)

        self.lQuantityPassive = tk.Label(self.Add_Passive, text="Quantity:", bg=Color.FrameBackground)
        self.lQuantityPassive.place(height=40, width=80, x=10, y=460)


        # Wejscia

        self.eNamePassive = ttk.Entry(self.Add_Passive, width=50)
        self.eNamePassive.place(height=20, width=230, x=100, y=70)

        self.eGroupPassive = ttk.Combobox(self.Add_Passive, )
        self.eGroupPassive.place(height=20, width=230, x=100, y=110)

        self.eSubCategoryPassive = ttk.Combobox(self.Add_Passive, )
        self.eSubCategoryPassive.place(height=20, width=230, x=100, y=150)

        self.eModelPassive = ttk.Entry(self.Add_Passive, width=50)
        self.eModelPassive.place(height=20, width=230, x=100, y=190)

        self.eAssemblyPassive = ttk.Combobox(self.Add_Passive,)
        self.eAssemblyPassive.place(height=20, width=230, x=100, y=230)

        self.eSizePassive = ttk.Entry(self.Add_Passive, width=50)
        self.eSizePassive.place(height=20, width=230, x=100, y=270)

        self.eValuePassive = ttk.Entry(self.Add_Passive, width=50)
        self.eValuePassive.place(height=20, width=230, x=100, y=310)

        self.eTolerancePassive = ttk.Entry(self.Add_Passive, width=50)
        self.eTolerancePassive.place(height=20, width=230, x=100, y=350)

        self.eWatsPassive = ttk.Entry(self.Add_Passive, width=50)
        self.eWatsPassive.place(height=20, width=230, x=100, y=390)

        self.eWherePassive = ttk.Entry(self.Add_Passive, width=50)
        self.eWherePassive.place(height=20, width=230, x=100, y=430)

        self.eQuantityPassive = ttk.Entry(self.Add_Passive, width=50)
        self.eQuantityPassive.place(height=20, width=230, x=100, y=470)


class AddConnectors:
    def __init__(self, master):
        self.Add_Con = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Con.place(x=0, y=0, height=610, width=850)

        ### BUTTONS

        self.AddCon = tk.Button(self.Add_Con, text='Add', font=14, bg=Color.WidgetButtons, fg='white'
                                      )
        self.AddCon.place(height=40, width=80, x=15, y=445)

        self.ClearCon = tk.Button(self.Add_Con, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                        )
        self.ClearCon.place(height=40, width=80, x=110, y=445)

        self.UploadLink = tk.Button(self.Add_Con, text='Upload Link', font=14, bg=Color.WidgetButtons, fg='white',
                                    )
        self.UploadLink.place(height=40, width=100, x=205, y=445)

        self.UploadPdf = tk.Button(self.Add_Con, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        ### Labels

        self.AddTitleCon = tk.Label(self.Add_Con, font=("Arial", 20), text="Add new item:", anchor='w',
                                 bg=Color.FrameBackground, fg='white')
        self.AddTitleCon.place(height=40, width=280, x=10, y=10)

        self.lNameCon = tk.Label(self.Add_Con, text="Name:", bg=Color.FrameBackground)
        self.lNameCon.place(height=40, width=80, x=10, y=60)

        self.lGroupCon = tk.Label(self.Add_Con, text="Group:", bg=Color.FrameBackground)
        self.lGroupCon.place(height=40, width=80, x=10, y=100)

        self.lSubCategoryCon = tk.Label(self.Add_Con, text="SubCategory:", bg=Color.FrameBackground)
        self.lSubCategoryCon.place(height=40, width=80, x=10, y=140)

        self.lModelCon = tk.Label(self.Add_Con, text="Model:", bg=Color.FrameBackground)
        self.lModelCon.place(height=40, width=80, x=10, y=180)

        self.lAssemblyCon = tk.Label(self.Add_Con, text="Assembly:", bg=Color.FrameBackground)
        self.lAssemblyCon.place(height=40, width=80, x=10, y=220)

        self.lBrandCon = tk.Label(self.Add_Con, text="Brand:", bg=Color.FrameBackground)
        self.lBrandCon.place(height=40, width=80, x=10, y=260)

        self.lWhereCon = tk.Label(self.Add_Con, text="Where:", bg=Color.FrameBackground)
        self.lWhereCon.place(height=40, width=80, x=10, y=300)

        self.lQuintityCon = tk.Label(self.Add_Con, text="Quantity:", bg=Color.FrameBackground)
        self.lQuintityCon.place(height=40, width=80, x=10, y=340)

        ### Enters


class AddEnergySources:
    def __init__(self, master):
        self.Add_Energy = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Energy.place(x=0, y=0, height=610, width=850)

        #### BUTTONS

        self.AddEnergy = tk.Button(self.Add_Energy, text='Add', font=14, bg=Color.WidgetButtons, fg='white'
                                      )
        self.AddEnergy.place(height=40, width=80, x=15, y=445)

        self.ClearEnergy = tk.Button(self.Add_Energy, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                        )
        self.ClearEnergy.place(height=40, width=80, x=110, y=445)

        self.UploadLink = tk.Button(self.Add_Energy, text='Upload Link', font=14, bg=Color.WidgetButtons, fg='white',
                                    )
        self.UploadLink.place(height=40, width=100, x=205, y=445)

        self.UploadPdf = tk.Button(self.Add_Energy, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        ### Labels

        self.AddTitle = tk.Label(self.Add_Energy, font=("Arial", 20), text="Add new item:", anchor='w',
                                 bg=Color.FrameBackground, fg='white')
        self.AddTitle.place(height=40, width=280, x=10, y=10)

        self.lName = tk.Label(self.Add_Energy, text="Name:", bg=Color.FrameBackground)
        self.lName.place(height=40, width=80, x=10, y=60)

        self.lGroup = tk.Label(self.Add_Energy, text="Group:", bg=Color.FrameBackground)
        self.lGroup.place(height=40, width=80, x=10, y=100)

        self.lSubCategory = tk.Label(self.Add_Energy, text="SubCategory:", bg=Color.FrameBackground)
        self.lSubCategory.place(height=40, width=80, x=10, y=140)

        self.lModel = tk.Label(self.Add_Energy, text="Model:", bg=Color.FrameBackground)
        self.lModel.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Add_Energy, text="Assembly:", bg=Color.FrameBackground)
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSize = tk.Label(self.Add_Energy, text="Size:", bg=Color.FrameBackground)
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lWhere = tk.Label(self.Add_Energy, text="Where:", bg=Color.FrameBackground)
        self.lWhere.place(height=40, width=80, x=10, y=300)

        self.lQuintity = tk.Label(self.Add_Energy, text="Quintity:", bg=Color.FrameBackground)
        self.lQuintity.place(height=40, width=80, x=10, y=340)

        ### Enters


class AddWires:
    def __init__(self, master):
        self.Add_Wires = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Wires.place(x=0, y=0, height=610, width=850)

        ### BUTTONS

        self.AddWires = tk.Button(self.Add_Wires, text='Add', font=14, bg=Color.WidgetButtons, fg='white'
                                      )
        self.AddWires.place(height=40, width=80, x=15, y=445)

        self.ClearWires = tk.Button(self.Add_Wires, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                        )
        self.ClearWires.place(height=40, width=80, x=110, y=445)

        self.UploadLink = tk.Button(self.Add_Wires, text='Upload Link', font=14, bg=Color.WidgetButtons, fg='white',
                                    )
        self.UploadLink.place(height=40, width=100, x=205, y=445)

        self.UploadPdf = tk.Button(self.Add_Wires, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        ### Labels

        self.AddTitle = tk.Label(self.Add_Wires, font=("Arial", 20), text="Add new item:", anchor='w',
                                 bg=Color.FrameBackground, fg='white')
        self.AddTitle.place(height=40, width=280, x=10, y=10)

        self.lName = tk.Label(self.Add_Wires, text="Name:", bg=Color.FrameBackground)
        self.lName.place(height=40, width=80, x=10, y=60)

        self.lGroup = tk.Label(self.Add_Wires, text="Group:", bg=Color.FrameBackground)
        self.lGroup.place(height=40, width=80, x=10, y=100)

        self.lSubCategory = tk.Label(self.Add_Wires, text="SubCategory:", bg=Color.FrameBackground)
        self.lSubCategory.place(height=40, width=80, x=10, y=140)

        self.lModel = tk.Label(self.Add_Wires, text="Model:", bg=Color.FrameBackground)
        self.lModel.place(height=40, width=80, x=10, y=180)

        self.lAssembly = tk.Label(self.Add_Wires, text="Assembly:", bg=Color.FrameBackground)
        self.lAssembly.place(height=40, width=80, x=10, y=220)

        self.lSize = tk.Label(self.Add_Wires, text="Size:", bg=Color.FrameBackground)
        self.lSize.place(height=40, width=80, x=10, y=260)

        self.lWhere = tk.Label(self.Add_Wires, text="Where:", bg=Color.FrameBackground)
        self.lWhere.place(height=40, width=80, x=10, y=300)

        self.lQuintity = tk.Label(self.Add_Wires, text="Quintity:", bg=Color.FrameBackground)
        self.lQuintity.place(height=40, width=80, x=10, y=340)

        ### Enters