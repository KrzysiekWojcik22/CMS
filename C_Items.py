import tkinter as tk
import Colors as Col
import classes as cl
import DataBaseOperation
import categories as cat
import MySQLdb
from tkinter import ttk
from mysql.connector import errorcode
import mysql.connector

Color = Col.ColoursMainWindow()
Cat_Semi = cat.EquipmentCategoriesSemiconductors()
Cat_Passive = cat.EquipmentCategoriesPassiveElements()
Cat_Opto = cat.EquipmentCategoriesOptoElectronics()
Cat_Connectors = cat.EquipmentCategoriesConnectors()
Cat_Energy = cat.EquipmentCategoriesEnergySources()
Cat_PC = cat.EquipmentCategoriesPCAccessories()
Cat_Switches = cat.EquipmentCategoriesSwitches()
Cat_Wires = cat.EquipmentCategoriesWires()
Cat_Mechanics = cat.EquipmentCategoriesMechanics()
Cat_Lab = cat.EquipmentCategoriesLaboratory()
Cat_Others = cat.EquipmentCategoriesOthers()
find_group = cat.SearchEquipmentGroup()


class Items:
    def __init__(self, master):
        self.Item = tk.Frame(master)
        self.Item.place(x=0, y=0, height=610, width=850)

        self.Item_1 = tk.PanedWindow(self.Item, bg=Color.FrameMenu)
        self.Item_1.place(height=700, width=140, x=0, y=0)

        self.Item_2 = tk.PanedWindow(self.Item, bg=Color.FrameBackground)
        self.Item_2.place(height=640, width=720, x=140, y=0)

        self.Sep1Pad1 = ttk.Separator(self.Item_1, orient='horizontal')
        self.Sep1Pad1.place(width=130, x=5, y=40)

        self.Item_Title = tk.Label(self.Item_1, text="Item")
        self.Item_Title.place(width=110, height=30, x=15, y=5)

        self.ShowItems = tk.Label(self.Item_1, text="Product Catalog", bg=Color.Labels_Background_FrameMenu,
                                  fg=Color.Labels_Foreground_FrameMenu, anchor="w", cursor="hand2")
        self.ShowItems.place(width=110, height=40, x=15, y=50)

        self.Suppliers = tk.Label(self.Item_1, text="Suppliers", bg=Color.Labels_Background_FrameMenu,
                                  fg=Color.Labels_Foreground_FrameMenu, anchor="w", cursor="hand2")
        self.Suppliers.place(width=110, height=40, x=15, y=100)

        self.Machines = tk.Label(self.Item_1, text="Machines", bg=Color.Labels_Background_FrameMenu,
                                 fg=Color.Labels_Foreground_FrameMenu, anchor="w", cursor="hand2")
        self.Machines.place(width=110, height=40, x=15, y=150)

        self.Calibration = tk.Label(self.Item_1, text="Calibration", bg=Color.Labels_Background_FrameMenu,
                                    fg=Color.Labels_Foreground_FrameMenu, anchor="w", cursor="hand2")
        self.Calibration.place(width=110, height=40, x=15, y=200)

        self.Doc = tk.Label(self.Item_1, text="Doc:", bg=Color.Labels_Background_FrameMenu,
                            fg=Color.Labels_Foreground_FrameMenu, anchor="w", cursor="hand2")
        self.Doc.place(width=110, height=40, x=15, y=250)

        ItemsC(master=self.Item_2)

        self.ShowItems.bind("<Enter>", cl.click)
        self.ShowItems.bind("<Leave>", cl.zwolnienie)
        self.ShowItems.bind("<Button-1>", lambda x: self.items())

        self.Suppliers.bind("<Enter>", cl.click)
        self.Suppliers.bind("<Leave>", cl.zwolnienie)
        self.Suppliers.bind("<Button-1>", lambda x: self.suppliers())

        self.Machines.bind("<Enter>", cl.click)
        self.Machines.bind("<Leave>", cl.zwolnienie)
        self.Machines.bind("<Button-1>", lambda x: self.machines())

        self.Calibration.bind("<Enter>", cl.click)
        self.Calibration.bind("<Leave>", cl.zwolnienie)
        self.Calibration.bind("<Button-1>", lambda x: self.calibration())

        self.Doc.bind("<Enter>", cl.click)
        self.Doc.bind("<Leave>", cl.zwolnienie)
        self.Doc.bind("<Button-1>", lambda x: self.doc())

    def items(self):
        ItemsC(master=self.Item_2)

    def suppliers(self):
        SuppliersC(master=self.Item_2)

    def machines(self):
        MachinesC(master=self.Item_2)

    def calibration(self):
        CalibrationC(master=self.Item_2)

    def doc(self):
        DocumentsC(master=self.Item_2)


