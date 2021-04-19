import random
import smtplib
import ssl
import mysql.connector
import tkinter as tk
import classes as cl
from tkinter import messagebox
from tkinter import ttk
from MainWindow import MainWindow
import windowxd as w
import Colors as Col

### Definie colours
Colors = Col.ColoursLoginWindow()
Type_of_Users = cl.TypeUsers()


class LoginToApp:
    def __init__(self):
        self.Login = tk.Tk()  # Tworzenie okna głównego
        self.Login.overrideredirect(True)  # Usuwanie ochydenej ramki windows
        screen_width = self.Login.winfo_screenwidth()  # Konfiguracja Okienka
        screen_height = self.Login.winfo_screenheight()
        login_width = 480
        login_height = 260
        center_x = int(screen_width / 2 - login_width / 2)
        center_y = int(screen_height / 2 - login_height / 2)
        self.Login.geometry(f'{login_width}x{login_height}+{center_x}+{center_y}')
        self.Login.resizable(False, False)
        self.Login.attributes('-topmost', True)
        self.Login.configure(bg=Colors.Main_Background)

        ##################### First
        myCanvas = tk.Canvas(self.Login, bg=Colors.Canvas, height=57.5, width=480)  # Budowa tła niebieskie
        myCanvas.tag_raise(1)
        myCanvas.place(x=0, y=-5)

        self.Sep2 = ttk.Separator(self.Login, orient='horizontal')
        self.Sep2.place(width=450, x=15, y=180)

        ##################### Labels

        self.LoginTitle = tk.Label(self.Login, text='Component Database Management',
                                   bg=Colors.Label_Title_Background, fg=Colors.Label_Title_Foreground,
                                   font=("Helvetica", 16))

        self.LoginTitle.place(height=55, width=380, x=0, y=0)

        self.close = tk.Label(self.Login, font=("Arial", 11), anchor=tk.CENTER, bg='#0052cc', text="X", cursor="hand2")
        self.close.tkraise(aboveThis=myCanvas)
        self.close.place(x=425, y=0, width=55, height=55)

        self.UserLoginLabel = tk.Label(self.Login, text='User Name', bg='white', font=("Helvetica", 10))
        self.UserLoginLabel.place(height=20, width=140, x=-10, y=80)

        self.UserLoginPassword = tk.Label(self.Login, text='User Password', bg='white', font=("Helvetica", 10))
        self.UserLoginPassword.place(height=25, width=140, x=0, y=110)

        self.UserLoginType = tk.Label(self.Login, text='User Type', bg='white', font=("Helvetica", 10))
        self.UserLoginType.place(height=25, width=140, x=-13, y=140)

        self.UserLoginLabel = tk.Label(self.Login, text='Forgot your password ?', fg='blue', bg='white')
        self.UserLoginLabel.place(height=20, width=140, x=16, y=200)

        self.CreateNewAccount = tk.Label(self.Login, text='Create New Account ', fg='blue', bg='white')
        self.CreateNewAccount.place(height=20, width=140, x=10, y=225)
        ##################### Buttons

        self.UserLogin = tk.Button(self.Login, text='Log in', font=14, bg='#0052cc', fg='white', command=self.login)
        self.UserLogin.place(height=40, width=100, x=360, y=200)

        ##################### Entres

        self.UserName = ttk.Entry(self.Login, width=50)
        self.UserName.place(height=20, width=260, x=200, y=80)

        self.UserPassword = ttk.Entry(self.Login, width=50, show='*')
        self.UserPassword.place(height=20, width=260, x=200, y=110)

        self.UserLoginType = ttk.Combobox(self.Login, values=Type_of_Users.TypeUsers)
        self.UserLoginType.current(0)
        self.UserLoginType.place(height=20, width=260, x=200, y=140)

        ##################### Bind

        self.close.bind("<Enter>", cl.Hover)
        self.close.bind("<Leave>", cl.Unhover)
        self.close.bind("<Button-1>", self.exitProgram)

        self.LoginTitle.bind("<Button-1>", self.startMove)
        self.LoginTitle.bind("<ButtonRelease-1>", self.stopMove)
        self.LoginTitle.bind("<B1-Motion>", self.moving)

        self.CreateNewAccount.bind("<Button-1>", CreateNewAccount)
        self.CreateNewAccount.bind("<Enter>", cl.UnderlineOn)
        self.CreateNewAccount.bind("<Leave>",cl.UnderLineOff)

        self.UserLoginLabel.bind("<Button-1>", ForgotPassword)
        self.UserLoginLabel.bind("<Enter>", cl.UnderlineOn)
        self.UserLoginLabel.bind("<Leave>", cl.UnderLineOff)

        #####################

        self.Login.mainloop()  # wywołanie pętli komunikatów

    def login(self):
        global User
        User = self.UserName.get()
        global Password
        Password = self.UserPassword.get()
        print(User, Password)

        w.MainWindow(master=None)
        # MainWindow()

        if (User == '' or Password == ''):
            # tk.messagebox.showerror("Login Error", "All fields are required  ")
            self.UserName.delete(0, 'end')
            self.UserPassword.delete(0, 'end')
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="KrzysiekmySql12",
                database="sql-kurs"
            )
            mycursor = mydb.cursor()
            sql = mycursor.execute(
                f"SELECT UserPasswordOryginal, UserPasswordChanged FROM useraccount WHERE UserName = '{User}'")
            mycursor.execute(sql)
            myresult = mycursor.fetchone()
            mydb.close()

            UserPasswordOryginal = myresult[0]
            UserGenerateChanged = myresult[1]

            if Password == UserGenerateChanged:
                tk.messagebox.showinfo("Login Status", 'Login Sucesfully')
                self.Login.destroy()
                MainWindow()

            elif Password == UserPasswordOryginal:
                print("musisz zmienic haslo")
                self.ChangePassword()
                self.UserPassword.delete(0, 'end')

            else:
                tk.messagebox.showerror('Error', 'Wrong User Name or Password')
                self.UserPassword.delete(0, 'end')

            '''
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="KrzysiekmySql12",
                database="sql-kurs"
            )

            mycursor = mydb.cursor()

           sql = "INSERT INTO useraccount(UserName, UserEmail, UserPasswordOryginal,UserPasswordChanged) " \
                  "VALUES (%s, %s,%s,%s)"
            val = ("Krzysiek123", "Krzysiek@onet.pl", "adasd312312", "haslo123")
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")'''

    def SendEmail(self, sender_email, receiver_email, message):
        password = "krzysiek123"
        port = 465
        smtp_serwer = "smtp.gmail.com"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_serwer, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    def ChangePassword(self):
        self.CHP = tk.Toplevel()
        self.CHP.title('Change Password')  # ustawienie tytułu okna głównego
        screen_width = self.Login.winfo_screenwidth()
        screen_height = self.Login.winfo_screenheight()
        Login_width = 400
        Login_height = 250
        center_x = int(screen_width / 2 - Login_width / 2)
        center_y = int(screen_height / 2 - Login_height / 2)
        self.CHP.geometry(f'{Login_width}x{Login_height}+{center_x}+{center_y}')
        self.CHP.resizable(False, False)
        self.CHP.attributes('-topmost')
        self.CHP.configure(bg='white')

        self.CHPTitle = tk.Label(self.CHP, text='Change Password',
                                 bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.CHPTitle.place(height=55, width=400, x=0, y=0)

        self.Sep5 = ttk.Separator(self.CHP, orient='horizontal')
        self.Sep5.place(width=370, x=15, y=180)

        self.NewPassword = tk.Label(self.CHP, text='New Password', fg='black', bg='white')
        self.NewPassword.place(height=40, width=100, x=0, y=60)

        self.NewPasswordConfirmation = tk.Label(self.CHP, text='New Password', fg='black', bg='white')
        self.NewPasswordConfirmation.place(height=40, width=100, x=0, y=110)

        self.eNewPassword = ttk.Entry(self.CHP, width=50, show='*')
        self.eNewPassword.place(height=30, width=220, x=150, y=70)

        self.eNewPasswordConfirmation = ttk.Entry(self.CHP, width=80, show='*')
        self.eNewPasswordConfirmation.place(height=30, width=220, x=150, y=120)

        self.changepassword = tk.Button(self.CHP, text='Change Password', font=14, bg='#0052cc', fg='white',
                                        command=self.changepassword1)
        self.changepassword.place(height=50, width=150, x=220, y=190)

    def changepassword1(self):
        rNewPassword = self.eNewPassword.get()
        rNewPasswordConfrimation = self.eNewPasswordConfirmation.get()

        if (rNewPassword == "" or rNewPasswordConfrimation == ""):
            tk.messagebox.showerror('Error', "Both Fields are required")

        elif (rNewPassword != rNewPasswordConfrimation):
            tk.messagebox.showerror('Error', "Password must be the same")
        elif (rNewPassword == rNewPasswordConfrimation):

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="KrzysiekmySql12",
                database="sql-kurs"
            )

            mycursor = mydb.cursor()

            sql2 = mycursor.execute(
                f"Update useraccount SET UserPasswordChanged ='{rNewPassword}' WHERE UserPasswordOryginal = '{Password}'")
            mycursor.execute(sql2)
            sql3 = mycursor.execute(
                f"Update useraccount SET UserPasswordOryginal ='HasloZmienione' WHERE UserPasswordOryginal = '{Password}'")
            mycursor.execute(sql3)
            mydb.commit()
            mydb.close()
            tk.messagebox.showinfo("Info", "Password was changed corttly")
            self.CHP.destroy()

    def requestForNewAccount(self):

        RUserName = self.eNewUserName.get()
        RUserEmail = self.eNewUserEmail.get()
        RUserEGM = self.eNewUserEGM.get()
        RUserDivision = self.eNewUserDivision.get()
        RUserReason = self.eNewUserReason.get()

        if (RUserName == '' or RUserEmail == '' or RUserEGM == '' or
                RUserDivision == '' or RUserReason == ''):
            tk.messagebox.showerror('Error', 'All fields are requaired')
            self.eNewUserName.delete(0, 'end')
            self.eNewUserEmail.delete(0, 'end')
            self.eNewUserEGM.delete(0, 'end')
            self.eNewUserDivision.delete(0, 'end')
        else:
            newmessage = (RUserName + " " + RUserEmail + " " + RUserEGM + " " + RUserDivision + " " + RUserReason)
            self.SendEmail("krzysiekpython@gmail.com", "krzysiu.w@spoko.pl", newmessage)
            tk.messagebox.showinfo('Info', 'Your request was send succesfully')
            self.CNAW.destroy()

    def fforgotpas1sword(self):
        Letters = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*[]{}:;'"
        PasswordLength = 10
        Password = "".join(random.sample(Letters, PasswordLength))
        Name = self.eNewUserName.get()
        Email = self.eNewUserEmail.get()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="KrzysiekmySql12",
            database="sql-kurs"
        )
        mycursor = mydb.cursor()

        sql4 = mycursor.execute(
            f"Update useraccount SET UserPasswordOryginal ='{Password}' WHERE UserEmail = '{Email}'")
        mycursor.execute(sql4)
        mydb.commit()
        mydb.close()

        messege = (f"Your password was changed to '{Password}'")
        self.SendEmail("krzysiekpython@gmail.com", Email, messege)
        tk.messagebox.showinfo('Info', 'Your password was changed - Check your email box ')

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

    def exitProgram(self, *args):
        self.Login.destroy()

    def frame_mapped(self, e):
        print(self, e)
        self.Login.update_idletasks()
        self.Login.overrideredirect(True)
        self.Login.state('normal')


