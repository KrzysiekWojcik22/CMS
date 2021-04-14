


class ColoursLoginWindow:
    def __init__(self):
        self.Main_Background = "white"

        self.Canvas = "green"

        self.Button_Foreground = ""

        self.Button_Background = ""

        self.Label_Title_Background = "#0052cc"

        self.Label_Title_Foreground = "white"

        self.Label_Foreground = "black"

        self.Label_Background = "white"

        self.Bind = ""

class ColoursMainWindow:
    def __init__(self):
        self.Border = ""

        self.MainBackground = "white"

        self.Frame = ""

        self.Buttons_Foreground = ""

        self.Buttons_Background = ""

        self.Labels_Foreground = ""

        self.Labels_Background = ""

        self.Labels_after_bind = ""
'''
class Icons:
    def __init__(self):
        from PIL import ImageTk, Image
        import tkinter as tk
        self.email_ic = ImageTk.PhotoImage(Image.open("ikoneczki\email.png"))
        self.emailL = tk.Label(self.root, image=self.email_ic, bg='red')
        self.emailL.photo = self.email_ic

        home_ic = ImageTk.PhotoImage(Image.open("ikoneczki\home.png"))
        homeL = tk.Label(self.root, image=home_ic)
        homeL.photo = home_ic

        add_ic = ImageTk.PhotoImage(Image.open("ikoneczki\plus.png"))
        addL = tk.Label(self.root, image=add_ic)
        addL.photo = add_ic

        delete_ic = ImageTk.PhotoImage(Image.open("ikoneczki\delete.png"))
        deleteL = tk.Label(self.root, image=delete_ic)
        deleteL.photo = delete_ic

        show_ic = ImageTk.PhotoImage(Image.open("ikoneczki\show.png"))
        showL = tk.Label(self.root, image=show_ic)
        showL.photo = show_ic

        chemistry_ic = ImageTk.PhotoImage(Image.open("ikoneczki\chemistry.png"))
        chemistryL = tk.Label(self.root, image=chemistry_ic)
        chemistryL.photo = chemistry_ic

        order_ic = ImageTk.PhotoImage(Image.open("ikoneczki\cart.png"))
        orderL = tk.Label(self.root, image=order_ic)
        orderL.photo = order_ic

        help_ic = ImageTk.PhotoImage(Image.open("ikoneczki\info.png"))
        helpL = tk.Label(self.root, image=help_ic)
        helpL.photo = help_ic
'''

class TypeUsers:
    def __init__(self):
        self.TypeUsers = ["Default", "Admin"]

class CloseProgram:
    def __init__(self, window):
       self.window = window.destroy()

class Move:
        def startMove(self, event):
            self.x = event.x
            self.y = event.y

        def stopMove(self, event):
            self.x = None
            self.y = None

        def moving(self, event):
            x = (event.x_root - self.x - self.Login.winfo_rootx() + self.Login.winfo_rootx())
            y = (event.y_root - self.y - self.Login.winfo_rooty() + self.Login.winfo_rooty())
            self.Login.geometry("+%s+%s" % (x, y))

class Hover:
    def __init__(self,event):
        event.widget.config(bg="red")

class Unhover:
    def __init__(self,event):
        event.widget.config(bg='#0052cc')

class click:
    def __init__(self,event):
        event.widget.config(bg="#52555E")

class zwolnienie:
    def __init__(self,event):
        event.widget.config(bg='blue')

class GenerateNewPassword:
    def __init__(self):
        import random
        Letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*[]{}:;'"
        PasswordLength = 10
        Password = "".join(random.sample(Letters, PasswordLength))
        print(Password)


