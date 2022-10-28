import tkinter as tk
from src.frontend.component.screen import center
class App(tk.Tk):
    def __init__(self, resizable = True):
        super().__init__()
        center(self, title = "Panda Importer", resizable=resizable)