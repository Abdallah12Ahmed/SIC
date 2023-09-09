import tkinter as tk
from tkinter import messagebox
import main

class HomePage:
    def __init__(self):
        self.root=tk.Tk()

        self.Sports=tk.Button(self.root,text='Spots')
        self.Sports.pack()

        self.Home_appliances = tk.Button(self.root, text='Home appliances')
        self.Home_appliances.pack()

        self.Electronics = tk.Button(self.root, text='Electronics')
        self.Electronics.pack()

        self.Fashion = tk.Button(self.root, text='Fashion')
        self.Fashion.pack()

        self.Books = tk.Button(self.root, text='Books')
        self.Books.pack()



        self.root.mainloop()





HomePage()