import tkinter as tk
import sys

root = tk.Tk()
root.geometry("300x400")


class Elder:
    def __init__(self,master):
        myFrame = tk.Frame(master, bg="red")
        myFrame.place(width = 200 , height =100,x = 12, y=34)
        self.MyButton = tk.Button(master, text="clisk", command =self.clicker)
        self.MyButton.place(width = 20 , height =10,x = 12, y=34)

        self.MyButton = tk.Button(master, text="clisk", command=self.clicker)
        self.MyButton.place(width=20, height=10, x=12, y=34)

    def clicker(self):
        print("work")
        Elder2(master=None)

class Elder2:
    def __init__(self,master):
        myFrame2 = tk.Frame(master, bg="blue")
        myFrame2.place(width = 40 , height =80,x = 12, y=34)
        self.MyButton = tk.Button(master, text="clisk", command=self.clicker2)
        self.MyButton.place(width=20, height=10, x=40, y=34)

    def clicker2(self):
        print("work")
        Elder3(master=None)



class  Elder3:
    def __init__(self,master):
        myFrame3 = tk.Frame(master, bg="green")
        myFrame3.place(width = 40 , height =80,x = 12, y=200)


e = Elder(root)
root.mainloop()