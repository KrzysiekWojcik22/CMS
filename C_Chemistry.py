import tkinter as tk
import Colors as Col
import classes as cl
from tkinter import ttk
from categories import EquipmentCategoriesChemistry

Color = Col.ColoursMainWindow()
Chem_cat = EquipmentCategoriesChemistry()
Units = Chem_cat.Units
Location = Chem_cat.Location

class Chemistry:
    def __init__(self, master, *args):
        self.Chemistry1 = tk.Frame(master)
        self.Chemistry1.place(x=0, y=0, height=620, width=850)

        self.Chem_1 = tk.PanedWindow(self.Chemistry1, bg=Color.FrameMenu)
        self.Chem_1.place(height=700, width=150, x=0, y=0)
        self.Chem_2 = tk.PanedWindow(self.Chemistry1, bg=Color.FrameBackground)
        self.Chem_2.place(height=640, width=720, x=140, y=0)

        self.Sep1Pad1 = ttk.Separator(self.Chem_1, orient='horizontal')
        self.Sep1Pad1.place(width=130, x=5, y=40)

        self.ChemistryTitle = tk.Label(self.Chem_1, font=("Arial", 14), bg=Color.Buttons_Background, fg='white',
                                       text="ChemInventory")
        self.ChemistryTitle.place(width=130, height=40, x=5, y=0)

        self.Search_Chemistry = tk.Label(self.Chem_1, text="Search",
                                         bg='#004554', fg="white", anchor="w",
                                         cursor="hand2")
        self.Search_Chemistry.place(width=110, height=40, x=15, y=50)

        self.Add_a_Container = tk.Label(self.Chem_1, text="Add a Container",
                                        bg=Color.Labels_Background_FrameMenu, fg="white", anchor="w",
                                        cursor="hand2")

        self.Add_a_Container.place(width=110, height=40, x=15, y=100)

        self.Order_Requests = tk.Label(self.Chem_1, text="Order Request",
                                       bg=Color.Labels_Background_FrameMenu, fg="white", anchor="w",
                                       cursor="hand2")

        self.Order_Requests.place(width=110, height=40, x=15, y=150)

        self.Locations = tk.Label(self.Chem_1, text="Locations",
                                  bg=Color.Labels_Background_FrameMenu, fg="white", anchor="w",
                                  cursor="hand2")

        self.Locations.place(width=110, height=40, x=15, y=200)

        self.Material_Safety_Data_Sheet = tk.Label(self.Chem_1, text="(M)SDS and File Storage)",
                                                   bg=Color.Labels_Background_FrameMenu, fg="white", anchor="w",
                                                   cursor="hand2")
        self.Material_Safety_Data_Sheet.place(width=110, height=40, x=15, y=250)

        # Bind

        self.Search_Chemistry.bind("<Enter>", cl.click)
        self.Search_Chemistry.bind("<Leave>", cl.zwolnienie)
        self.Search_Chemistry.bind("<Button-1>", lambda x: Search(master=self.Chem_2))

        self.Add_a_Container.bind("<Enter>", cl.click)
        self.Add_a_Container.bind("<Leave>", cl.zwolnienie)
        self.Add_a_Container.bind("<Button-1>", lambda x: AddaContainer(master=self.Chem_2))

        self.Order_Requests.bind("<Enter>", cl.click)
        self.Order_Requests.bind("<Leave>", cl.zwolnienie)
        self.Order_Requests.bind("<Button-1>", lambda x: OrderRequest(master=self.Chem_2))

        self.Locations.bind("<Enter>", cl.click)
        self.Locations.bind("<Leave>", cl.zwolnienie)
        self.Locations.bind("<Button-1>", lambda x: Locations(master=self.Chem_2))

        self.Material_Safety_Data_Sheet.bind("<Enter>", cl.click)
        self.Material_Safety_Data_Sheet.bind("<Leave>", cl.zwolnienie)
        self.Material_Safety_Data_Sheet.bind("<Button-1>", lambda x: MSDSandFileStorage(master=self.Chem_2))


