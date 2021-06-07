import tkinter as tk
import Colors as Col
import classes as cl
from tkinter import ttk
from categories import EquipmentCategoriesChemistry
from tkinter import filedialog
import DataBaseOperation
from tkinter import messagebox
import yagmail

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
        self.Search.place(height=640, width=720, x=-1, y=-1)

        # search

        self.Search_title = tk.Label(self.Search, text="Search for a Container", font=('Arial', 12), fg="black",
                                     anchor="w", )
        self.Search_title.place(height=40, width=350, x=15, y=15)

        Obramowanie = tk.Canvas(self.Search, bg='grey', height=350, width=350)
        Obramowanie.tag_raise(0)
        Obramowanie.place(x=15, y=60)

        self.Name = tk.Label(self.Search, text="Name:", font=('Arial', 10), fg="black", anchor="w", bg='gray')
        self.Name.place(height=20, width=80, x=35, y=80)

        self.CAS = tk.Label(self.Search, text="CAS Number:", font=('Arial', 10), fg="black", anchor="w", bg='gray')
        self.CAS.place(height=20, width=80, x=35, y=160)
        #
        self.Barcode = tk.Label(self.Search, text="Barcode", font=('Arial', 10), fg="black", anchor="w", bg='gray')
        self.Barcode.place(height=20, width=80, x=35, y=240)

        self.Limit_search = tk.Label(self.Search, text="Limit Search to:", font=('Arial', 8), fg="black", anchor="w",
                                     bg='gray')
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
        self.Container.place(height=640, width=720, x=-1, y=-1)

        self.Container_title = tk.Label(self.Container, text="Make Order", font=('Arial', 14), fg="black",
                                        anchor="w", )
        self.Container_title.place(height=40, width=150, x=10, y=5)

        self.Container_Name = tk.Label(self.Container, text="Container Name:", font=('Arial', 10), fg="black",
                                       anchor="w", )
        self.Container_Name.place(height=20, width=120, x=10, y=60)

        self.CAS_Number = tk.Label(self.Container, text="CAS Number:", font=('Arial', 10), fg="black", anchor="w", )
        self.CAS_Number.place(height=20, width=120, x=10, y=110)

        self.Container_Size = tk.Label(self.Container, text="Container Size:", font=('Arial', 10), fg="black",
                                       anchor="w", )
        self.Container_Size.place(height=20, width=120, x=10, y=160)

        self.Barcode = tk.Label(self.Container, text="Barcode:", font=('Arial', 10), fg="black", anchor="w", )
        self.Barcode.place(height=20, width=120, x=10, y=210)

        self.Location = tk.Label(self.Container, text="Location:", font=('Arial', 10), fg="black", anchor="w", )
        self.Location.place(height=20, width=120, x=10, y=260)

        self.Supplier = tk.Label(self.Container, text="Supplier:", font=('Arial', 10), fg="black", anchor="w", )
        self.Supplier.place(height=20, width=120, x=10, y=310)

        self.Expiry_Date = tk.Label(self.Container, text="Expiry Date:", font=('Arial', 10), fg="black", anchor="w", )
        self.Expiry_Date.place(height=20, width=120, x=10, y=360)

        self.Product_Code = tk.Label(self.Container, text="Product Code", font=('Arial', 10), fg="black", anchor="w", )
        self.Product_Code.place(height=20, width=120, x=10, y=410)

        self.Documents = tk.Label(self.Container, text="Upload links to product:", font=('Arial', 10), fg="black",
                                  anchor="w", )
        self.Documents.place(height=20, width=160, x=10, y=460)

        # Enters

        self.e_Container_Name = ttk.Entry(self.Container)
        self.e_Container_Name.place(height=20, width=350, x=10, y=85)

        self.e_CAS_Number = ttk.Entry(self.Container)
        self.e_CAS_Number.place(height=20, width=350, x=10, y=135)

        self.e_Container_Size = ttk.Entry(self.Container)
        self.e_Container_Size.place(height=20, width=245, x=10, y=185)

        self.e_Container_Unit = ttk.Combobox(self.Container, values=Units)
        self.e_Container_Unit.place(height=20, width=75, x=285, y=185)

        self.e_Quantity = ttk.Entry(self.Container)
        self.e_Quantity.place(height=20, width=350, x=10, y=235)

        self.e_Location = ttk.Combobox(self.Container, values=Location)
        self.e_Location.place(height=20, width=350, x=10, y=285)

        self.e_Supplier = ttk.Entry(self.Container)
        self.e_Supplier.place(height=20, width=350, x=10, y=335)

        self.e_Expiry_Date = ttk.Entry(self.Container)
        self.e_Expiry_Date.place(height=20, width=350, x=10, y=385)

        self.e_Product_Code = ttk.Entry(self.Container)
        self.e_Product_Code.place(height=20, width=350, x=10, y=435)

        self.e_Documents = ttk.Entry(self.Container)
        self.e_Documents.place(height=20, width=350, x=10, y=485)

        # Buttons

        self.b_Clear_Container = tk.Button(self.Container, text="Clear", command=self.clear_container)
        self.b_Clear_Container.place(height=40, width=80, x=105, y=520)

        self.b_Add_Container = tk.Button(self.Container, text="Add", command=self.add_container)
        self.b_Add_Container.place(height=40, width=80, x=10, y=520)

    def clear_container(self):
        self.e_Container_Name.delete(0, tk.END)
        self.e_CAS_Number.delete(0, tk.END)
        self.e_Container_Size.delete(0, tk.END)
        self.e_Container_Unit.delete(0, tk.END)
        self.e_Quantity.delete(0, tk.END)
        self.e_Location.delete(0, tk.END)
        self.e_Supplier.delete(0, tk.END)
        self.e_Expiry_Date.delete(0, tk.END)
        self.e_Product_Code.delete(0, tk.END)
        self.e_Documents.delete(0, tk.END)

    def get_values(self):
        self.name = self.e_Container_Name.get()
        self.cas_number = self.e_CAS_Number.get()
        self.container_size = self.e_Container_Size.get()
        self.container_unit = self.e_Container_Unit.get()
        self.quantity = self.e_Quantity.get()
        self.location = self.e_Location.get()
        self.supplier = self.e_Supplier.get()
        self.expiry_date = self.e_Expiry_Date.get()
        self.product_code = self.e_Product_Code.get()
        self.link = self.e_Documents.get()

    def container_to_database(self):
        DataBaseOperation.ConnectDatabase.__init__(self, host="10.224.20.12", port=3306, user="Krzysiek",
                                                   password="start123", database="CMS")
        DataBaseOperation.ConnectDatabase._open(self)

        DataBaseOperation.ConnectDatabase.insert_new_container(self, name=self.name, cas_number=self.cas_number,
                                                               size=self.container_size, unit=self.container_unit,
                                                               quantity=self.quantity, location=self.location,
                                                               supplier=self.supplier, expiry_date=self.expiry_date,
                                                               product_code=self.product_code, link=self.link,
                                                               photo="tak", pdf="tak")

        DataBaseOperation.ConnectDatabase._close(self)

    def add_container(self):
        self.get_values()
        self.container_to_database()
        self.clear_container()
        tk.messagebox.showinfo("Add", "Item was added")