class ItemsC:
    def __init__(self, master):

        self.ItemF = tk.Frame(master, bg="gray")
        self.ItemF.place(x=-1, y=-1, height=610, width=850)

        self.TitleFrame = tk.Canvas(self.ItemF, bg='blue', height=90, width=722)
        self.TitleFrame.create_rectangle(-1, 41, 722, 94, fill='#004554', outline='#004554')
        self.TitleFrame.tag_raise(0)
        self.TitleFrame.place(x=-2, y=-2)

        self.Title = tk.Label(self.ItemF, text="Search for the item:", anchor='w')
        self.Title.place(height=40, width=180, x=10, y=0)

        self.Search = tk.Entry(self.ItemF, width=30)
        self.Search.place(height=20, width=150, x=10, y=55)

        self.GroupSearch = ttk.Combobox(self.ItemF, values=find_group.Group)
        self.GroupSearch.bind("<Button-1>", self.clear_categories)
        self.GroupSearch.place(height=20, width=150, x=180, y=55)

        self.Category2 = ttk.Combobox(self.ItemF)
        self.Category2.bind("<Button-1>", self.find_groups)
        self.Category2.place(height=20, width=150, x=350, y=55)

        self.Category3 = ttk.Combobox(self.ItemF)
        self.Category3.bind("<Button-1>", self.find_categories)
        self.Category3.place(height=20, width=180, x=520, y=55)

        self.Search_item = tk.Button(self.ItemF, text="Search", compound=tk.LEFT, command=self.search)
        self.Search_item.place(height=30, width=100, x=600, y=5)
        scrollbar = tk.Scrollbar(self.ItemF,)
        scrollbar.place(height=100, width=30, x=620, y=100)
        self.tree = ttk.Treeview(self.ItemF, columns=("ID", "User Name","email","supervisor"))
        self.tree.place(height=400, width=600, x=15, y=100)
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='email')
        self.tree.heading('#3', text='supervisor')
        self.tree.heading('#4', text='role')
        self.tree.column('#0', stretch=tk.NO)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
        self.id = 1
        self.iid = 0


    def clear_categories(self, *args):
        self.Category2.delete(0, tk.END)
        self.Category3.delete(0, tk.END)

    def find_groups(self, *args):
        group = self.GroupSearch.get()
        self.Category3.delete(0, tk.END)

        if group == "All":
            self.Category2.config(values="tak")
        elif group == "Semiconductors":
            self.Category2.config(values=Cat_Semi.SemiCat)
        elif group == "Passive elements":
            self.Category2.config(values=Cat_Passive.PassiveElementsGroup)
        elif group == "Optoelectronic":
            self.Category2.config(values=Cat_Opto.Opto_Group)
        elif group == "Connector":
            self.Category2.config(values=Cat_Connectors.Connectors_group)
        elif group == "Energy Sources":
            self.Category2.config(values="tak")
        elif group == "PC accessories":
            self.Category2.config(values=Cat_PC.Computer_Accessories)
        elif group == "Switches":
            self.Category2.config(values=Cat_Switches.Switches_Group)
        elif group == "Wires":
            self.Category2.config(values=Cat_Wires.Wires_group)
        elif group == "Mechanics":
            self.Category2.config(values=Cat_Mechanics.Mechanics)
        elif group == "Laboratory":
            self.Category2.config(values=Cat_Lab.Tools)
        elif group == "Others":
            self.Category2.config(values="tak")

    def find_categories(self, *args):
        category2 = self.Category2.get()

        if category2 == "Diodes":
            self.Category3.config(values=Cat_Semi.Diodes)
        elif category2 == "Thyristors":
            self.Category3.config(values=Cat_Semi.Thyristors)
        elif category2 == "Triacs":
            self.Category3.config(values=Cat_Semi.Triacs)
        elif category2 == "Diacs":
            self.Category3.config(values=Cat_Semi.Diacs)
        elif category2 == "Transistors":
            self.Category3.config(values=Cat_Semi.Transistors)
        elif category2 == "Integrated circuits":
            self.Category3.config(values=Cat_Semi.Integrated_circuits)

        elif category2 == 'Resistors':
            self.Category3.config(values=Cat_Passive.Resistors)
        elif category2 == 'Capacitors':
            self.Category3.config(values=Cat_Passive.Capacitors)
        elif category2 == 'Inductors':
            self.Category3.config(values=Cat_Passive.Inductors)
        elif category2 == 'EMI EMC components':
            self.Category3.config(values=Cat_Passive.EMI_EMC_components)
        elif category2 == 'Quartz crystals and filters':
            self.Category3.config(values=Cat_Passive.Quartz_crystals_and_filters)
        elif category2 == 'Potentiometers':
            self.Category3.config(values=Cat_Passive.Potentiometers)
        elif category2 == 'Encoders':
            self.Category3.config(values=Cat_Passive.Encoders)
        elif category2 == 'NTC thermistors':
            self.Category3.config(values=Cat_Passive.NTC_thermistors)

    def search(self):

        group = self.GroupSearch.get()
        category = self.Category2.get()
        category2 = self.Category3.get()

        print(group)
        print(category)
        print(category2)
        mydb = MySQLdb.connect(host="10.224.20.18", port=3306, user="Krzysiek",
                               password="start123", database="CMS")
        self.__connection = mydb
        self.__session = mydb.cursor()

        all = ("Select * from CMS.Users")

        self.__session.execute(all)
        all1 = self.__session.fetchall()


        cpt=0
        for row in all1:
            self.tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4]))
            cpt += 1  # increment the ID




        self.__connection.commit()

        self.__session.close()
        self.__connection.close()


class SuppliersC:
    def __init__(self, master):
        self.ItemF = tk.Frame(master, bg="red")
        self.ItemF.place(x=-1, y=-1, height=610, width=850)


class MachinesC:
    def __init__(self, master):
        self.machinesF = tk.Frame(master, bg='green')
        self.machinesF.place(x=-1, y=-1, height=610, width=850)


class CalibrationC:
    def __init__(self, master):
        self.ItemF = tk.Frame(master, bg="pink")
        self.ItemF.place(x=-1, y=-1, height=610, width=850)


class DocumentsC:
    def __init__(self, master):
        self.ItemF = tk.Frame(master, bg="yellow")
        self.ItemF.place(x=-1, y=-1, height=610, width=850)