class Search:
    def __init__(self, master):
        self.Search = tk.Frame(master, bg="gray")
        self.Search.place(height=640, width=720, x=0, y=0)

        ## search

        self.Search_title = tk.Label(self.Search, text="Search for a Container", font=('Arial', 12), fg="black", anchor="w",)
        self.Search_title.place(height=40, width=350, x=15, y=15)

        Obramowanie = tk.Canvas(self.Search, bg='grey', height=350, width=350)
        Obramowanie.tag_raise(0)
        Obramowanie.place(x=15, y=60)

        self.Name = tk.Label(self.Search, text="Name:", font=('Arial', 10), fg="black", anchor="w",bg='gray')
        self.Name.place(height=20, width=80, x=35, y=80)

        self.CAS = tk.Label(self.Search, text="CAS Number:", font=('Arial', 10), fg="black", anchor="w",bg='gray')
        self.CAS.place(height=20, width=80, x=35, y=160)
#
        self.Barcode = tk.Label(self.Search, text="Barcode", font=('Arial', 10), fg="black", anchor="w",bg='gray')
        self.Barcode.place(height=20, width=80, x=35, y=240)

        self.Limit_search = tk.Label(self.Search, text="Limit Search to:", font=('Arial', 8), fg="black", anchor="w",bg='gray')
        self.Limit_search.place(height=20, width=120, x=35, y=310)

        # Enters

        self.Compound_Name = ttk.Entry(self.Search, width=50, )
        self.Compound_Name.place(height=30, width=300, x=35, y=105)

        self.CAS_Registry_Number = ttk.Entry(self.Search, width=50)
        self.CAS_Registry_Number.place(height=30, width=300, x=35, y=185)

        self.Barcode = ttk.Entry(self.Search, width=50)
        self.Barcode.place(height=30, width=300, x=35, y=265)

        # Buttons

        self.Structure_Search = tk.Button(self.Search, text='Adv. Search', font=12, bg='#0052cc', fg='white')
        self.Structure_Search.place(height=30, width=100, x=150, y=330)

        self.SearchB = tk.Button(self.Search, text='Search', font=12, bg='#0052cc', fg='white')
        self.SearchB.place(height=30, width=70, x=265, y=330)