class OrderRequest:
    def __init__(self, master):
        self.Products = tk.Frame(master, bg="green")
        self.Products.place(height=640, width=720, x=-1, y=-1)

        # Buttons

        self.clear = tk.Button(self.Products, text="Clear", command=self.clear_values)
        self.clear.place(height=40, width=80, x=105, y=430)

        self.sent_order = tk.Button(self.Products, text="Add", command=self.make_order)
        self.sent_order.place(height=40, width=80, x=10, y=430)

        # Labels

        self.Container_Order_Title = tk.Label(self.Products, text="Container Name:", font=('Arial', 14), fg="black",
                                              anchor="w", )

        self.Container_Order_Title.place(height=40, width=150, x=10, y=5)

        self.Container_Order_Name = tk.Label(self.Products, text="Container Name:", font=('Arial', 10), fg="black",
                                             anchor="w", )
        self.Container_Order_Name.place(height=20, width=120, x=10, y=60)

        self.CAS_Order_Number = tk.Label(self.Products, text="CAS Number:", font=('Arial', 10), fg="black",
                                         anchor="w", )
        self.CAS_Order_Number.place(height=20, width=120, x=10, y=110)

        self.Container_Order_Size = tk.Label(self.Products, text="Container Size:", font=('Arial', 10), fg="black",
                                             anchor="w", )
        self.Container_Order_Size.place(height=20, width=120, x=10, y=160)

        self.Container_Order_Supplier = tk.Label(self.Products, text="Supplier:", font=('Arial', 10), fg="black", anchor="w", )
        self.Container_Order_Supplier.place(height=20, width=120, x=10, y=210)

        self.Container_Order_Quantity = tk.Label(self.Products, text="Quantity:", font=('Arial', 10), fg="black", anchor="w", )
        self.Container_Order_Quantity.place(height=20, width=120, x=10, y=260)

        self.Container_Order_Link = tk.Label(self.Products, text="Link:", font=('Arial', 10), fg="black", anchor="w", )
        self.Container_Order_Link.place(height=20, width=120, x=115, y=260)

        self.Container_Order_Comment = tk.Label(self.Products, text="Comments", font=('Arial', 10), fg="black",
                                                anchor="w", )
        self.Container_Order_Comment.place(height=20, width=120, x=10, y=310)

        # Enters

        self.e_Container_Order_Name = ttk.Entry(self.Products)
        self.e_Container_Order_Name.place(height=20, width=350, x=10, y=85)

        self.e_CAS_Order_Number = ttk.Entry(self.Products)
        self.e_CAS_Order_Number.place(height=20, width=350, x=10, y=135)

        self.e_Container_Order_Size = ttk.Entry(self.Products)
        self.e_Container_Order_Size.place(height=20, width=245, x=10, y=185)

        self.e_Container_Order_Unit = ttk.Combobox(self.Products, values=Units)
        self.e_Container_Order_Unit.place(height=20, width=75, x=285, y=185)

        self.e_Container_Order_Supplier = ttk.Entry(self.Products)
        self.e_Container_Order_Supplier.place(height=20, width=350, x=10, y=235)

        self.e_Container_Order_Quantity = ttk.Entry(self.Products)
        self.e_Container_Order_Quantity.place(height=20, width=75, x=10, y=285)

        self.e_Container_Order_Link = ttk.Entry(self.Products)
        self.e_Container_Order_Link.place(height=20, width=245, x=115, y=285)

        self.e_Container_Comments = tk.Text(self.Products)
        self.e_Container_Comments.place(height=80, width=350, x=10, y=335)

    def get_values(self):
        self.name = self.e_Container_Order_Name.get()
        self.cas = self.e_CAS_Order_Number.get()
        self.size = self.e_Container_Order_Size.get()
        self.unit = self.e_Container_Order_Unit.get()
        self.supplier = self.e_Container_Order_Supplier.get()
        self.link = self.e_Container_Order_Link.get()
        self.comments = self.e_Container_Comments.get(1.0, "end-1c")

    def clear_values(self):
        self.e_Container_Order_Name.delete(0, tk.END)
        self.e_CAS_Order_Number.delete(0, tk.END)
        self.e_Container_Order_Size.delete(0, tk.END)
        self.e_Container_Order_Unit.delete(0, tk.END)
        self.e_Container_Order_Supplier.delete(0, tk.END)
        self.e_Container_Order_Link.delete(0, tk.END)
        self.e_Container_Comments.delete('1.0', 'end')

    def send_email(self):
        receiver = "krzysiu.w@spoko.pl"
        Message = f"Please order'{self.name},'{self.cas}','{self.size}','{self.unit},'{self.supplier}','{self.link}','{self.comments}'"
        yag = yagmail.SMTP("krzysiekpython@gmail.com", password="krzysiek123")
        yag.send(
            to=receiver,
            subject="New Container Order",
            contents=Message,
        )

    def make_order(self):
        self.get_values()
        self.send_email()
        self.clear_values()
        tk.messagebox.showinfo("Info", "Order was sent correctly")


