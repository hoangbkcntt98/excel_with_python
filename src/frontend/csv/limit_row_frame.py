import tkinter as tk
from tkinter import ttk
from src.config import __sr_width__
from src.frontend.asset.style.styles import PandaStyle
class LimitRowFrame(ttk.Frame):
    def __init__(self, container, super_container, data):
        super().__init__(container, width=__sr_width__-45, height=150)
        PandaStyle()
        self.configure(style='bWhite.TFrame')
        self.pack()
        self.place(x=0, y=0)
        self.pack_propagate(0)