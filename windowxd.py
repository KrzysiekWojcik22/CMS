import tkinter as tk
import classes as cl
import Colors as Col
from tkinter import ttk
from C_MakeOrder import MakeOrder
from C_Add import AddEquipmentFirst
from C_Help import Help
from C_Chemistry import Chemistry
from C_Items import Items
from C_Home import StartPage

Color = Col.ColoursMainWindow()


class MainWindow:
    def __init__(self, master):
        self.master = tk.Toplevel()
        self.master.overrideredirect(True)
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        root_width = 1045
        root_height = 720
        center_x = int(screen_width / 2 - root_width / 2)
        center_y = int(screen_height / 2 - root_height / 2)
        self.master.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        self.master.attributes('-topmost', True)
        self.master.configure(bg=Color.MainBackground)

        PasekGora = tk.Canvas(self.master, bg='grey', height=725, width=1050)  # Budowa tła niebieskie
        PasekGora.tag_raise(0)
        PasekGora.place(x=-2, y=-1.5)
        PasekGora.create_rectangle(0, 0, 1045, 56, fill='#004554', outline='#004554')
        PasekGora.create_rectangle(0, 57, 1050, 120, fill='#3C3E45', outline='#3C3E45')
        PasekGora.create_rectangle(0, 121, 200, 724, fill='#3C3E45', outline='#3C3E45')

        PasekGora.bind("<Button-1>", self.startMove)
        PasekGora.bind("<ButtonRelease-1>", self.stopMove)
        PasekGora.bind("<B1-Motion>", self.moving)
        PasekGora.bind("<Double-Button-1>", self.minimize)
        PasekGora.bind("<Map>", self.frame_mapped)

        ### icony

        Icons = cl.Icons(self.master)
        logo = Icons.myLabel
        logo.photo = Icons.my_img
        logo.place(x=10, y=2.5, height=48, width=48)


        ## Głowny interfejs

        self.rootTitle = tk.Label(self.master, text='Component Database Management',
                                  bg='#004554', fg='white', font=("Helvetica", 14),anchor="w")
        self.rootTitle.place(height=55, width=400, x=65, y=0)

        self.EP = tk.Label(self.master, font=("Arial", 12), bg=Color.MainBg_Label, fg='white',
                           text="Enterprise Park")
        self.EP.place(height=40, width=150, x=325, y=65)

        self.EQ = tk.Label(self.master, font=("Arial", 12), bg=Color.MainBg_Label, fg='white',
                           text="Technical Center")
        self.EQ.place(height=40, width=150, x=575, y=65)

        self.TCK = tk.Label(self.master, font=("Arial", 12), bg=Color.MainBg_Label, fg='white',
                            text="Equal Business Park")
        self.TCK.place(height=40, width=150, x=825, y=65)

        ### Separatory

        self.rootSep = ttk.Separator(self.master, orient='vertical')
        self.rootSep.place(width=150, x=15, y=130)

        self.rootSep2 = ttk.Separator(self.master, orient='vertical')
        self.rootSep2.place(width=150, x=15, y=650)

        ### glowne labelki

        self.ProjectL = tk.Label(self.master, font=("Arial", 40), bg='#3C3E45', fg='white', text="CMS")

        self.ProjectL.place(height=60, width=120, x=15, y=62.5)

        self.UsernameL = tk.Label(self.master, text='Krzysztof Wojcik',
                                  bg='#004554', fg='white', font=("Helvetica", 14))

        self.UsernameL.place(height=40, width=180, x=800, y=5)

        self.Designer = tk.Label(self.master, font=("Arial", 11), bg='#3C3E45', fg='white',
                                 text="Created by:\n Krzysztof Wójcik")
        self.Designer.place(height=60, width=140, x=15, y=655)

        ### Obramowanie i przyciski funkcyjne dla modern flat gui

        Close = tk.Label(self.master, font=("Arial", 11), anchor=tk.CENTER, bg='#0052cc', text="X", cursor="hand2")
        Close.tkraise(aboveThis=PasekGora)
        Close.place(x=990, y=0, width=55, height=55)

        ###Funkcje dla ramki

        Close.bind("<Enter>", cl.Hover)
        Close.bind("<Leave>", cl.Unhover)
        Close.bind("<Button-1>", lambda x: self.master.destroy())

        ### Tworzenie labelek z nazwami zmieniającymi kolor

        LHome = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Home", anchor="w",
                         cursor="hand2")
        LHome["compound"] = tk.LEFT
        LHome["image"] = Icons.home_ic
        LHome.tkraise(aboveThis=PasekGora)
        LHome.place(x=15, y=150, width=170, height=40)

        LAddEq = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Add Equipment", anchor="w",
                          cursor="hand2")
        LAddEq["compound"] = tk.LEFT
        LAddEq["image"] = Icons.add_ic
        LAddEq.tkraise(aboveThis=PasekGora)
        LAddEq.place(x=15, y=200, width=170, height=40)

        LDeleteEq = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Delete Equipment",
                             anchor="w", cursor="hand2")
        LDeleteEq["compound"] = tk.LEFT
        LDeleteEq["image"] = Icons.delete_ic
        LDeleteEq.tkraise(aboveThis=PasekGora)
        LDeleteEq.place(x=15, y=250, width=170, height=40)

        LShowEq = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Show Equipment",
                           anchor="w", cursor="hand2")
        LShowEq["compound"] = tk.LEFT
        LShowEq["image"] = Icons.show_ic
        LShowEq.tkraise(aboveThis=PasekGora)
        LShowEq.place(x=15, y=300, width=170, height=40)

        LChemistry = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Chemistry", anchor="w",
                              cursor="hand2")
        LChemistry["compound"] = tk.LEFT
        LChemistry["image"] = Icons.chemistry_ic
        LChemistry.tkraise(aboveThis=PasekGora)
        LChemistry.place(x=15, y=350, width=170, height=40)

        LMakeOrder = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Make Order", anchor="w",
                              cursor="hand2")
        LMakeOrder["compound"] = tk.LEFT
        LMakeOrder["image"] = Icons.order_ic
        LMakeOrder.tkraise(aboveThis=PasekGora)
        LMakeOrder.place(x=15, y=400, width=170, height=40)

        LHelp = tk.Label(self.master, font=("Arial", 12), bg='#3C3E45', fg='white', text="   Help", anchor="w",
                         cursor="hand2")
        LHelp["compound"] = tk.LEFT
        LHelp["image"] = Icons.help_ic
        LHelp.tkraise(aboveThis=PasekGora)
        LHelp.place(x=15, y=450, width=170, height=40)

        ### Potrzebuje ramki dla dodawania, show, order, chemistry,


        Home = tk.Frame(self.master)
        Home.place(x=199, y=118, height=610, width=850)
        StartPage(master=Home)

        AddEq = tk.Frame(self.master)
        DeleteEq = tk.Frame(self.master)
        ShowEq = tk.Frame(self.master)
        FChemistry = tk.Frame(self.master)
        FMakeOrder = tk.Frame(self.master)


        ### Bindowanie klawiszy funkcyjnych

        def forgetFrames():
            Home.place_forget()
            AddEq.place_forget()
            DeleteEq.place_forget()
            ShowEq.place_forget()
            FChemistry.place_forget()
            FMakeOrder.place_forget()

        def show_home(event):
            forgetFrames()
            Home.place(x=199, y=118, height=610, width=850)
            StartPage(master=Home)

        def show_add_eq(event):
            forgetFrames()
            AddEq.place(x=199, y=118, height=610, width=850)
            AddEquipmentFirst(master=AddEq)

        def show_delete_eq(event):
            forgetFrames()
            DeleteEq.place(x=199, y=118, height=610, width=850)

        def show_items(event):
            forgetFrames()
            ShowEq.place(x=199, y=118, height=610, width=850)
            Items(master=ShowEq)

        def show_chemistry(event):
            forgetFrames()
            FChemistry.place(x=199, y=118, height=610, width=850)
            Chemistry(master=FChemistry)

        def show_make_order(event):
            FMakeOrder.place(x=199, y=118, height=610, width=850)
            MakeOrder(master=FMakeOrder)

        def show_help(event):
            Help()
            print("Work7")

        LHome.bind("<Enter>", cl.click)
        LHome.bind("<Leave>", cl.zwolnienie)
        LHome.bind("<Button-1>", show_home)

        LAddEq.bind("<Enter>", cl.click)
        LAddEq.bind("<Leave>", cl.zwolnienie)
        LAddEq.bind("<Button-1>", show_add_eq)

        LDeleteEq.bind("<Enter>", cl.click)
        LDeleteEq.bind("<Leave>", cl.zwolnienie)
        LDeleteEq.bind("<Button-1>", show_delete_eq)

        LShowEq.bind("<Enter>", cl.click)
        LShowEq.bind("<Leave>", cl.zwolnienie)
        LShowEq.bind("<Button-1>", show_items)

        LChemistry.bind("<Enter>", cl.click)
        LChemistry.bind("<Leave>", cl.zwolnienie)
        LChemistry.bind("<Button-1>", show_chemistry)

        LMakeOrder.bind("<Enter>", cl.click)
        LMakeOrder.bind("<Leave>", cl.zwolnienie)
        LMakeOrder.bind("<Button-1>", show_make_order)

        LHelp.bind("<Enter>", cl.click)
        LHelp.bind("<Leave>", cl.zwolnienie)
        LHelp.bind("<Button-1>", show_help)

    def startMove(self, event):
        self.x = event.x
        self.y = event.y

    def stopMove(self, event):
        self.x = None
        self.y = None

    def moving(self, event):
        x = (event.x_root - self.x - self.master.winfo_rootx() + self.master.winfo_rootx())
        y = (event.y_root - self.y - self.master.winfo_rooty() + self.master.winfo_rooty())
        self.master.geometry("+%s+%s" % (x, y))

    def minimize(self, *args):
        self.master.update_idletasks()
        self.master.overrideredirect(False)
        self.master.state('withdrawn')
        self.master.state('iconic')

    def frame_mapped(self, e):
        print(self, e)
        self.master.update_idletasks()
        self.master.overrideredirect(True)
        self.master.state('normal')

    def menu(self, master, *args):
        self.file_menu = tk.Menu(master, tearoff=False)
        self.file_menu.add_command(label='New')
        self.file_menu.add_command(label='Open...')
        self.file_menu.add_command(label='Close')
