import tkinter as tk
import Colors as Col
import classes as cl
from tkinter import ttk
import categories as cat


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
        self.Machines.bind("<Button-1>",  lambda x: self.machines())

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

        self.Item_Name = tk.Label(self.ItemF, text="Item name:", anchor='w')
        self.Item_Name.place(height=40, width=70, x=10, y=40)

        self.Search = tk.Entry(self.ItemF, width=30)
        self.Search.place(height=30, width=150, x=115, y=50)

        self.GroupSearch = ttk.Combobox(self.ItemF, values=find_group.Group)
        self.GroupSearch.bind("<Button-1>", self.clear_categories)
        self.GroupSearch.place(height=30, width=150, x=285, y=50)

        self.Category2 = ttk.Combobox(self.ItemF)
        self.Category2.bind("<Button-1>", self.find_categories)
        self.Category2.place(height=30, width=150, x=455, y=50)

    def clear_categories(self, *args):
        self.Category2.delete(0, tk.END)

    def find_categories(self, *args):
        group = self.GroupSearch.get()
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