class Locations:
    def __init__(self, master):
        self.Location = tk.Frame(master, bg="pink")
        self.Location.place(height=640, width=720, x=-1, y=-1)

        self.Location_Title = tk.Label(self.Location, text="Location", font=('Arial', 14), fg="black", anchor="w")

        self.Location_Title.place(height=40, width=150, x=10, y=5)


class MSDSandFileStorage:
    def __init__(self, master):
        self.MSDSF = tk.Frame(master, bg="gray")
        self.MSDSF.place(height=640, width=720, x=-1, y=-1)

        Ikony = cl.Icons(master=self.MSDSF)

        self.TitleFrame = tk.Canvas(self.MSDSF, bg='grey', height=90, width=722)  # Budowa tła niebieskie
        self.TitleFrame.create_rectangle(-1, 42, 722, 90, fill='#004554', outline='#004554')
        self.TitleFrame.tag_raise(0)
        self.TitleFrame.place(x=-2, y=-2)

        self.MSDSF_Title = tk.Label(self.MSDSF, text="  (M)SDS and File Storage", font=(14), anchor='w')
        self.MSDSF_Title["compound"] = tk.LEFT
        self.MSDSF_Title["image"] = Ikony.document_ic
        self.MSDSF_Title.place(height=40, width=300, x=10, y=0)

        self.Sep1 = ttk.Separator(self.MSDSF, orient='vertical')
        self.Sep1.place(width=720, x=0, y=90)

        self.Sep2 = ttk.Separator(orient='horizontal')
        self.Sep2.place(width=10, height=10, x=10, y=20)

        self.Search = ttk.Entry(self.MSDSF, width=25, )
        self.Search.place(height=25, width=120, x=460, y=7.5)

        self.Upload_Files = tk.Button(self.MSDSF, text=" Upload Files", image=Ikony.upload_ic, compound=tk.LEFT, command = self.upload_documents)
        self.Upload_Files.place(height=30, width=100, x=600, y=5)

        self.All_Files = tk.Label(self.MSDSF, text="All Files", font=(14), anchor='w', cursor="hand2")
        self.All_Files.place(height=30, width=70, x=10, y=50)

        self.MSDS = tk.Label(self.MSDSF, text="(M)SDS", font=(14), anchor='w', cursor="hand2")
        self.MSDS.place(height=30, width=70, x=110, y=50)

        self.COA = tk.Label(self.MSDSF, text="COA", font=(14), anchor='w', cursor="hand2")
        self.COA.place(height=30, width=70, x=210, y=50)

        self.Risk_Assessments = tk.Label(self.MSDSF, text="Risk Assessments", font=(14), anchor='w', cursor="hand2")
        self.Risk_Assessments.place(height=30, width=140, x=310, y=50)

        self.All_Files.bind("<Enter>", cl.click)
        self.All_Files.bind("<Leave>", cl.zwolnienie)
        # self.All_Files.bind("<Button-1>", show_chemistry)

        self.MSDS.bind("<Enter>", cl.click)
        self.MSDS.bind("<Leave>", cl.zwolnienie)
        # self.MSDS.bind("<Button-1>", show_chemistry)

        self.COA.bind("<Enter>", cl.click)
        self.COA.bind("<Leave>", cl.zwolnienie)
        # self.COA.bind("<Button-1>", show_chemistry)

        self.Risk_Assessments.bind("<Enter>", cl.click)
        self.Risk_Assessments.bind("<Leave>", cl.zwolnienie)
    # self.Risk_Assessments.bind("<Button-1>", show_chemistry)

    def upload_documents(self):
        print("work")