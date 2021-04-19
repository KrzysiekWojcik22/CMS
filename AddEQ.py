import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog

class AddComponent:
    def __init__(self):
        self.Add = tk.Tk()
        self.Add.title('Add New Components')
        screen_width = self.Add.winfo_screenwidth()
        screen_height = self.Add.winfo_screenheight()
        Add_width = 480
        Add_height = 500
        center_x = int(screen_width / 2 - Add_width / 2)
        center_y = int(screen_height / 2 - Add_height / 2)
        self.Add.geometry(f'{Add_width}x{Add_height}+{center_x}+{center_y}')
        #self.Add.resizable(False, False)
        self.Add.attributes('-topmost')
        self.Add.configure(bg='#EEEEEE')
        #photo1 = PhotoImage(file="ikona.png")
        #self.root.iconphoto(False, photo1)





        self.menubar = Menu(self.Add)
        self.Add.config(menu=self.menubar)
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

        self.AddTitle = tk.Label(self.Add, text='Add New Equipment',
                                   bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.AddTitle.place(height=55, width=480, x=0, y=0)

        self.AddComponent = tk.Button(self.Add, text='Add', font = 14, bg='#0052cc', fg='white', command=lambda: AddComponent.fAddComponent(self))
        self.AddComponent.place(height=40, width=80, x=15, y=445)

        self.ClearComponent = tk.Button(self.Add, text='Clear', font = 14, bg='#0052cc', fg='white', command=lambda: AddComponent.fClearComponent(self))
        self.ClearComponent.place(height=40, width=80, x=110, y=445)

        self.QuitComponent = tk.Button(self.Add, text='Quit', font = 14, bg='#0052cc', fg='white', command=lambda: AddComponent.fQuitComponent(self))
        self.QuitComponent.place(height=40, width=80, x=205, y=445)

        self.lName = ttk.Label(self.Add, text="Name:", )
        self.lName.place(height=40, width=80, x=10, y=60)

        self.lCategory = ttk.Label(self.Add, text="Category:", )
        self.lCategory.place(height=40, width=80, x=10, y=100)

        SizeComponents = ["0201", "0402", "0603", "0805", "1008", "1206", "1210"]

        Categories = ["Semiconductors", "Passive Elements", "Optoelectronic", "Connectors",
                      "Energy Sources", "PC Accessories", "Fuses", "Switches", "Fans", "Wires",
                      "Mechanics", "Enclosures", "Laboratory", "Others"]

        self.SposobMontazu = ["THT", "SMD", "Panel", "Kabel"]
        # CasesTHT = ["DIP", "SDIP" , "TO" ]
        CasesSMD = ["SOJ", "SOIC", "PLCC", "QFP", "BGA"]
        self.grupa = ["Diody", "Tyrystory", "Triaki", "Diaki", "Tranzystory", "Układy Scalone"]
        self.subcategorysemi = ["Diody Uniwersalne", "Diody schotky", "Zenera", "specjalne"]


        self.eName = ttk.Entry(self.Add, width=50)
        self.eName.place(height=20, width=180, x=100, y=70)

        self.eCategory = ttk.Combobox(self.Add, values=Categories)
        self.eCategory.place(height=20, width=180, x=100, y=110)
        self.eCategory.bind('<<ComboboxSelected>>', self.kategoria)

        self.UploadPdf = tk.Button(self.Add, text='Upload PDF', font = 14, bg='#0052cc', fg='white', command=self.fUploadPDF)
        self.UploadPdf.place(height=40, width=100, x=340, y=70)

        self.UploadLink = tk.Button(self.Add, text='Upload Link', font = 14, bg='#0052cc', fg='white', command =self.fUploadPDF)
        self.UploadLink.place(height=40, width=100, x=340, y=150)

        self.Link = tk.Entry(self.Add, width=50)
        self.Link.place(height=20, width=180, x=340, y=200)

    def fUploadPDF(self):
        input = filedialog.askopenfile(initialdir="/")
        print(input)

    def fUploadLink(self):
        input2 = filedialog.askopenfile(initialdir="/")
        print(input2)

    def kategoria(self, kategoria1):
        MCategory = self.eCategory.get()
        try:
            self.eAssembly.place_forget()
            self.lGroup.place_forget()
            self.lSubCategory.place_forget()
            self.lModel.place_forget()
            self.lQuintity.place_forget()
            self.lWhere.place_forget()
            self.eWhere.place_forget()
            self.eGroup.place_forget()
            self.eSubCategory.place_forget()
            self.eModel.place_forget()
            self.eQuintity.place_forget()
            self.lAssembly.place_forget()
            self.eAssembly.place_forget()
            self.eSize.place_forget()
            self.lSize.place_forget()
        except:
            pass

        if MCategory == "Semiconductors":

           self.lGroup = ttk.Label(self.Add, text="Group:")
           self.lGroup.place(height=40, width=80, x=10, y=140)
           self.eGroup = ttk.Combobox(self.Add, values=self.grupa)
           self.eGroup.place(height=20, width=180, x=100, y=150)

           self.lSubCategory = ttk.Label(self.Add, text="SubCategory:")
           self.lSubCategory.place(height=40, width=80, x=10, y=180)

           self.eSubCategory = ttk.Combobox(self.Add,values=self.subcategorysemi)
           self.eSubCategory.place(height=20, width=180, x=100, y=190)

           self.lModel = ttk.Label(self.Add, text="Model:")
           self.lModel.place(height=40, width=80, x=10, y=220)

           self.eModel = ttk.Entry(self.Add, width=50)
           self.eModel.place(height=20, width=180, x=100, y=230)

           self.lAssembly=ttk.Label(self.Add, text="Assembly:")
           self.lAssembly.place(height=40, width=80, x=10, y=260)

           self.eAssembly = ttk.Combobox(self.Add,values=self.SposobMontazu)
           self.eAssembly.place(height=20, width=180, x=100, y=270)

           self.lSize = ttk.Label(self.Add, text="Size:")
           self.lSize.place(height=40, width=80, x=10, y=300)

           self.eSize = ttk.Entry(self.Add, width=50)
           self.eSize.place(height=20, width=180, x=100, y=310)

           self.lWhere = ttk.Label(self.Add, text="Where:")
           self.lWhere.place(height=40, width=80, x=10, y=340)

           self.eWhere = ttk.Entry(self.Add, width=50)
           self.eWhere.place(height=20, width=180, x=100, y=350)

           self.lQuintity =ttk.Label(self.Add, text="Quintity:")
           self.lQuintity.place(height=40, width=80, x=10, y=380)

           self.eQuintity = ttk.Entry(self.Add, width=50)
           self.eQuintity.place(height=20, width=180, x=100, y=390)

        elif MCategory == "Passive Elements":


            self.eAssembly = ttk.Combobox(self.Add, values=self.SposobMontazu)
            self.eAssembly.place(height=20, width=180, x=100, y=170)

        elif MCategory == "Optoelectronics":
            print("Hello1")
        elif MCategory == "Connectors":
            print("Hello2")
        elif MCategory == "Energy Sources":
            print("Hello3")
        elif MCategory == "PC Accessories":
            print("Hello4")
        elif MCategory == "Fuses":
            print("Hello5")
        elif MCategory == "Switches":
            print("Hello6")
        elif MCategory == "Fans":
            print("Hello7")
        elif MCategory == "Wires":
            print("Hello8")
        elif MCategory == "Mechanics":
            print("Hello9")
        elif MCategory == "Enclosures":
            print("Hello10")
        elif MCategory == "Laboratory":
            print("Hello11")
        elif MCategory == "Others":
            print("Hello12")

    def fQuitComponent(self):
        self.Add.destroy()


    def fAddComponent(self):
        MCategory = self.eCategory.get()
        if MCategory == "Semiconductors":
            Name = self.eName.get()
            Group = self.eGroup.get()
            SubCategory =self.eSubCategory.get()
            Model =self.eModel.get()
            Assembly =self.eAssembly.get()
            Size =self.eSize.get()
            Where =self.eWhere.get()
            Quantity =self.eQuintity.get()
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="KrzysiekmySql12",
                database="sql-kurs"
            )
            mycursor = mydb.cursor()
            AddSemi = mycursor.execute(f"Insert Into semiconductors(Name_S, Group_S, SubCategory_S, Model_S, Assembly_S, Size_S, Where_S, Quantity_S) "
                                   f"VALUES('{Name}','{Group}','{SubCategory}','{Model}','{Assembly}','{Size}','{Where}','{Quantity}')")
            mycursor.execute(AddSemi)
            mydb.commit()
            mydb.close()
            tk.messagebox.showinfo("Info", "Item was added corectly")
            self.Add.destroy()


'''
    def fClearComponent(self):
        self.eName.delete(0, 'end')
        self.eCategory.delete(0, 'end')
      #  self.eGroup.delete(0, 'end')
      #  self.eAssembly.delete(0, 'end')
      #  self.eSize.delete(0, 'end')
      #  self.eCase.delete(0, 'end')
      #  self.eStorage.delete(0, 'end')
     #   self.eQuantity.delete(0, 'end')

    def fQuitComponent(self):
        print("Quit")


'''