class AddaContainer:
    def __init__(self, master):
        self.Container = tk.Frame(master, bg=Color.WidgetBackground)
        self.Container.place(height=640, width=720, x=0, y=0)

        self.Container_Name = tk.Label(self.Container, text="Container Name:", font=('Arial', 12), fg="black", anchor="w",)
        self.Container_Name.place(height=40, width=350, x=15, y=15)

        self.CAS_Number = tk.Label(self.Container, text="CAS Number:", font=('Arial', 12), fg="black", anchor="w",)
        self.CAS_Number.place(height=40, width=350, x=15, y=15)

        self.Container_Size = tk.Label(self.Container, text="Container Size:", font=('Arial', 12), fg="black", anchor="w",)
        self.Container_Size.place(height=40, width=350, x=15, y=15)

        self.Container_Unit = tk.Label(self.Container, text="Units:", font=('Arial', 12), fg="black", anchor="w",)
        self.Container_Unit.place(height=40, width=350, x=15, y=15)

        self.Barcode = tk.Label(self.Container, text="Barcode:", font=('Arial', 12), fg="black", anchor="w",)
        self.Barcode.place(height=40, width=350, x=15, y=15)

        self.Location = tk.Label(self.Container, text="Location:", font=('Arial', 12), fg="black", anchor="w",)
        self.Location.place(height=40, width=350, x=15, y=15)

        self.Supplier = tk.Label(self.Container, text="Supplier:", font=('Arial', 12), fg="black", anchor="w",)
        self.Supplier.place(height=40, width=350, x=15, y=15)

        self.Expiry_Date = tk.Label(self.Container, text="Expiry Date:", font=('Arial', 12), fg="black", anchor="w",)
        self.Expiry_Date.place(height=40, width=350, x=15, y=15)

        self.Product_Code = tk.Label(self.Container, text="Product Code", font=('Arial', 12), fg="black", anchor="w",)
        self.Product_Code.place(height=40, width=350, x=15, y=15)

        self.Documents = tk.Label(self.Container, text="Upload Documents:", font=('Arial', 12), fg="black", anchor="w",)
        self.Documents.place(height=40, width=350, x=15, y=15)

        # Enters

        self.e_Container_Name = ttk.Entry(self.Container, width=50)
        self.e_Container_Name.place(height=40, width=350, x=15, y=15)

        self.e_CAS_Number = ttk.Entry(self.Container, width=50)
        self.e_CAS_Number.place(height=40, width=350, x=15, y=15)

        self.e_Container_Size = ttk.Entry(self.Container, width=50)
        self.e_Container_Size.place(height=40, width=350, x=15, y=15)

        self.e_Container_Unit = ttk.Combobox(self.Container, values=Units )
        self.e_Container_Unit.place(height=40, width=350, x=15, y=15)

        self.e_Location = ttk.Combobox(self.Container, values=Location)
        self.e_Location.place(height=40, width=350, x=15, y=15)

        self.e_Supplier = ttk.Entry(self.Container, width=50)
        self.e_Supplier.place(height=40, width=350, x=15, y=15)

        self.e_Expiry_Date = ttk.Entry(self.Container, width=50)
        self.e_Expiry_Date.place(height=40, width=350, x=15, y=15)

        self.e_Product_Code = ttk.Entry(self.Container, width=50)
        self.e_Product_Code.place(height=40, width=350, x=15, y=15)

        self.e_Documents = ttk.Entry(self.Container, width=50)
        self.e_Documents.place(height=40, width=350, x=15, y=15)

        # Buttons

        self.b_Add_Comment = tk.Button(self.Container)
        self.b_Add_Comment.place(height=40, width=350, x=15, y=15)

        self.b_Add = tk.Button(self.Container)
        self.b_Add.place(height=40, width=350, x=15, y=15)


class OrderRequest:
    def __init__(self, master):
        self.Products = tk.Frame(master, bg="green")
        self.Products.place(height=640, width=720, x=0, y=0)

        self.Container_Name = tk.Label(self.Products, text="Container Name:", font=('Arial', 12), fg="black",
                                       anchor="w", )
        self.Container_Name.place(height=40, width=350, x=15, y=15)

        self.CAS_Number = tk.Label(self.Products, text="CAS Number:", font=('Arial', 12), fg="black", anchor="w", )
        self.CAS_Number.place(height=40, width=350, x=15, y=15)

        self.Container_Size = tk.Label(self.Products, text="Container Size:", font=('Arial', 12), fg="black",
                                       anchor="w", )
        self.Container_Size.place(height=40, width=350, x=15, y=15)

        self.Container_Unit = tk.Label(self.Products, text="Units:", font=('Arial', 12), fg="black", anchor="w", )
        self.Container_Unit.place(height=40, width=350, x=15, y=15)

        self.Comment = tk.Label(self.Products, text="Units:", font=('Arial', 12), fg="black", anchor="w", )
        self.Comment.place(height=40, width=350, x=15, y=15)

        self.Quantity = tk.Label(self.Products, text="Units:", font=('Arial', 12), fg="black", anchor="w", )
        self.Quantity.place(height=40, width=350, x=15, y=15)


class Locations:
    def __init__(self, master):
        self.NewChemistry = tk.Frame(master, bg="pink")
        self.NewChemistry.place(height=640, width=720, x=0, y=0)


class MSDSandFileStorage:
    def __init__(self, master):
        self.MSDSF = tk.Frame(master, bg="pink")
        self.MSDSF.place(height=640, width=720, x=0, y=0)
    '''
    All Files 
    MSDS
    COA
    Risk Assessments
    Edit Categories
    Search files
    Upload Files
    
    '''