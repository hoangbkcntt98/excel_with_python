import tkinter as tk
from tkinter import ttk
from src.config import __sr_width__
class ToolBtnFrame(ttk.Frame):
    def __init__(self, container, super_container):
        super().__init__(container, width=__sr_width__, height=70)
        self.configure(style='bBlue.TFrame')
        self.place(x=0,y=70)
        self.selected_value = tk.IntVar()
        ttk.Radiobutton(
            container,
            text='Delete Columns',
            style="bBlue.TRadiobutton",
            value=0,
            variable=self.selected_value,
            command=lambda : super_container.change_mode(0)).grid(column=0, row=0, padx=5)
        ttk.Radiobutton(
            container,
            text='Order Columns',
            style="bBlue.TRadiobutton",
            value=1,
            variable=self.selected_value,
            command=lambda :super_container.change_mode(1)).grid(column=1, row=0, padx=5)
        ttk.Radiobutton(
            container,
            text='Handle Rows',
            style="bBlue.TRadiobutton",
            value=2,
            variable=self.selected_value,
            command=lambda: super_container.change_mode(2)).grid(column=2, row=0, padx=5)
        apply_btn = ttk.Button(
            master=container,
            text="Apply",
            command=lambda :super_container.apply_mode(self.selected_value)
        )
        apply_btn.grid(row=0, column=3, padx=5,columnspan=2)