class ChangePassword:
    def __init__(self):
        self.CHP = tk.Toplevel()
        self.CHP.overrideredirect(True)
        self.CHP.title('Change Password')  # ustawienie tytułu okna głównego
        screen_width = self.CHP.winfo_screenwidth()
        screen_height = self.CHP.winfo_screenheight()
        CHP_width = 400
        CHP_height = 250
        center_x = int(screen_width / 2 - CHP_width / 2)
        center_y = int(screen_height / 2 - CHP_height / 2)
        self.CHP.geometry(f'{CHP_width}x{CHP_height}+{center_x}+{center_y}')
        self.CHP.resizable(False, False)
        self.CHP.attributes('-topmost')
        self.CHP.configure(bg='white')

        self.CHPTitle = tk.Label(self.CHP, text='Change Password',
                                 bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.CHPTitle.place(height=55, width=400, x=0, y=0)

        self.Sep5 = ttk.Separator(self.CHP, orient='horizontal')
        self.Sep5.place(width=370, x=15, y=180)

        self.NewPassword = tk.Label(self.CHP, text='New Password', fg='black', bg='white')
        self.NewPassword.place(height=40, width=100, x=0, y=60)

        self.NewPasswordConfirmation = tk.Label(self.CHP, text='New Password', fg='black', bg='white')
        self.NewPasswordConfirmation.place(height=40, width=100, x=0, y=110)

        self.eNewPassword = ttk.Entry(self.CHP, width=50, show='*')
        self.eNewPassword.place(height=30, width=220, x=150, y=70)

        self.eNewPasswordConfirmation = ttk.Entry(self.CHP, width=80, show='*')
        self.eNewPasswordConfirmation.place(height=30, width=220, x=150, y=120)

        self.changepassword = tk.Button(self.CHP, text='Change Password', font=14, bg='#0052cc', fg='white',
                                        )
        self.changepassword.place(height=50, width=150, x=220, y=190)


class ForgotPassword:
    def __init__(self, *args):
        self.CNFW = tk.Toplevel()
        self.CNFW.overrideredirect(True)
        self.CNFW.title('Forgot Password')  # ustawienie tytułu okna głównego
        screen_width = self.CNFW.winfo_screenwidth()
        screen_height = self.CNFW.winfo_screenheight()
        CNFW_width = 400
        CNFW_height = 250
        center_x = int(screen_width / 2 - CNFW_width / 2)
        center_y = int(screen_height / 2 - CNFW_height / 2)
        self.CNFW.geometry(f'{CNFW_width}x{CNFW_height}+{center_x}+{center_y}')
        self.CNFW.resizable(False, False)
        self.CNFW.attributes('-topmost')
        self.CNFW.configure(bg='white')

        self.CNAWTitle = tk.Label(self.CNFW, text='Forgot Password',
                                  bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.CNAWTitle.place(height=55, width=400, x=0, y=0)

        self.Sep4 = ttk.Separator(self.CNFW, orient='horizontal')
        self.Sep4.place(width=370, x=15, y=180)

        self.NewUserName = tk.Label(self.CNFW, text='Add User Name', fg='black', bg='white')
        self.NewUserName.place(height=40, width=100, x=0, y=60)

        self.NewUserEmail = tk.Label(self.CNFW, text='Add User Email', fg='black', bg='white')
        self.NewUserEmail.place(height=40, width=100, x=0, y=110)

        self.eNewUserName = ttk.Entry(self.CNFW, width=50)
        self.eNewUserName.place(height=30, width=220, x=150, y=70)

        self.eNewUserEmail = ttk.Entry(self.CNFW, width=50)
        self.eNewUserEmail.place(height=30, width=220, x=150, y=120)

        self.ForgotPassword = tk.Button(self.CNFW, text='Request for Account', font=14, bg='#0052cc', fg='white',
                                        command=cl.GenerateNewPassword)
        self.ForgotPassword.place(height=50, width=150, x=220, y=190)


class CreateNewAccount:
    def __init__(self, *args):
        self.CNAW = tk.Toplevel()
        self.CNAW.overrideredirect(True)
        self.CNAW.title('Create New Account')  # ustawienie tytułu okna głównego
        screen_width = self.CNAW.winfo_screenwidth()
        screen_height = self.CNAW.winfo_screenheight()
        CNAW_width = 450
        CNAW_height = 500
        center_x = int(screen_width / 2 - CNAW_width / 2)
        center_y = int(screen_height / 2 - CNAW_height / 2)
        self.CNAW.geometry(f'{CNAW_width}x{CNAW_height}+{center_x}+{center_y}')
        self.CNAW.resizable(False, False)
        self.CNAW.attributes('-topmost')
        self.CNAW.configure(bg='white')

        self.CNAWTitle = tk.Label(self.CNAW, text='Create New Account',
                                  bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.CNAWTitle.place(height=55, width=480, x=0, y=0)

        self.Sep3 = ttk.Separator(self.CNAW, orient='horizontal')
        self.Sep3.place(width=420, x=15, y=380)

        self.NewUserName = tk.Label(self.CNAW, text='Add User Name', fg='black', bg='white')
        self.NewUserName.place(height=40, width=100, x=0, y=90)

        self.NewUserEmail = tk.Label(self.CNAW, text='Add User Email', fg='black', bg='white')
        self.NewUserEmail.place(height=40, width=100, x=0, y=140)

        self.NewUserEGM = tk.Label(self.CNAW, text='Add User EGM ', fg='black', bg='white')
        self.NewUserEGM.place(height=40, width=100, x=0, y=190)

        self.NewUserDivision = tk.Label(self.CNAW, text='Add User Division ', fg='black', bg='white')
        self.NewUserDivision.place(height=40, width=100, x=0, y=240)

        self.NewUserReason = tk.Label(self.CNAW, text='Add User Reason ', fg='black', bg='white')
        self.NewUserReason.place(height=40, width=100, x=0, y=290)

        self.eNewUserName = ttk.Entry(self.CNAW, width=50)
        self.eNewUserName.place(height=30, width=280, x=150, y=100)

        self.eNewUserEmail = ttk.Entry(self.CNAW, width=50)
        self.eNewUserEmail.place(height=30, width=280, x=150, y=150)

        self.eNewUserEGM = ttk.Entry(self.CNAW, width=50)
        self.eNewUserEGM.place(height=30, width=280, x=150, y=200)

        self.eNewUserDivision = ttk.Entry(self.CNAW, width=50)
        self.eNewUserDivision.place(height=30, width=280, x=150, y=250)

        self.eNewUserReason = ttk.Entry(self.CNAW, width=50)
        self.eNewUserReason.place(height=30, width=280, x=150, y=300)

        self.NewUserRequest = tk.Button(self.CNAW, text='Request for Account', font=14, bg='#0052cc', fg='white', )
        # command=self.requestForNewAccount)
        self.NewUserRequest.place(height=50, width=150, x=280, y=420)


LoginToApp()
