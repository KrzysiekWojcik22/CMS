import tkinter as tk
import classes as cl
from tkinter import ttk
import Colors as Col

Color = Col.ColoursMainWindow()


class StartPage:
    def __init__(self, master):
        self.Start_Page = tk.Frame(master, bg=Color.FrameBackground)
        self.Start_Page.place(x=0, y=0, height=620, width=850)



