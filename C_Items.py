import tkinter as tk
import Colors as Col
import classes as cl
from tkinter import ttk

Color = Col.ColoursMainWindow()


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

        self.ShowItems.bind("<Enter>", cl.click)
        self.ShowItems.bind("<Leave>", cl.zwolnienie)
        self.ShowItems.bind("<Button-1>")

        self.Suppliers.bind("<Enter>", cl.click)
        self.Suppliers.bind("<Leave>", cl.zwolnienie)
        self.Suppliers.bind()

        self.Machines.bind("<Enter>", cl.click)
        self.Machines.bind("<Leave>", cl.zwolnienie)
        self.Machines.bind()

        self.Calibration.bind("<Enter>", cl.click)
        self.Calibration.bind("<Leave>", cl.zwolnienie)
        self.Calibration.bind()

        self.Doc.bind("<Enter>", cl.click)
        self.Doc.bind("<Leave>", cl.zwolnienie)
        self.Doc.bind()

    def items(self):
        pass

    def Suppliers(self):
        pass
    def Calibration(self):
        pass
    def Doc(self):
        pass


class ItemsC:
    def __init__(self, master):
        self.ItemF = tk.Frame(master, bg="black")
        self.ItemF.place(x=0, y=0, height=610, width=850)