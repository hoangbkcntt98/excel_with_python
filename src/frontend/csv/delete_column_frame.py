import tkinter as tk
from tkinter import ttk
from src.config import __sr_width__
from src.frontend.asset.style.styles import PandaStyle
class DeleteColumnFrame(ttk.Frame):
    def __init__(self, container, super_container, data):
        super().__init__(container, width=__sr_width__-45, height=150)
        PandaStyle()
        self.configure(style='bWhite.TFrame')


        headers = data['header']
        x_count = 0
        y_count = -1

        for i in range(len(headers)):
            check = tk.StringVar()
            checkbox = ttk.Checkbutton(
                master=self,
                text=headers[i],
                variable=check,
                command=super_container.show_result,
                onvalue=headers[i],
                offvalue="",
                style="TCheckbutton"

            )
            if i % 5 == 0:
                y_count += 1
                x_count = 0
            checkbox.place(x=x_count * 100, y=20 * y_count)
            super_container.check_list.append(check)
            x_count += 1


        self.pack()
        self.place(x=0, y=0)
        self.pack_propagate(0)