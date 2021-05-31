import tkinter as tk
import classes as cl
import Colors as Col
import categories as cat
import DataBaseOperation
import uuid
import os
import SFTP_Operation as sftp

from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

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
        self.AddOptoelectronic.bind("<Button-1>", lambda x: self.add_optoelectronics())

        self.AddConnectors.bind("<Enter>", cl.click)
        self.AddConnectors.bind("<Leave>", cl.zwolnienie)
        self.AddConnectors.bind("<Button-1>", lambda x: self.add_connectors())

        self.AddEnergySources.bind("<Enter>", cl.click)
        self.AddEnergySources.bind("<Leave>", cl.zwolnienie)
        self.AddEnergySources.bind("<Button-1>", lambda x: self.add_energy_sources())

        self.AddPCAccesories.bind("<Enter>", cl.click)
        self.AddPCAccesories.bind("<Leave>", cl.zwolnienie)
        self.AddPCAccesories.bind("<Button-1>", lambda x: self.add_pc_accessories())

        self.AddSwitches.bind("<Enter>", cl.click)
        self.AddSwitches.bind("<Leave>", cl.zwolnienie)
        self.AddSwitches.bind("<Button-1>", lambda x: self.add_switches())

        self.AddWires.bind("<Enter>", cl.click)
        self.AddWires.bind("<Leave>", cl.zwolnienie)
        self.AddWires.bind("<Button-1>", lambda x: self.add_wires())

        self.AddMechanics.bind("<Enter>", cl.click)
        self.AddMechanics.bind("<Leave>", cl.zwolnienie)
        self.AddMechanics.bind("<Button-1>", lambda x: self.add_mechanics())

        self.AddLaboratory.bind("<Enter>", cl.click)
        self.AddLaboratory.bind("<Leave>", cl.zwolnienie)
        self.AddLaboratory.bind("<Button-1>", lambda x: self.add_lab())

        self.AddOthers.bind("<Enter>", cl.click)
        self.AddOthers.bind("<Leave>", cl.zwolnienie)
        self.AddOthers.bind("<Button-1>", lambda x: self.add_others())

    def add_semiconductors(self):
        AddEquipmentSemiconductors(master=self.PadAdd2)

    def add_passive_elements(self):
        AddEquipmentPassiveElements(master=self.PadAdd2)

    def add_optoelectronics(self):
        AddOptoelectronics(master=self.PadAdd2)

    def add_connectors(self):
        AddConnectors(master=self.PadAdd2)

    def add_energy_sources(self):
        AddEnergySources(master=self.PadAdd2)

    def add_pc_accessories(self):
        AddPCAccessories(master=self.PadAdd2)

    def add_switches(self):
        AddSwitches(master=self.PadAdd2)

    def add_wires(self):
        AddWires(master=self.PadAdd2)

    def add_mechanics(self):
        AddMechanics(master=self.PadAdd2)

    def add_lab(self):
        AddLaboratory(master=self.PadAdd2)

    def add_others(self):
        AddOthers(master=self.PadAdd2)


