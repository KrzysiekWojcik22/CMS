class EquipmentCategoriesSemiconductors:
    def __init__(self):
        self.SemiCat = ["Diodes", "Thyristors", "Triacs", "Diacs", "Transistors", "Integrated circuits"]

        self.Diodes = ["Universal diodes", "Schottky diodes", "Zener diodes", "Transil diodes",
                       "Single phase bridge rectifiers", "Three phase bridge rectifiers"]

        self.Thyristors = ["Single thyristores", "Thyristor modules"]

        self.Triacs = ["Triacs"]

        self.Diacs = ["Diacs"]

        self.Transistors = ["Unipolar transistors", "Bipolar transistors", "IGBT transistors and modules"]

        self.Integrated_circuits = ["Analog and mixed integrated circuits",
                                    "Logic integrated circuits ", "Microcontrollers and Microprocessors",
                                    "Memories - integrated circuits", "Peripheral integrated circuits",
                                    "Voltage regulators", "Others"]


class EquipmentCategoriesPassiveElements:
    def __init__(self):
        self.PassiveElementsGroup = ["Resistors", "Capacitors", "Inductors", "EMI EMC components",
                                     "Quartz crystals and filters", "Potentiometers", "Encoders", "NTC thermistors"]

        self.Resistors = ["SMD resistors", "SMD precision resistors", "Carbon THT resistors",
                          "Metal film THT resistors",
                          "Power resistors", "Fusible resistors", "Heating resistors", "Resistor networks",
                          "Audio resistors"]

        self.Capacitors = ["MLCC SMD capacitors", "THT ceramic capacitors", "MLCC THT capacitors",
                           "SNAP - IN electrolytic capacitors",
                           "Screw terminal and others el.capacitors", "Polyester capacitors",
                           "Polypropylene capacitors", "Paper capacitors",
                           "Motor capacitors", "Lighting capacitors", "Tantalum capacitors, SMD niobium capacitors",
                           "SMD capacitors others",
                           "Trimmers", "Polymer and Hybrid Capacitors", "Audio capacitors"]

        self.Inductors = ["SMD coils", "SMD inductors", "SMD power inductors", "THT inductors", "Audio coils"]

        self.EMI_EMC_components = ["EMI / EMC ferrites", "EMI / EMC sheets"]

        self.Quartz_crystals_and_filters = ["Quartz crystals", "Quartz generators", "Ceramic filters and resonators",
                                            "SAW filters and resonators"]

        self.Potentiometers = ["Trimmers", "Shaft potentiometers", "Slide potentiometers", "Audio potentiometers"]

        self.Encoders = ["Absolute type encoders", "Incremental type encoders"]

        self.NTC_thermistors = ["Measurement NTC thermistors", "Protection NTC thermistors"]


class EquipmentCategoriesOptoElectronics:
    def __init__(self):
        self.Opto_Group = ["LEDs", "LED indicators", "Displays", "Optocouplers", "Photoelements", "Laser"]

        self.LEDs = ["THT LEDs", "SMD LEDs", "Power LEDs", "Special effect LED's", "IR LEDs", "UV LEDs",
                     "Plants growth LED", "LED light sources"]

        self.LED_indicators = ["LED PCB indicators", "LED Panel Mount Indicators"]

        self.Displays = ["LED displays", "OLED displays", "LCD displays", "TFT displays", "VFD displays",
                         "Intelligent displays modules", "E-paper", "Displays - accessories", "HMI Panels"]

        self.Optocouplers = ["Optocouplers - analog output", "Optocouplers - digital output", "Optocouplers - others",
                             "Optotriacs"]

        self.Photoelements = ["Photodiodes", "IR receiver modules", "Phototransistors", "Photoresistors"]

        self.Laser = ["Laser diodes", "Laser modules"]


