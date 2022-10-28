import tkinter as tk
from tkinter import ttk
from src.config import __output_dir__
from src.config import  __sr_width__
from src.backend.csv.csv_app import read_data_from_csv, create_csv_from_list
from src.frontend.asset.style.styles import PandaStyle
from src.frontend.component.scrollable_frame import VerticalScrolledFrame
from src.frontend.component.tree_frame import TreeViewFrame
from .delete_column_frame import DeleteColumnFrame
from .change_order_frame import ChangeOrderFrame
from .tool_btn_frame import ToolBtnFrame
from .limit_row_frame import LimitRowFrame
class CreateRecordFrame(ttk.Frame):
    def __init__(self, container, control):
        super().__init__(container, width=__sr_width__, height=400)
        self.configure(style='bWhite.TFrame')
        PandaStyle()
        self.control = control
        self.check_list = []
        self.order_list = []
        self._skip_row = False
        self.show_frame = 0

        # read data
        self.data_csv = read_data_from_csv(__output_dir__ + 'output.csv')
        self._from_row = 0
        self._to_row = len(self.data_csv['data'])
        # tree view Frame
        self.treeview_frame = TreeViewFrame(self, self.data_csv)
        #add frame
        add_frame_wrapper = ttk.LabelFrame(self, width=__sr_width__ - 20, height=90, padding=5, text="Tools")
        add_frame_wrapper.pack()
        add_frame = VerticalScrolledFrame(add_frame_wrapper, width=__sr_width__-20, height=100, padding=5)
        add_frame.pack()
        add_frame.pack_propagate(0)
        self.frames = {
            0: DeleteColumnFrame(add_frame.interior, self, self.data_csv),
            1: ChangeOrderFrame(add_frame.interior,self,self.data_csv),
            2: LimitRowFrame(add_frame.interior, self,self.data_csv)
        }

        button_frame = ttk.Frame(self, width=__sr_width__ - 20, height=99)
        back_btn = ttk.Button(master=button_frame, text="Back", command=lambda : self.back())
        back_btn.place(x=0, y=20)
        html_btn = ttk.Button(master=button_frame,text="Make HTML")
        html_btn.place(x=190+100, y=20)
        csv_btn = ttk.Button(
            master=button_frame,
            text="Make CSV",
            command=lambda: self.to_csv()
        )
        csv_btn.place(x=190, y=20)
        button_frame.pack()
        button_frame.pack_propagate(0)

        # Tool Btn Frame
        tool_frame = ttk.Frame(self, width=__sr_width__ - 20, height=120,)
        ToolBtnFrame(tool_frame, self)
        tool_frame.pack(after=add_frame)
        tool_frame.pack_propagate(0)
        self.grid(column=0, row=0)
        self.change_frame()

    def back(self):
        self.control.view_frame = 0
        self.control.change_frame()
    def change_frame(self):
        frame = self.frames[self.show_frame]
        frame.tkraise()

    def change_mode(self, value):
        self.show_frame = value
        if value == 1:
            self.frames[1]._destroy()
            self.frames[1]._create()
        self.change_frame()

    def change_order(self):
        self.show_frame = 1
        ordered_list = [x.get() for x in self.order_list]
        print('order',ordered_list)
        self.treeview_frame.update_table()
        self.change_frame()

    def apply_mode(self, val):
        print('apply', val)
        val = val.get()
        if val == 1:
            self.change_order()
        elif val ==0 :
            self.delete_cols()
        elif val == 2:
            self.limit_row()

    def limit_row(self):
        self.treeview_frame.update_table()

    def delete_cols(self):
        del_list = [x.get() for x in self.check_list if x.get() != '']
        print('del', del_list)
        self.treeview_frame.del_cols(del_list)
    def get_deleted_cols(self):
        return [x.get() for x in self.check_list]
    def get_ordered_cols(self):
        return [x.get() for x in self.order_list]
    def get_limit(self):
        print(self._skip_row)
        return [self._from_row, self._to_row]
    def get_skip_row(self):
        return self._skip_row
    def to_csv(self):
        # tree = self.treeview_frame.mytree
        ordered = [x.get() for x in self.order_list]
        deleted = [x.get() for x in self.check_list]
        limit = [self._from_row, self._to_row]
        skip = self.get_skip_row()
        data = read_data_from_csv(__output_dir__+'output.csv',ordered_columns=ordered,deleted_columns=deleted, limit = limit, skip=skip)
        create_csv_from_list(__output_dir__+'handled_data.csv',data['data'])

    def all_columns(self):
        return [x.get() for x in self.check_list]

    def show_result(self):
        print([x.get() for x in self.check_list])