class AddEquipmentSemiconductors:
    def __init__(self, master):
        self.Add_Semi = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Semi.place(x=-1, y=-1, height=610, width=850)

        self.b_AddComponent = tk.Button(self.Add_Semi, text='Add', font=14, bg=Color.WidgetButtons, fg='white',
                                        command=self.process_add_semi)
        self.b_AddComponent.place(height=40, width=80, x=15, y=445)

        self.b_ClearComponent = tk.Button(self.Add_Semi, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                          command=self.clear_enters)
        self.b_ClearComponent.place(height=40, width=80, x=110, y=445)

        self.UploadPdf = tk.Button(self.Add_Semi, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        # Labelki

        self.AddTitle = tk.Label(self.Add_Semi, font=("Arial", 20), text="Add new item:  Semiconductors", anchor='w',
                                 bg=Color.FrameBackground, fg='white')
        self.AddTitle.place(height=40, width=480, x=10, y=10)

        self.l_Name = tk.Label(self.Add_Semi, text="Name:", bg=Color.FrameBackground)
        self.l_Name.place(height=40, width=80, x=10, y=60)

        self.l_Group = tk.Label(self.Add_Semi, text="Group:", bg=Color.FrameBackground)
        self.l_Group.place(height=40, width=80, x=10, y=100)

        self.l_Category = tk.Label(self.Add_Semi, text="Category:", bg=Color.FrameBackground)
        self.l_Category.place(height=40, width=80, x=10, y=140)

        self.l_Model = tk.Label(self.Add_Semi, text="Model:", bg=Color.FrameBackground)
        self.l_Model.place(height=40, width=80, x=10, y=180)

        self.l_Assembly = tk.Label(self.Add_Semi, text="Assembly:", bg=Color.FrameBackground)
        self.l_Assembly.place(height=40, width=80, x=10, y=220)

        self.l_Size = tk.Label(self.Add_Semi, text="Size:", bg=Color.FrameBackground)
        self.l_Size.place(height=40, width=80, x=10, y=260)

        self.l_Where = tk.Label(self.Add_Semi, text="Where:", bg=Color.FrameBackground)
        self.l_Where.place(height=40, width=80, x=10, y=300)

        self.l_Quantity = tk.Label(self.Add_Semi, text="Quantity:", bg=Color.FrameBackground)
        self.l_Quantity.place(height=40, width=80, x=10, y=340)

        self.Link = tk.Label(self.Add_Semi, text="Link:", bg=Color.FrameBackground)
        self.Link.place(height=40, width=40, x=360, y=340)

        # Entry

        self.e_Name = ttk.Entry(self.Add_Semi, width=50)
        self.e_Name.place(height=20, width=230, x=100, y=70)

        self.e_Group = ttk.Combobox(self.Add_Semi, values=Cat_Semi.SemiCat)
        self.e_Group.bind("<Button-1>", self.reset_category)
        self.e_Group.place(height=20, width=230, x=100, y=110)

        self.e_Category = ttk.Combobox(self.Add_Semi)
        self.e_Category.bind("<Button-1>", self.choose_category)
        self.e_Category.place(height=20, width=230, x=100, y=150)

        self.e_Model = ttk.Entry(self.Add_Semi, width=50)
        self.e_Model.place(height=20, width=230, x=100, y=190)

        self.e_Assembly = ttk.Combobox(self.Add_Semi)
        self.e_Assembly.place(height=20, width=230, x=100, y=230)

        self.e_Size = ttk.Entry(self.Add_Semi, width=50)
        self.e_Size.place(height=20, width=230, x=100, y=270)

        self.e_Where = ttk.Entry(self.Add_Semi, width=50)
        self.e_Where.place(height=20, width=230, x=100, y=310)

        self.e_Quantity = ttk.Entry(self.Add_Semi, width=50)
        self.e_Quantity.place(height=20, width=230, x=100, y=350)

        self.e_Link = tk.Entry(self.Add_Semi)
        self.e_Link.place(height=20, width=250, x=410, y=350)

        # Wejscia link i dokumenty i obrazy

        self.Obraz = ttk.Button(self.Add_Semi, text="tutaj bedzie obraz", command=self.picture_process)
        self.Obraz.place(height=250, width=250, x=410, y=70)

    def reset_category(self, *args):
        self.e_Category.delete(0, tk.END)

    def choose_category(self, *args):
        category = self.e_Group.get()
        if category == 'Diodes':
            self.e_Category.config(values=Cat_Semi.Diodes)
        elif category == 'Thyristors':
            self.e_Category.config(values=Cat_Semi.Thyristors)
        elif category == 'Triacs':
            self.e_Category.config(values=Cat_Semi.Triacs)
        elif category == 'Diacs':
            self.e_Category.config(values=Cat_Semi.Diacs)
        elif category == 'Transistors':
            self.e_Category.config(values=Cat_Semi.Transistors)
        elif category == 'Integrated circuits':
            self.e_Category.config(values=Cat_Semi.Integrated_circuits)

    def picture_process(self):
        self.generate_uniqe_id()
        self.open_img()
        self.save_picture_in_sftp_server()

    def generate_uniqe_id(self):
        self.Uniqe_ID = uuid.uuid1()
        print(self.Uniqe_ID)

    def open_img(self):

        self.path = filedialog.askopenfilename()
        img = Image.open(self.path)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(self.Add_Semi, image=img)
        panel.image = img
        panel.place(height=250, width=250, x=410, y=70)

    def save_picture_in_sftp_server(self):
        host = '10.224.20.12'
        port = 22
        username = 'sftpuser'
        keyfile_path = None
        password = 'start123'
        self.sftpclient = sftp.SFTP.create_sftp_client(host, port, username, password, keyfile_path, 'DSA')
        self.sftpclient.put(f'{self.path}', f'./shared/Semiconductors/{self.Uniqe_ID}.png')
        self.sftpclient.close()

    def process_add_semi(self):
        self.get_values()
        self.sent_to_database()
        self.clear_enters()
        tk.messagebox.showinfo("Add", "Item was added")

    def clear_enters(self, *args):
        self.e_Name.delete(0, tk.END)
        self.e_Group.delete(0, tk.END)
        self.e_Category.delete(0, tk.END)
        self.e_Model.delete(0, tk.END)
        self.e_Assembly.delete(0, tk.END)
        self.e_Size.delete(0, tk.END)
        self.e_Where.delete(0, tk.END)
        self.e_Quantity.delete(0, tk.END)
        self.e_Link.delete(0, tk.END)

    def get_values(self):
        self.RVName_S = self.e_Name.get()
        self.RVGroup_S = self.e_Group.get()
        self.RVSubCategory_S = self.e_Category.get()
        self.RVModel_S = self.e_Model.get()
        self.RVAssembly_S = self.e_Assembly.get()
        self.RVSize_S = self.e_Size.get()
        self.RVWhere_S = self.e_Where.get()
        self.RVQuantity_S = self.e_Quantity.get()
        self.RVLink_S = self.e_Link.get()
        self.Namepictures = self.Uniqe_ID

    def sent_to_database(self, *args):
        DataBaseOperation.ConnectDatabase.__init__(self, host="10.224.20.12", port=3306, user="Krzysiek",
                                                   password="start123", database="CMS")
        DataBaseOperation.ConnectDatabase._open(self)
        DataBaseOperation.ConnectDatabase.insert_semi(self, Name_S=self.RVName_S, Group_S=self.RVGroup_S,
                                                      Category_S=self.RVSubCategory_S, Model_S=self.RVModel_S,
                                                      Assembly_S=self.RVAssembly_S, Size_S=self.RVSize_S,
                                                      Where_S=self.RVWhere_S, Quantity_S=self.RVQuantity_S,
                                                      Link_S=self.RVLink_S, Picture_S=self.Namepictures)
        DataBaseOperation.ConnectDatabase._close(self)


class AddEquipmentPassiveElements:
    def __init__(self, master):
        self.Add_Passive = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Passive.place(x=-1, y=-1, height=610, width=850)

        self.b_AddPassive = tk.Button(self.Add_Passive, text='Add', font=14, bg=Color.Buttons_Background,
                                      fg='white', command=self.process_add_passive)
        self.b_AddPassive.place(height=40, width=80, x=15, y=520)

        self.ClearPassive = tk.Button(self.Add_Passive, text='Clear', font=14, bg=Color.Buttons_Background,
                                      fg='white', command=self.clear_enters)
        self.ClearPassive.place(height=40, width=80, x=110, y=520)

        self.UploadPdfPassive = tk.Button(self.Add_Passive, text='Upload PDF', font=14, bg=Color.Buttons_Background,
                                          fg='white')
        self.UploadPdfPassive.place(height=40, width=100, x=320, y=520)

        # Labelki

        self.AddTitlePassive = tk.Label(self.Add_Passive, font=("Arial", 20), text="Add new item:  Passive elements",
                                        anchor='w', bg=Color.FrameBackground, fg='white')
        self.AddTitlePassive.place(height=40, width=480, x=10, y=10)

        self.l_NamePassive = tk.Label(self.Add_Passive, text="Name:", bg=Color.FrameBackground)
        self.l_NamePassive.place(height=40, width=80, x=10, y=60)

        self.l_GroupPassive = tk.Label(self.Add_Passive, text="Group:", bg=Color.FrameBackground)
        self.l_GroupPassive.place(height=40, width=80, x=10, y=100)

        self.l_CategoryPassive = tk.Label(self.Add_Passive, text="Category:", bg=Color.FrameBackground)
        self.l_CategoryPassive.place(height=40, width=80, x=10, y=140)

        self.l_ModelPassive = tk.Label(self.Add_Passive, text="Model:", bg=Color.FrameBackground)
        self.l_ModelPassive.place(height=40, width=80, x=10, y=180)

        self.l_Assembly = tk.Label(self.Add_Passive, text="Assembly:", bg=Color.FrameBackground)
        self.l_Assembly.place(height=40, width=80, x=10, y=220)

        self.l_SizePassive = tk.Label(self.Add_Passive, text="Size:", bg=Color.FrameBackground)
        self.l_SizePassive.place(height=40, width=80, x=10, y=260)

        self.l_ValuePassive = tk.Label(self.Add_Passive, text="Value:", bg=Color.FrameBackground)
        self.l_ValuePassive.place(height=40, width=80, x=10, y=300)

        self.l_TolerancePassive = tk.Label(self.Add_Passive, text="Tolerance:", bg=Color.FrameBackground)
        self.l_TolerancePassive.place(height=40, width=80, x=10, y=340)

        self.l_WatsPassive = tk.Label(self.Add_Passive, text="Wats:", bg=Color.FrameBackground)
        self.l_WatsPassive.place(height=40, width=80, x=10, y=380)

        self.l_WherePassive = tk.Label(self.Add_Passive, text="Where:", bg=Color.FrameBackground)
        self.l_WherePassive.place(height=40, width=80, x=10, y=420)

        self.l_QuantityPassive = tk.Label(self.Add_Passive, text="Quantity:", bg=Color.FrameBackground)
        self.l_QuantityPassive.place(height=40, width=80, x=10, y=460)

        self.Link = tk.Label(self.Add_Passive, text="Link:", bg=Color.FrameBackground)
        self.Link.place(height=40, width=180, x=290, y=340)

        # Wejscia

        self.e_NamePassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_NamePassive.place(height=20, width=230, x=100, y=70)

        self.e_GroupPassive = ttk.Combobox(self.Add_Passive, values=Cat_Passive.PassiveElementsGroup)
        self.e_GroupPassive.bind("<Button-1>", self.reset_category)
        self.e_GroupPassive.place(height=20, width=230, x=100, y=110)

        self.e_CategoryPassive = ttk.Combobox(self.Add_Passive)
        self.e_CategoryPassive.bind("<Button-1>", self.choose_passive)
        self.e_CategoryPassive.place(height=20, width=230, x=100, y=150)

        self.e_ModelPassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_ModelPassive.place(height=20, width=230, x=100, y=190)

        self.e_AssemblyPassive = ttk.Combobox(self.Add_Passive, )
        self.e_AssemblyPassive.place(height=20, width=230, x=100, y=230)

        self.e_SizePassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_SizePassive.place(height=20, width=230, x=100, y=270)

        self.e_ValuePassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_ValuePassive.place(height=20, width=230, x=100, y=310)

        self.e_TolerancePassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_TolerancePassive.place(height=20, width=230, x=100, y=350)

        self.e_WatsPassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_WatsPassive.place(height=20, width=230, x=100, y=390)

        self.e_WherePassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_WherePassive.place(height=20, width=230, x=100, y=430)

        self.e_QuantityPassive = ttk.Entry(self.Add_Passive, width=50)
        self.e_QuantityPassive.place(height=20, width=230, x=100, y=470)

        self.e_Link = tk.Entry(self.Add_Passive)
        self.e_Link.place(height=20, width=250, x=410, y=350)

        ###
        self.Obraz = ttk.Button(self.Add_Passive, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=410, y=70)

    def reset_category(self, *args):
        self.e_CategoryPassive.delete(0, tk.END)

    def choose_passive(self, *args):
        category = self.e_GroupPassive.get()
        if category == 'Resistors':
            self.e_CategoryPassive.config(values=Cat_Passive.Resistors)
        elif category == 'Capacitors':
            self.e_CategoryPassive.config(values=Cat_Passive.Capacitors)
        elif category == 'Inductors':
            self.e_CategoryPassive.config(values=Cat_Passive.Inductors)
        elif category == 'EMI EMC components':
            self.e_CategoryPassive.config(values=Cat_Passive.EMI_EMC_components)
        elif category == 'Quartz crystals and filters':
            self.e_CategoryPassive.config(values=Cat_Passive.Quartz_crystals_and_filters)
        elif category == 'Potentiometers':
            self.e_CategoryPassive.config(values=Cat_Passive.Potentiometers)
        elif category == 'Encoders':
            self.e_CategoryPassive.config(values=Cat_Passive.Encoders)
        elif category == 'NTC thermistors':
            self.e_CategoryPassive.config(values=Cat_Passive.NTC_thermistors)

    def process_add_passive(self):
        self.get_values()
        self.clear_enters()
        self.sent_to_database()
        messagebox.showinfo("Add EQ", "Item was added successfully")

    def get_values(self):
        self.name = self.e_NamePassive.get()
        self.group = self.e_GroupPassive.get()
        self.category = self.e_CategoryPassive.get()
        self.model = self.e_ModelPassive.get()
        self.assembly = self.e_AssemblyPassive.get()
        self.size = self.e_SizePassive.get()
        self.value = self.e_ValuePassive.get()
        self.tolerance = self.e_TolerancePassive.get()
        self.wats = self.e_WatsPassive.get()
        self.quantity = self.e_QuantityPassive.get()
        self.where = self.e_WherePassive.get()
        self.link = self.e_Link.get()

    def clear_enters(self):
        self.e_NamePassive.delete(0, tk.END)
        self.e_GroupPassive.delete(0, tk.END)
        self.e_CategoryPassive.delete(0, tk.END)
        self.e_ModelPassive.delete(0, tk.END)
        self.e_AssemblyPassive.delete(0, tk.END)
        self.e_SizePassive.delete(0, tk.END)
        self.e_ValuePassive.delete(0, tk.END)
        self.e_TolerancePassive.delete(0, tk.END)
        self.e_WatsPassive.delete(0, tk.END)
        self.e_QuantityPassive.delete(0, tk.END)
        self.e_WherePassive.delete(0, tk.END)
        self.e_Link.delete(0, tk.END)

    def sent_to_database(self, *args):
        DataBaseOperation.ConnectDatabase.__init__(self, host="10.224.20.18", port=3306, user="Krzysiek",
                                                   password="start123", database="CMS")

        DataBaseOperation.ConnectDatabase._open(self)

        DataBaseOperation.ConnectDatabase.insert_passive(self, name=self.name, group=self.group, category=self.category,
                                                         model=self.model, assembly=self.assembly, size=self.size,
                                                         value=self.value, tolerance=self.tolerance, wats=self.wats,
                                                         where=self.where, quantity=self.quantity,
                                                         link=self.link, picture='tak')
        DataBaseOperation.ConnectDatabase._close(self)


class AddOptoelectronics:
    def __init__(self, master):
        self.Add_Opto = tk.Frame(master, bg="blue")
        self.Add_Opto.place(x=-1, y=-1, height=610, width=850)

        self.b_Add_Opto = tk.Button(self.Add_Opto, text='Add', font=14, bg=Color.Buttons_Background,
                                    fg='white', command=self.process_add_connectors)
        self.b_Add_Opto.place(height=40, width=80, x=15, y=520)

        self.Clear_Opto = tk.Button(self.Add_Opto, text='Clear', font=14, bg=Color.Buttons_Background,
                                    fg='white', command=self.clear_enters)
        self.Clear_Opto.place(height=40, width=80, x=110, y=520)

        self.UploadPdfPassive = tk.Button(self.Add_Opto, text='Upload PDF', font=14, bg=Color.Buttons_Background,
                                          fg='white')
        self.UploadPdfPassive.place(height=40, width=100, x=320, y=520)

        # Labelki

        self.Add_Title_Opto = tk.Label(self.Add_Opto, font=("Arial", 20), text="Add new item:  Optoelectronics",
                                       anchor='w',
                                       bg=Color.FrameBackground, fg='white')
        self.Add_Title_Opto.place(height=40, width=480, x=10, y=10)

        self.l_Name_Opto = tk.Label(self.Add_Opto, text="Name:", bg=Color.FrameBackground)
        self.l_Name_Opto.place(height=40, width=80, x=10, y=60)

        self.l_Group_Opto = tk.Label(self.Add_Opto, text="Group:", bg=Color.FrameBackground)
        self.l_Group_Opto.place(height=40, width=80, x=10, y=100)

        self.l_Category_Opto = tk.Label(self.Add_Opto, text="Category:", bg=Color.FrameBackground)
        self.l_Category_Opto.place(height=40, width=80, x=10, y=140)

        self.l_Model_Opto = tk.Label(self.Add_Opto, text="Model:", bg=Color.FrameBackground)
        self.l_Model_Opto.place(height=40, width=80, x=10, y=180)

        self.l_Assembly_Opto = tk.Label(self.Add_Opto, text="Assembly:", bg=Color.FrameBackground)
        self.l_Assembly_Opto.place(height=40, width=80, x=10, y=220)

        self.l_Size_Opto = tk.Label(self.Add_Opto, text="Size:", bg=Color.FrameBackground)
        self.l_Size_Opto.place(height=40, width=80, x=10, y=260)

        self.l_Colour_Opto = tk.Label(self.Add_Opto, text="Colour:", bg=Color.FrameBackground)
        self.l_Colour_Opto.place(height=40, width=80, x=10, y=300)

        self.l_Wats_Opto = tk.Label(self.Add_Opto, text="Wats:", bg=Color.FrameBackground)
        self.l_Wats_Opto.place(height=40, width=80, x=10, y=340)

        self.l_Where_Opto = tk.Label(self.Add_Opto, text="Where:", bg=Color.FrameBackground)
        self.l_Where_Opto.place(height=40, width=80, x=10, y=380)

        self.l_QuantityPassive = tk.Label(self.Add_Opto, text="Quantity:", bg=Color.FrameBackground)
        self.l_QuantityPassive.place(height=40, width=80, x=10, y=420)

        self.Link_Opto = tk.Label(self.Add_Opto, text="Link:", bg=Color.FrameBackground)
        self.Link_Opto.place(height=40, width=180, x=290, y=340)

        # Wejscia

        self.e_Name_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Name_Opto.place(height=20, width=230, x=100, y=70)

        self.e_Group_Opto = ttk.Combobox(self.Add_Opto, values=Cat_Opto.Opto_Group)
        self.e_Group_Opto.bind("<Button-1>", self.reset_category)
        self.e_Group_Opto.place(height=20, width=230, x=100, y=110)

        self.e_Category_Opto = ttk.Combobox(self.Add_Opto)
        self.e_Category_Opto.bind("<Button-1>", self.choose_opto)
        self.e_Category_Opto.place(height=20, width=230, x=100, y=150)

        self.e_Model_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Model_Opto.place(height=20, width=230, x=100, y=190)

        self.e_Assembly_Opto = ttk.Combobox(self.Add_Opto, )
        self.e_Assembly_Opto.place(height=20, width=230, x=100, y=230)

        self.e_Size_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Size_Opto.place(height=20, width=230, x=100, y=270)

        self.e_Colour_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Colour_Opto.place(height=20, width=230, x=100, y=310)

        self.e_Wats_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Wats_Opto.place(height=20, width=230, x=100, y=350)

        self.e_Where_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Where_Opto.place(height=20, width=230, x=100, y=390)

        self.e_Quantity_Opto = ttk.Entry(self.Add_Opto, width=50)
        self.e_Quantity_Opto.place(height=20, width=230, x=100, y=430)

        self.e_Link_Opto = tk.Entry(self.Add_Opto)
        self.e_Link_Opto.place(height=20, width=250, x=410, y=350)

        ###
        self.Obraz = ttk.Button(self.Add_Opto, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=410, y=70)

    def reset_category(self, *args):
        self.e_Category_Opto.delete(0, tk.END)

    def choose_opto(self, *args):
        category = self.e_Group_Opto.get()
        if category == 'LEDs':
            self.e_Category_Opto.config(values=Cat_Opto.LEDs)
        elif category == 'LED indicators':
            self.e_Category_Opto.config(values=Cat_Opto.LED_indicators)
        elif category == 'Displays':
            self.e_Category_Opto.config(values=Cat_Opto.Displays)
        elif category == 'Optocouplers':
            self.e_Category_Opto.config(values=Cat_Opto.Optocouplers)
        elif category == 'Photoelements':
            self.e_Category_Opto.config(values=Cat_Opto.Photoelements)
        elif category == 'Laser':
            self.e_Category_Opto.config(values=Cat_Opto.Laser)

    def process_add_connectors(self):
        self.get_values()
        self.clear_enters()
        self.sent_to_database()
        messagebox.showinfo("Add EQ", "Item was added successfully")

    def get_values(self):
        self.name = self.e_Name_Opto.get()
        self.group = self.e_Group_Opto.get()
        self.category = self.e_Category_Opto.get()
        self.model = self.e_Model_Opto.get()
        self.assembly = self.e_Assembly_Opto.get()
        self.size = self.e_Size_Opto.get()
        self.colour = self.e_Colour_Opto.get()
        self.wats = self.e_Wats_Opto.get()
        self.where = self.e_Where_Opto.get()
        self.quantity = self.e_Quantity_Opto.get()
        self.link = self.e_Link_Opto.get()

    def clear_enters(self):
        self.e_Name_Opto.delete(0, tk.END)
        self.e_Group_Opto.delete(0, tk.END)
        self.e_Category_Opto.delete(0, tk.END)
        self.e_Model_Opto.delete(0, tk.END)
        self.e_Assembly_Opto.delete(0, tk.END)
        self.e_Size_Opto.delete(0, tk.END)
        self.e_Colour_Opto.delete(0, tk.END)
        self.e_Wats_Opto.delete(0, tk.END)
        self.e_Quantity_Opto.delete(0, tk.END)
        self.e_Link_Opto.delete(0, tk.END)

    def sent_to_database(self):

        DataBaseOperation.ConnectDatabase.__init__(self, host="10.224.20.18", port=3306, user="Krzysiek",
                                                   password="start123", database="CMS")
        DataBaseOperation.ConnectDatabase._open(self)

        DataBaseOperation.ConnectDatabase.insert_opto(self, name=self.name, group=self.group, category=self.category,
                                                      model=self.model, assembly=self.assembly, size=self.size,
                                                      colour=self.colour, wats=self.wats, where=self.where,
                                                      quantity=self.quantity, link=self.link)
        DataBaseOperation.ConnectDatabase._close(self)


class AddConnectors:
    def __init__(self, master):
        self.Add_Con = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Con.place(x=-1, y=-1, height=610, width=850)

        ### BUTTONS

        self.AddCon = tk.Button(self.Add_Con, text='Add', font=14, bg=Color.WidgetButtons, fg='white',
                                command=self.process_add_connectors)
        self.AddCon.place(height=40, width=80, x=15, y=445)

        self.ClearCon = tk.Button(self.Add_Con, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                  command=self.clear_enters)

        self.ClearCon.place(height=40, width=80, x=110, y=445)

        self.UploadPdf = tk.Button(self.Add_Con, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        ### Labels

        self.AddTitleCon = tk.Label(self.Add_Con, font=("Arial", 20), text="Add new item:  Connectors", anchor='w',
                                    bg=Color.FrameBackground, fg='white')
        self.AddTitleCon.place(height=40, width=280, x=10, y=10)

        self.l_Name_Con = tk.Label(self.Add_Con, text="Name:", bg=Color.FrameBackground)
        self.l_Name_Con.place(height=40, width=80, x=10, y=60)

        self.l_Group_Con = tk.Label(self.Add_Con, text="Group:", bg=Color.FrameBackground)
        self.l_Group_Con.place(height=40, width=80, x=10, y=100)

        self.l_Category_Con = tk.Label(self.Add_Con, text="Category:", bg=Color.FrameBackground)
        self.l_Category_Con.place(height=40, width=80, x=10, y=140)

        self.l_Model_Con = tk.Label(self.Add_Con, text="Model:", bg=Color.FrameBackground)
        self.l_Model_Con.place(height=40, width=80, x=10, y=180)

        self.l_Assembly_Con = tk.Label(self.Add_Con, text="Assembly:", bg=Color.FrameBackground)
        self.l_Assembly_Con.place(height=40, width=80, x=10, y=220)

        self.l_Brand_Con = tk.Label(self.Add_Con, text="Brand:", bg=Color.FrameBackground)
        self.l_Brand_Con.place(height=40, width=80, x=10, y=260)

        self.l_Where_Con = tk.Label(self.Add_Con, text="Where:", bg=Color.FrameBackground)
        self.l_Where_Con.place(height=40, width=80, x=10, y=300)

        self.l_Quantity_Con = tk.Label(self.Add_Con, text="Quantity:", bg=Color.FrameBackground)
        self.l_Quantity_Con.place(height=40, width=80, x=10, y=340)

        self.l_Link_Con = tk.Label(self.Add_Con, text="Link:", bg=Color.FrameBackground)
        self.l_Link_Con.place(height=40, width=180, x=290, y=340)

        ### Enters

        self.e_Name_Con = ttk.Entry(self.Add_Con, width=50)
        self.e_Name_Con.place(height=20, width=230, x=100, y=70)

        self.e_Group_Con = ttk.Combobox(self.Add_Con, values=Cat_Connectors.Connectors_group)
        self.e_Group_Con.place(height=20, width=230, x=100, y=110)

        self.e_Category_Con = ttk.Combobox(self.Add_Con)
        self.e_Category_Con.bind("<Button-1>", self.choose_connectors)
        self.e_Category_Con.place(height=20, width=230, x=100, y=150)

        self.e_Model_Con = ttk.Entry(self.Add_Con, width=50)
        self.e_Model_Con.place(height=20, width=230, x=100, y=190)

        self.e_Assembly_Con = ttk.Combobox(self.Add_Con, )
        self.e_Assembly_Con.place(height=20, width=230, x=100, y=230)

        self.e_Brand_Con = ttk.Entry(self.Add_Con, width=50)
        self.e_Brand_Con.place(height=20, width=230, x=100, y=270)

        self.e_Where_Con = ttk.Entry(self.Add_Con, width=50)
        self.e_Where_Con.place(height=20, width=230, x=100, y=310)

        self.e_Quantity_Con = ttk.Entry(self.Add_Con, width=50)
        self.e_Quantity_Con.place(height=20, width=230, x=100, y=350)

        self.e_Link_Con = tk.Entry(self.Add_Con)
        self.e_Link_Con.place(height=20, width=250, x=410, y=350)

        self.Obraz = ttk.Button(self.Add_Con, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=410, y=70)

    def choose_connectors(self, *args):
        category = self.e_Group_Con.get()
        if category == 'Signal connectors':
            self.e_Category_Con.config(values=Cat_Connectors.Signal_connectors)
        elif category == 'Data connectors':
            self.e_Category_Con.config(values=Cat_Connectors.Data_connectors)
        elif category == 'RF connectors':
            self.e_Category_Con.config(values=Cat_Connectors.RF_connectors)
        elif category == 'Power connectors':
            self.e_Category_Con.config(values=Cat_Connectors.Power_connectors)
        elif category == 'Push on connectors and cable terminals':
            self.e_Category_Con.config(values=Cat_Connectors.Push_on_connectors_and_cable_terminals)
        elif category == 'Industrial connectors':
            self.e_Category_Con.config(values=Cat_Connectors.Industrial_connectors)

    def process_add_connectors(self):
        self.get_values()
        self.clear_enters()
        self.sent_to_database()
        messagebox.showinfo("Add EQ", "Item was added successfully")

    def get_values(self):
        self.name = self.e_Name_Con.get()
        self.group = self.e_Group_Con.get()
        self.category = self.e_Category_Con.get()
        self.model = self.e_Model_Con.get()
        self.brand = self.e_Brand_Con.get()
        self.assembly = self.e_Assembly_Con.get()
        self.where = self.e_Where_Con.get()
        self.quantity = self.e_Quantity_Con.get()
        self.link = self.e_Link_Con.get()

    def clear_enters(self):
        self.e_Name_Con.delete(0, tk.END)
        self.e_Group_Con.delete(0, tk.END)
        self.e_Category_Con.delete(0, tk.END)
        self.e_Model_Con.delete(0, tk.END)
        self.e_Brand_Con.delete(0, tk.END)
        self.e_Assembly_Con.delete(0, tk.END)
        self.e_Where_Con.delete(0, tk.END)
        self.e_Quantity_Con.delete(0, tk.END)
        self.e_Link_Con.delete(0, tk.END)

    def sent_to_database(self):
        DataBaseOperation.ConnectDatabase.__init__(self, host="10.224.20.18", port=3306, user="Krzysiek",
                                                   password="start123", database="CMS")
        DataBaseOperation.ConnectDatabase._open(self)

        DataBaseOperation.ConnectDatabase.insert_connectors(self, name=self.name, group=self.group,
                                                            category=self.category, model=self.model,
                                                            assembly=self.assembly, brand=self.brand,
                                                            where=self.where, quantity=self.quantity, link=self.link)

        DataBaseOperation.ConnectDatabase._close(self)


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

        self.AddTitleEnergy = tk.Label(self.Add_Energy, font=("Arial", 20), text="Add new item:", anchor='w',
                                       bg=Color.FrameBackground, fg='white')
        self.AddTitleEnergy.place(height=40, width=280, x=10, y=10)

        self.lNameEnergy = tk.Label(self.Add_Energy, text="Name:", bg=Color.FrameBackground)
        self.lNameEnergy.place(height=40, width=80, x=10, y=60)

        self.lGroupEnergy = tk.Label(self.Add_Energy, text="Group:", bg=Color.FrameBackground)
        self.lGroupEnergy.place(height=40, width=80, x=10, y=100)

        self.lSubCategoryEnergy = tk.Label(self.Add_Energy, text="SubCategory:", bg=Color.FrameBackground)
        self.lSubCategoryEnergy.place(height=40, width=80, x=10, y=140)

        self.lModelEnergy = tk.Label(self.Add_Energy, text="Model:", bg=Color.FrameBackground)
        self.lModelEnergy.place(height=40, width=80, x=10, y=180)

        self.lAssemblyEnergy = tk.Label(self.Add_Energy, text="Assembly:", bg=Color.FrameBackground)
        self.lAssemblyEnergy.place(height=40, width=80, x=10, y=220)

        self.lWhereEnergy = tk.Label(self.Add_Energy, text="Where:", bg=Color.FrameBackground)
        self.lWhereEnergy.place(height=40, width=80, x=10, y=260)

        self.lQuintityEnergy = tk.Label(self.Add_Energy, text="Quintity:", bg=Color.FrameBackground)
        self.lQuintityEnergy.place(height=40, width=80, x=10, y=300)

        ### Enters

        self.eNameEnergy = ttk.Entry(self.Add_Energy, width=50)
        self.eNameEnergy.place(height=20, width=230, x=100, y=70)

        self.eGroupEnergy = ttk.Combobox(self.Add_Energy, )
        self.eGroupEnergy.place(height=20, width=230, x=100, y=110)

        self.eSubCategoryEnergy = ttk.Combobox(self.Add_Energy, )
        self.eSubCategoryEnergy.place(height=20, width=230, x=100, y=150)

        self.eModelEnergy = ttk.Entry(self.Add_Energy, width=50)
        self.eModelEnergy.place(height=20, width=230, x=100, y=190)

        self.eAssemblyEnergy = ttk.Combobox(self.Add_Energy, )
        self.eAssemblyEnergy.place(height=20, width=230, x=100, y=230)

        self.eWhereEnergy = ttk.Entry(self.Add_Energy, width=50)
        self.eWhereEnergy.place(height=20, width=230, x=100, y=270)

        self.eQuantityEnergy = ttk.Entry(self.Add_Energy, width=50)
        self.eQuantityEnergy.place(height=20, width=230, x=100, y=310)

        ###
        self.Link = tk.Label(self.Add_Energy, text="Tutaj będzie link", bg=Color.FrameBackground)
        self.Link.place(height=40, width=180, x=360, y=340)

        self.Obraz = ttk.Button(self.Add_Energy, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=360, y=70)


class AddPCAccessories:
    def __init__(self, master):
        self.Add_PCAccesories = tk.Frame(master, bg="green")
        self.Add_PCAccesories.place(x=0, y=0, height=610, width=850)


class AddSwitches:
    def __init__(self, master):
        self.Add_Switches = tk.Frame(master, bg="red")
        self.Add_Switches.place(x=0, y=0, height=610, width=850)


class AddWires:
    def __init__(self, master):
        self.Add_Wires = tk.Frame(master, bg=Color.FrameBackground)
        self.Add_Wires.place(x=0, y=0, height=610, width=850)

        ### BUTTONS

        self.AddWires = tk.Button(self.Add_Wires, text='Add', font=14, bg=Color.WidgetButtons, fg='white',
                                  command=self.process_add_wires)
        self.AddWires.place(height=40, width=80, x=15, y=445)

        self.ClearWires = tk.Button(self.Add_Wires, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                    command=self.clear_enters)
        self.ClearWires.place(height=40, width=80, x=110, y=445)

        self.UploadPdf = tk.Button(self.Add_Wires, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.UploadPdf.place(height=40, width=100, x=320, y=445)

        ### Labels

        self.AddTitleWires = tk.Label(self.Add_Wires, font=("Arial", 20), text="Add new item: Wires", anchor='w',
                                      bg=Color.FrameBackground, fg='white')
        self.AddTitleWires.place(height=40, width=280, x=10, y=10)

        self.l_Name_Wires = tk.Label(self.Add_Wires, text="Name:", bg=Color.FrameBackground)
        self.l_Name_Wires.place(height=40, width=80, x=10, y=60)

        self.l_Group_Wires = tk.Label(self.Add_Wires, text="Group:", bg=Color.FrameBackground)
        self.l_Group_Wires.place(height=40, width=80, x=10, y=100)

        self.l_Category_Wires = tk.Label(self.Add_Wires, text="SubCategory:", bg=Color.FrameBackground)
        self.l_Category_Wires.place(height=40, width=80, x=10, y=140)

        self.l_Colour_Wires = tk.Label(self.Add_Wires, text="Colour:", bg=Color.FrameBackground)
        self.l_Colour_Wires.place(height=40, width=80, x=10, y=180)

        self.l_Length_Wires = tk.Label(self.Add_Wires, text="Length:", bg=Color.FrameBackground)
        self.l_Length_Wires.place(height=40, width=80, x=10, y=220)

        self.l_Number_Cores_Wires = tk.Label(self.Add_Wires, text="Nub. of cores:", bg=Color.FrameBackground)
        self.l_Number_Cores_Wires.place(height=40, width=80, x=10, y=260)

        self.l_Where_Wires = tk.Label(self.Add_Wires, text="Where:", bg=Color.FrameBackground)
        self.l_Where_Wires.place(height=40, width=80, x=10, y=300)

        self.l_Quantity_Wires = tk.Label(self.Add_Wires, text="Quantity:", bg=Color.FrameBackground)
        self.l_Quantity_Wires.place(height=40, width=80, x=10, y=340)

        self.l_Link_Wires = tk.Label(self.Add_Wires, text="Link:", bg=Color.FrameBackground)
        self.l_Link_Wires.place(height=40, width=40, x=360, y=340)

        ### Enters

        self.e_Name_Wires = ttk.Entry(self.Add_Wires, width=50)
        self.e_Name_Wires.place(height=20, width=230, x=100, y=70)

        self.e_Group_Wires = ttk.Combobox(self.Add_Wires, values=Cat_Wires.Wires_group)
        self.e_Group_Wires.bind("<Button-1>", self.reset_category)
        self.e_Group_Wires.place(height=20, width=230, x=100, y=110)

        self.e_Category_Wires = ttk.Combobox(self.Add_Wires)
        self.e_Category_Wires.bind("<Button-1>", self.choose_wires)
        self.e_Category_Wires.place(height=20, width=230, x=100, y=150)

        self.e_Colour_Wires = ttk.Entry(self.Add_Wires, width=50)
        self.e_Colour_Wires.place(height=20, width=230, x=100, y=190)

        self.e_Length_Wires = ttk.Entry(self.Add_Wires, width=50)
        self.e_Length_Wires.place(height=20, width=230, x=100, y=230)

        self.e_Number_Cores_Wires = ttk.Entry(self.Add_Wires, width=50)
        self.e_Number_Cores_Wires.place(height=20, width=230, x=100, y=270)

        self.e_Where_Con = ttk.Entry(self.Add_Wires, width=50)
        self.e_Where_Con.place(height=20, width=230, x=100, y=310)

        self.e_Quantity_Wires = ttk.Entry(self.Add_Wires, width=50)
        self.e_Quantity_Wires.place(height=20, width=230, x=100, y=350)

        self.e_Link_Wires = tk.Entry(self.Add_Wires)
        self.e_Link_Wires.place(height=20, width=250, x=410, y=350)

        self.Obraz = ttk.Button(self.Add_Wires, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=410, y=70)

    def reset_category(self, *args):
        self.e_Category_Wires.delete(0, tk.END)

    def choose_wires(self, *args):
        category = self.e_Group_Wires.get()
        if category == 'Cables':
            self.e_Category_Wires.config(values=Cat_Wires.Cables)
        elif category == 'Cables Assemblies':
            self.e_Category_Wires.config(values=Cat_Wires.Cables_Assemblies)
        elif category == 'Conduits and Insulating Sleeves':
            self.e_Category_Wires.config(values=Cat_Wires.Conduits_and_Insulating_Sleeves)
        elif category == 'Cables Accessories':
            self.e_Category_Wires.config(values=Cat_Wires.Cables_Accessories)

    def process_add_wires(self):
        self.get_values()
        self.clear_enters()
        self.sent_to_database()
        messagebox.showinfo("Add EQ", "Item was added successfully")

    def get_values(self):
        self.name = self.e_Name_Wires.get()
        self.group = self.e_Group_Wires.get()
        self.category = self.e_Category_Wires.get()
        self.colour = self.e_Colour_Wires.get()
        self.length = self.e_Length_Wires.get()
        self.number_core = self.e_Number_Cores_Wires.get()
        self.where = self.e_Where_Con.get()
        self.quantity = self.e_Quantity_Wires.get()
        self.link = self.e_Link_Wires.get()

    def clear_enters(self):
        self.e_Name_Wires.delete(0, tk.END)
        self.e_Group_Wires.delete(0, tk.END)
        self.e_Category_Wires.delete(0, tk.END)
        self.e_Colour_Wires.delete(0, tk.END)
        self.e_Length_Wires.delete(0, tk.END)
        self.e_Number_Cores_Wires.delete(0, tk.END)
        self.e_Where_Con.delete(0, tk.END)
        self.e_Quantity_Wires.delete(0, tk.END)
        self.e_Link_Wires.delete(0, tk.END)

    def sent_to_database(self):

        DataBaseOperation.ConnectDatabase.__init__(self, host="10.224.20.18", port=3306, user="Krzysiek",
                                                   password="start123", database="CMS")

        DataBaseOperation.ConnectDatabase._open(self)

        DataBaseOperation.ConnectDatabase.insert_wires(self, name=self.name, group=self.group, category=self.category,
                                                       colour=self.colour, length=self.length,
                                                       number_core=self.number_core, where=self.where,
                                                       quantity=self.quantity, link=self.link)

        DataBaseOperation.ConnectDatabase._close(self)


class AddMechanics:
    def __init__(self, master):
        self.Add_Mechanics = tk.Frame(master, bg="blue")
        self.Add_Mechanics.place(x=0, y=0, height=610, width=850)


class AddLaboratory:
    def __init__(self, master):
        self.Add_Lab = tk.Frame(master, bg="blue")
        self.Add_Lab.place(x=0, y=0, height=610, width=850)


class AddOthers:
    def __init__(self, master):
        self.Add_Others = tk.Frame(master, bg="yellow")
        self.Add_Others.place(x=-1, y=-1, height=610, width=850)

        self.b_Add_Others = tk.Button(self.Add_Others, text='Add', font=14, bg=Color.WidgetButtons, fg='white',
                                  command=self.Add_Others)
        self.b_Add_Others.place(height=40, width=80, x=15, y=445)

        self.b_Clear_Others = tk.Button(self.Add_Others, text='Clear', font=14, bg=Color.WidgetButtons, fg='white',
                                    command=self.Add_Others)
        self.b_Clear_Others.place(height=40, width=80, x=110, y=445)

        self.b_Upload_Pdf_Others = tk.Button(self.Add_Others, text='Upload PDF', font=14, bg=Color.WidgetButtons, fg='white',
                                   )
        self.b_Upload_Pdf_Others.place(height=40, width=100, x=320, y=445)

        ### Labels

        self.AddTitleWires = tk.Label(self.Add_Others, font=("Arial", 20), text="Add new item: Others", anchor='w',
                                      bg=Color.FrameBackground, fg='white')
        self.AddTitleWires.place(height=40, width=280, x=10, y=10)

        self.l_Name_Others = tk.Label(self.Add_Others, text="Name:", bg=Color.FrameBackground)
        self.l_Name_Others.place(height=40, width=80, x=10, y=60)

        self.l_Description_Others = tk.Label(self.Add_Others, text="Description:", bg=Color.FrameBackground)
        self.l_Description_Others.place(height=40, width=80, x=10, y=100)

        self.l_Height_Others = tk.Label(self.Add_Others, text="Height:", bg=Color.FrameBackground)
        self.l_Height_Others.place(height=40, width=80, x=10, y=140)

        self.l_Width_Others = tk.Label(self.Add_Others, text="Width:", bg=Color.FrameBackground)
        self.l_Width_Others.place(height=40, width=80, x=10, y=180)

        self.l_Length_Others = tk.Label(self.Add_Others, text="Length:", bg=Color.FrameBackground)
        self.l_Length_Others.place(height=40, width=80, x=10, y=220)

        self.l_Value_Others = tk.Label(self.Add_Others, text="Value:", bg=Color.FrameBackground)
        self.l_Value_Others.place(height=40, width=80, x=10, y=260)

        self.l_Where_Others = tk.Label(self.Add_Others, text="Where:", bg=Color.FrameBackground)
        self.l_Where_Others.place(height=40, width=80, x=10, y=300)

        self.l_Quantity_Others = tk.Label(self.Add_Others, text="Quantity:", bg=Color.FrameBackground)
        self.l_Quantity_Others.place(height=40, width=80, x=10, y=340)

        self.l_Link_Others = tk.Label(self.Add_Others, text="Link:", bg=Color.FrameBackground)
        self.l_Link_Others.place(height=40, width=40, x=360, y=340)

        ### Enters

        self.e_Name_Others = ttk.Entry(self.Add_Others, width=50)
        self.e_Name_Others.place(height=20, width=230, x=100, y=70)

        self.e_Description_Others = tk.Text(self.Add_Others)
        self.e_Description_Others.place(height=20, width=230, x=100, y=110)

        self.e_Height_Others = ttk.Entry(self.Add_Others)
        self.e_Height_Others.place(height=20, width=230, x=100, y=150)

        self.e_Width_Others = ttk.Entry(self.Add_Others, width=50)
        self.e_Width_Others.place(height=20, width=230, x=100, y=190)

        self.e_Length_Wires = ttk.Entry(self.Add_Others, width=50)
        self.e_Length_Wires.place(height=20, width=230, x=100, y=230)

        self.e_Value_Others = ttk.Entry(self.Add_Others, width=50)
        self.e_Value_Others.place(height=20, width=230, x=100, y=270)

        self.e_Where_Others = ttk.Entry(self.Add_Others, width=50)
        self.e_Where_Others.place(height=20, width=230, x=100, y=310)

        self.e_Quantity_Others = ttk.Entry(self.Add_Others, width=50)
        self.e_Quantity_Others.place(height=20, width=230, x=100, y=350)

        self.e_Link_Others = tk.Entry(self.Add_Others)
        self.e_Link_Others.place(height=20, width=250, x=410, y=350)

        self.Obraz = ttk.Button(self.Add_Others, text="tutaj bedzie obraz")
        self.Obraz.place(height=250, width=250, x=410, y=70)
