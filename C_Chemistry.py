import tkinter as tk
import Colors as Col
import classes as cl
from tkinter import ttk

Color = Col.ColoursMainWindow()


class Chemistry:
    def __init__(self, master, *args):
        self.Chemistry1 = tk.Frame(master)
        self.Chemistry1.place(x=0, y=0, height=620, width=850)

        self.Chem_1 = tk.PanedWindow(self.Chemistry1, bg=Color.FrameMenu)
        self.Chem_1.place(height=700, width=140, x=0, y=0)
        self.Chem_2 = tk.PanedWindow(self.Chemistry1, bg=Color.FrameBackground)
        self.Chem_2.place(height=640, width=720, x=140, y=0)

        self.Sep1Pad1 = ttk.Separator(self.Chem_1, orient='horizontal')
        self.Sep1Pad1.place(width=130, x=5, y=40)

        self.Material_Safety_Data_Sheet = tk.Label(self.Chem_1, text="Material Safety DS",
                                                   bg=Color.Labels_Background_FrameMenu, fg="white", anchor="w",
                                                   cursor="hand2")
        self.Material_Safety_Data_Sheet.place(width=110, height=40, x=15, y=50)

        self.Material_Safety_Doc_Word = tk.Label(self.Chem_1, text="Material Safety Doc",
                                                 bg=Color.Labels_Background_FrameMenu, fg="white", anchor="w",
                                                 cursor="hand2")
        self.Material_Safety_Doc_Word.place(width=110, height=40, x=15, y=100)

        self.Products = tk.Label(self.Chem_1, text="Products", bg=Color.Labels_Background_FrameMenu, fg="white",
                                 anchor="w", cursor="hand2")
        self.Products.place(width=110, height=40, x=15, y=150)

        self.NewChemistry = tk.Label(self.Chem_1, text="New Chemistry", bg=Color.Labels_Background_FrameMenu,
                                     fg="white", anchor="w", cursor="hand2")
        self.NewChemistry.place(width=110, height=40, x=15, y=200)

        ##### Bind

        self.Material_Safety_Data_Sheet.bind("<Enter>", cl.click)
        self.Material_Safety_Data_Sheet.bind("<Leave>", cl.zwolnienie)
        self.Material_Safety_Data_Sheet.bind("<Button-1>")

        self.Material_Safety_Doc_Word.bind("<Enter>", cl.click)
        self.Material_Safety_Doc_Word.bind("<Leave>", cl.zwolnienie)
        self.Material_Safety_Doc_Word.bind("<Button-1>")

        self.Products.bind("<Enter>", cl.click)
        self.Products.bind("<Leave>", cl.zwolnienie)
        self.Products.bind("<Button-1>")

        self.NewChemistry.bind("<Enter>", cl.click)
        self.NewChemistry.bind("<Leave>", cl.zwolnienie)
        self.NewChemistry.bind("<Button-1>")