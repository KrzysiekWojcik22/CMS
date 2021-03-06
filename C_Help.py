import tkinter as tk
import classes as cl
from tkinter import ttk


class Help:
    def __init__(self):
        self.Help = tk.Toplevel()
        self.Help.overrideredirect(True)
        self.Help.title('Help')
        screen_width = self.Help.winfo_screenwidth()
        screen_height = self.Help.winfo_screenheight()
        help_width = 400
        help_height = 700
        center_x = int(screen_width / 2 - help_width / 2)
        center_y = int(screen_height / 2 - help_height / 2)
        self.Help.geometry(f'{help_width}x{help_height}+{center_x}+{center_y}')
        self.Help.resizable(False, False)
        self.Help.attributes('-topmost', True)
        self.Help.configure(bg="grey")

        self.CHPTitle = tk.Label(self.Help, text='Help',
                                 bg='#0052cc', fg='white', font=("Helvetica", 14))
        self.CHPTitle.place(height=55, width=400, x=0, y=0)

        self.close = tk.Label(self.Help, font=("Arial", 11), anchor=tk.CENTER, bg='#0052cc', text="X", cursor="hand2")
        self.close.tkraise(aboveThis=self.CHPTitle)
        self.close.place(x=345, y=0, width=55, height=55)

        self.close.bind("<Enter>", cl.Hover)
        self.close.bind("<Leave>", cl.Unhover)
        self.close.bind("<Button-1>", lambda x: self.Help.destroy())

        self.Sep5 = ttk.Separator(self.Help, orient='horizontal')
        self.Sep5.place(width=370, x=15, y=180)

        self.CHPTitle.bind("<Button-1>", self.start_move)
        self.CHPTitle.bind("<ButtonRelease-1>", self.stop_move)
        self.CHPTitle.bind("<B1-Motion>", self.moving)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def moving(self, event):
        x = (event.x_root - self.x - self.Help.winfo_rootx() + self.Help.winfo_rootx())
        y = (event.y_root - self.y - self.Help.winfo_rooty() + self.Help.winfo_rooty())
        self.Help.geometry("+%s+%s" % (x, y))

    def frame_mapped(self, e):
        print(self, e)
        self.Help.update_idletasks()
        self.Help.overrideredirect(True)
        self.Help.state('normal')
