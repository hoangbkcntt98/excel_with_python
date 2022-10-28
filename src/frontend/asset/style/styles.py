import tkinter as tk
from tkinter import ttk

class PandaStyle(ttk.Style):
    def __init__(self):
        super().__init__()
        #checkbox button
        self.configure('TRadiobutton', background="white")
        self.configure('TLabel', background="white")
        self.configure('TFrame', background="white")
        self.configure('bWhite.TFrame', background="white")
        self.configure('bBlue.TFrame', background="#F0F8FF")
        self.configure('bBlue.TCheckbutton', background="#F0F8FF")
        self.configure('bBlue.TRadiobutton', background="#F0F8FF")
        self.configure('TCheckbutton', background="white")
