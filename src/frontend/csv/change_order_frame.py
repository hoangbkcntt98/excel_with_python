import tkinter as tk
from tkinter import ttk
from src.frontend.asset.style.styles import PandaStyle
from src.config import __sr_width__

class ChangeOrderFrame(ttk.Frame):
    def __init__(self, container, super_container, data):
        super().__init__(container, width=__sr_width__-45, height=100)
        PandaStyle()
        self.configure(style='bWhite.TFrame')
        self.container = container
        self.super_container = super_container

        self.headers = data['header']
        self._create()
        self.place(x=0, y=0)
        self.pack_propagate(0)
    def _destroy(self):
        for widget in self.winfo_children():
            widget.destroy()
    def _create(self):
        x_count = 0
        y_count = -1

        deleted_list = self.super_container.get_deleted_cols()
        headers = self.headers
        if len(deleted_list)>0:
            headers = [x for x in headers if not x in deleted_list]
        ordered_list = []
        for i in range(len(headers)):
            check = tk.StringVar()
            order_val = ttk.Combobox(
                self,
                values=headers,
                textvariable=check,
                width=8,
                state="readonly"
            )

            order_val.current(i)
            order_label = ttk.Label(
                master=self,
                text=i + 1,
            )
            if i % 5 == 0:
                y_count += 1
                x_count = 0
            order_label.place(x=x_count * 100, y=25 * y_count)
            order_val.place(x=x_count * 100 + 17, y=25 * y_count)
            ordered_list.append(check)
            x_count += 1
        self.super_container.order_list = ordered_list

