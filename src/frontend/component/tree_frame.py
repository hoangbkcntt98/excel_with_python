import tkinter as tk
from tkinter import ttk
from src.config import __sr_width__, __output_dir__
from src.backend.csv.csv_app import read_data_from_csv
class TreeViewFrame(ttk.Frame):
    def __init__(self, container, data_csv):
        super().__init__(container, width=__sr_width__, height=160)
        self.container = container
        self.ordered_column = False
        self.data_csv = data_csv
        self.create_tree()

    def create_tree(self):
        data = self.data_csv['data']
        headers = self.data_csv['header']

        # treeview frame

        self.pack_propagate(False)
        self.pack()
        # treeview
        style = ttk.Style()
        style.configure("Treeview",
                        font=(None, 10),
                        rowheight=int(10 * 2.5))

        scrollbarx = tk.Scrollbar(self, orient="horizontal")
        scrollbary = tk.Scrollbar(self, orient="vertical")
        self.mytree = ttk.Treeview(self, show="headings", padding=0)
        self.mytree.place(width=__sr_width__ - 30, height=140)

        scrollbary.place(relx=0.97, rely=0.001, width=20, height=160)
        scrollbarx.place(relx=0.002, rely=0.922, width=__sr_width__, height=20)

        self.mytree.configure(xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        scrollbarx.configure(command=self.mytree.xview)
        scrollbary.configure(command=self.mytree.yview)

        self.mytree.configure(
            columns=tuple(headers)
        )
        for d in data:
            self.mytree.insert('', tk.END, values=d)
        for i in range(len(headers)):
            self.mytree.heading(i, text=headers[i], anchor="w")
            if i < 4:
                self.mytree.column(i, width=60)
            elif i == len(headers) - 1:
                self.mytree.column(i, width=240)
            else:
                self.mytree.column(i, width=120)


    def del_cols(self, del_list):
        display_columns = []
        for col in self.mytree["columns"]:
            if col not in del_list:
                display_columns.append(col)
        self.mytree['displaycolumns'] = display_columns
        self.mytree.update()
    def update_table(self, columns):
        if columns:
            self.ordered_column = columns
            self.clear_all()
            self.data_csv = read_data_from_csv(__output_dir__+'output.csv', ordered_columns=columns, deleted_columns=self.container.get_deleted_cols())
            print('updated_data', self.data_csv )
            self.create_tree()
        else:
            print('nothing for update')

    def clear_all(self):
        print('delete_all')
        for item in self.mytree.get_children():
            self.mytree.delete(item)