class EquipmentCategoriesConnectors:
    def __init__(self):
        self.Connectors_group = ["Signal connectors", "Data connectors", "RF connectors", "Power connectors",
                                 "Push on connectors and cable terminals", "Industrial connectors"]

        self.Signal_connectors = ["Pin headers", "CE100 connectors 2,54mm", "CE156 connectors 3,96mm",
                                  "DIN 41.612DIN 41.617connectors", "Dubox connectors 2,54mm", "FFC(FPC) connectors",
                                  "IDC connectors", "Micro - Match connectors 1,27mm", "Mini - Clamp connectors 2mm",
                                  "MTA - 100 connectors 2, 54mm", "IDC picoflex connectors 1, 27mm",
                                  "Board - to - board connectors", "Raster signal connectors"]

        self.Data_connectors = ["D - Sub connectors", "MDR connectors", "USB & IEEE1394 connectors", "RJ connectors",
                                "Card connectors",
                                "Centronics connectors", "V35 connectors", "Optical connectors"]

        self.RF_connectors = ["4.3 - 10 connectors", "BNC connectors", "UHF & Mini - UHF connectors", "TNC connectors",
                              "C connectors", " N connectors", "FME connectors", "SMA, SMB, SMC connectors",
                              "Micro connectors", "F connectors", "Coaxial connectors", "RF adapters"]

        self.Power_connectors = ["AC supply connectors", "Terminal blocks", "DC power connectors", "LED connectors",
                                 "Solar connectors", "Rail mounted connectors"]

        self.Push_on_connectors_and_cable_terminals = ["Insulated terminals", "Non - insulated terminals",
                                                       "Bootlace ferrule and butt splice", "Solder terminals PCB mount"]

        self.Industrial_connectors = ["Industrial circular connectors", "Rectangular multipole connectors",
                                      "Valve connectors", "Automotive connectors", "Industrial connectors - others"]

        # self.Other_connectors


class EquipmentCategoriesEnergySources:
    def __init__(self):
        self.Battery = ["tak"]


class EquipmentCategoriesPCAccessories:
    def __init__(self):
        self.Computer_Accessories = ["Memory Cards", "Pendrives", "Computer Power Supply Units and UPSs", "Peripherals",
                                     "Stands and Holders", "HDD/SSD", "AdaptersSocket", "Accessories - Others",
                                     "Privacy Filters"]


class EquipmentCategoriesSwitches:
    def __init__(self):

        self.Switches_Group = ["Microswitches", "Panel_Mount_Switches", "Rocker_Switches", "Dip_Switches",
                               "Rotary_Switches", "Toggle_Switches", "Push_Button_Switches",
                               "Vandal_Resistant_Switches", "Indicators"]

        self.Microswitches = []

        self.Panel_Mount_Switches = ["Panel Mount Switches", "Standard 16mm", "Panel Mount Switches", "Standard 22mm",
                                     "Panel Mount Switches", "Standard 30mm", "Panel Mount Accessories"]
        self.Rocker_Switches = []

        self.Dip_Switches = []

        self.Rotary_Switches = []

        self.Toggle_Switches = []

        self.Push_Button_Switches = ["Standard Switches", "Keypad Switches", "Door Switches", "Push-Pull Switches",
                                     "Detect Switches"]

        self.Vandal_Resistant_Switches = ["Push Button Switches", "Piezoelectric Switches", "Capacitive switches"]

        self.Indicators = ["LED Panel Mount Indicators", "Neon Indicators"]


