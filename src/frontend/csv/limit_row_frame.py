import tkinter as tk
from tkinter import ttk
from src.config import __sr_width__
from src.frontend.asset.style.styles import PandaStyle
from src.util.util_string import list_str_to_int
class LimitRowFrame(ttk.Frame):
    def __init__(self, container, super_container, data):
        super().__init__(container, width=__sr_width__-45, height=150)
        PandaStyle()
        self.configure(style='bWhite.TFrame')
        self.super_container = super_container

        max_row = len(data['data'])-1
        _from_value = tk.IntVar(value=1)
        _from_label = ttk.Label(
            master=self,
            text='From row',
            width=50
        )
        _from_label.place(x=50, y=50)
        _from = ttk.Entry(
            master=self,
            textvariable=_from_value,
        )
        _from.place(x=110, y = 50, width=50)

        _to_value = tk.IntVar(value=max_row+1)
        _to_label = ttk.Label(
            master=self,
            text='To row',
            width=50
        )
        _to_label.place(x=200, y=50)
        _to = ttk.Entry(
            master=self,
            textvariable=_to_value
        )
        _to.place(x=250, y=50, width=50)

        _skip_value = tk.StringVar()
        _skip_label = ttk.Label(
            master=self,
            text="Skip rows"
        )
        _skip = ttk.Entry(
            master=self,
            textvariable=_skip_value
        )
        _skip_help = ttk.Label(
            master=self,
            text="Eg: 1,2,3"
        )
        _skip_label.place(x=50, y = 0)
        _skip.place(x=120, y =0, width=150)
        _skip_help.place(x=280, y =0)

        _set_btn = tk.Button(
            master=self,
            text="Set",
            command= lambda : self.set_var(_from_value,_to_value, _skip_value),
            bg='blue',
            fg='white',
        )
        _set_btn.place(x= 350, y =0, width=40)

        warning_label = ttk.Label(
            master=self,
            text="(You need click 'Set' before 'Apply')"
        )
        warning_label.place(x = 350, y = 30 )
        self.pack()
        self.place(x=0, y=0)
        self.pack_propagate(0)
    def set_var(self, _from_row, _to_row, _skip_value):
        skip_list = _skip_value.get().split(',')
        self.super_container._skip_row = list_str_to_int(skip_list)
        self.super_container._from_row = _from_row.get()-1
        self.super_container._to_row = _to_row.get()-1