class EquipmentCategoriesWires:
    def __init__(self):
        self.Wires_group = ["Cables", "Cables Assemblies", "Conduits and Insulating Sleeves", "Cables Accessories"]

        self.Cables = ["Single Core Cables", "Test Leads", "Power Cords", "Data Transmission Cables",
                       "Multicore Cables", "Cables for Power Chains",
                       "Silicone Cables", "Heat resistant cablesCar", "Installation Cables - FLRY,Coaxial Cables",
                       "Audio-Video Cables", "Ribbon Cables",
                       "Telephone Cables", "Spiral Cables", "Coil Wires", "Resistance Wires", "Silver Plated Wires",
                       "Copper Braids", "Cables - Others"]

        self.Cables_Assemblies = ["HDMI", "DVI", "DisplayPort cables and adapt", "USB cables and adapters",
                                  "RJ45 Cables", "Fibre Optic Patchcords and Pigtails", "Audio - Video Cables",
                                  "Computer cables and adapters", "Ribbon Cables with IDC Connectors",
                                  "Power Supply" "Cords,Monitor cables and adapters", "Coaxial Assemblies",
                                  "Telephone Cables Assemblies", "Sensors - Cables"]

        self.Conduits_and_Insulating_Sleeves = ["Conduits and Insulating Sleeves", "Wiring ducts", "Polyester conduits",
                                                "Electro Insulation tubes", "Protective tubes", "Conduits accessories"]

        self.Cables_Accessories = ["Cable Ties and Holders", "Cable Holders", "Worm Gear Clamps and Fixing Clamps",
                                   "Wire Markers,Glands and Grommets", "Cable Chains", "Gel Cable Joints"]


class EquipmentCategoriesMechanics:
    def __init__(self):
        self.Mechanics = ["Bolts", "Screws", "Nuts", "Spacers", "Enclosures", "Others"]


class EquipmentCategoriesLaboratory:
    def __init__(self):
        self.Measuring_Instruments = ["Analog Multimeters", "Digital Multimeters", "Meters - Accessories",
                                      "Meters and Clamp Probes", "Testers and Meters For El. Installations",
                                      "Meters of environmental conditions", "Inspection Cameras", "Boroscopes",
                                      "Automotive meters", "Panel Meters Laboratory", "instruments Laboratory",
                                      "instruments - Others" "Laboratory Power Supplies" "Oscilloscopes and Scopemeters",
                                      "LAN and Telephone Networks Testers"]

        self.Measuring_Accessories = ["Test Leads", "Probes - Test Plugs", "Test hooks", "Test Clips",
                                      "Crocodile Clips",
                                      "Banana & Fork Plugs", "Banana Sockets", "Laboratory Clamps",
                                      "Hangers and uprights on wires", "Contact Probes",
                                      "Laboratory Connectors - Others"]

        self.PCB_prototyping_and_production = ["Copper laminates", "Universal PCBs", "Assembly kits",
                                               "Materials for PCB production", ]

        self.Soldering_and_Welding_Equipment = ["Soldering irons and guns", "Gas soldering irons & torches",
                                                "Soldering & desoldering stations", "Soldering stations - accessories",
                                                "Soldering tips & nozzles", "Soldering fume extraction systems",
                                                "Soldering pots & baths", "Soldering Devices & Exposure Units",
                                                "Auxiliary soldering tools", "Desoldering wicks",
                                                "Dispensers & accessories", "Solders", "Fluxes",
                                                "Soldering chemicals", "Welding Equipment"]

        self.Tools = ["Tools"]

        self.Storage = ["Storage"]

        self.Antistatic_Protection = ["Storage"]


class EquipmentCategoriesOthers:
    pass


class EquipmentCategoriesChemistry:
    def __init__(self):
        self.Units = ["g", "mg", "kg", "lbs", "oz", "mL", "L"]
        self.Location = ["EP", "EQ", "TCK"]
        self.EP = ["Main LAB", "ProtoLAB", "EMC TENT"]
        self.EQ = ["Main LAB"]
        self.TCK = ["Main LAB"]


class SearchEquipmentGroup:
    def __init__(self):
        self.Group = ["All", "Semiconductors", "Passive elements", "Optoelectronic", "Connector", "Energy Sources",
                      "PC accessories", "Switches", "Wires", "Mechanics", "Laboratory", "Others"]


class SearchEquipmentCategory:
    def __init__(self):
        self.AllCategory = []












