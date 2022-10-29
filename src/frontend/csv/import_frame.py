import tkinter as tk
from tkinter import Canvas, ttk
from src.frontend.component.image import PandaImage
from src.config import __image_dir__, __sr_width__,__base_font__, __output_dir__, __sr_height__
from src.frontend.asset.style.styles import PandaStyle
from tkinter.messagebox import showinfo, showerror
from src.backend.csv.csv_app import get_excel_info, to_csv, read_data_from_csv, read_execl_file, create_csv_from_list
from tkinter import filedialog as fd
import os.path
from src.util.util_string import get_string
import pandas as pd
class ImportFrame(ttk.Frame):
    def __init__(self, container, control):
        super().__init__(container, width=__sr_width__, height=400)
        self.pack_propagate(False)
        self.configure(style='bWhite.TFrame')
        PandaStyle()
        self.control = control
        self.container = container
        self.frame = tk.LabelFrame(self, width=__sr_width__, height=300, bg="white", text="Import/Update Data")
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.sheet_name = tk.StringVar()
        self.limit_columns = tk.StringVar()
        self.skip_rows = tk.StringVar()
        self.file_path = False

        sheet_label = ttk.Label(
            master=self.frame,
            text='\n1. Click Get Information, choose your file\n2. Choose Sheet name (Required) \n3. Enter Limit Columns (Optional)\n4. Enter Skip rows (Optinal)\n5. Click Import/Update'
        )
        sheet_label.place(x= 10, y =0)


        get_info_btn = ttk.Button(
            master=self.frame,
            text="Get Excel Information",
            command=self.get_info
        )
        get_info_btn.place(x= 10,y = 100)

        #button frame
        self.btn_frame = ttk.Frame(
            master=self,
            width=__sr_width__,
            height=100,

        )
        back_btn = ttk.Button(
            master=self.btn_frame,
            text="Back",
            command=self.back
        )
        back_btn.place(x=10, y = 20)


        self.btn_frame.pack_propagate(False)
        self.btn_frame.place(x = 0, y=300)

        self.place(x=0, y=0)

    def back(self):
        self.control.view_frame = 0
        self.control.change_frame()
    def get_info(self):
        print('Get Information')
        filetypes = (
            ('Excel 2016', '*.xlsx'),
            ('Csv', '*.csv'),
            ('Excel', '*.xls'),
        )

        filenames = fd.askopenfile(
            title='Read file',
            initialdir='/',
            filetypes=filetypes)
        if filenames:
            filepath = os.path.abspath(filenames.name)
            res = get_excel_info(filepath)
            self.file_path = res['file_path']

            path_label = ttk.Label(
                text="File: "+res['file_path']
            )
            path_label.place(x=150, y =120)

            sheet_name_label = ttk.Label(
                text="Sheet Name",
                master=self.frame
            )
            sheet_name_label.place(x =10, y = 150)
            sheet_cb = ttk.Combobox(
                self.frame,
                textvariable=self.sheet_name,
                state="readonly"
            )
            sheet_cb['values'] = res['sheet_name']
            sheet_cb.place(x=100, y =150)

            limit_column_label = ttk.Label(
                master=self.frame,
                text="Limit Columns"
            )
            limit_column_entry = ttk.Entry(
                master=self.frame,
                textvariable=self.limit_columns
            )
            limit_column_help = ttk.Label(
                master=self.frame,
                text="Eg:Enter B:K for columns from B to K"
            )
            limit_column_label.place(x =10, y = 200, width=100)
            limit_column_entry.place(x=100, y =200, width=50)
            limit_column_help.place(x = 150, y=200)

            skip_row_label = ttk.Label(
                master=self.frame,
                text="Skip Rows :"
            )
            skip_row_entry = ttk.Entry(
                master=self.frame,
                textvariable=self.skip_rows
            )
            skip_row_help = ttk.Label(
                master=self.frame,
                text="Eg: 1,2 for skip row 1st and 2nd "
            )
            skip_row_label.place(x=10, y=250)
            skip_row_entry.place(x=100, y=250, width=50)
            skip_row_help.place(x=150, y=250)

            import_update_btn = ttk.Button(
                master=self.btn_frame,
                text="Import/Update",
                command=self.import_update_data
            )
            import_update_btn.place(x=250, y=20, width=100)
    def import_update_data(self):
        sheet_name = get_string(self.sheet_name)
        skip_rows = get_string(self.skip_rows)
        limit_columns = get_string(self.limit_columns)
        if skip_rows:
            skip_rows = skip_rows.split(',')
        if not sheet_name:
            showerror("Import Data Error", message="Sheet Name: Cannot Empty!!")
        else:
            res = read_execl_file(path=self.file_path,sheet=sheet_name,reading_cols=limit_columns,unness_rows=skip_rows)
            new_file_path = __output_dir__ + 'output.csv'
            to_csv(new_file_path, res['data_frame'])
            if res:
                self.control.data_csv = read_data_from_csv(__output_dir__ + 'output.csv')
                self.control.update_frame(1)
                self.control.sheet_name = sheet_name
                create_csv_from_list(__output_dir__+'file_info.csv', [[sheet_name,skip_rows,limit_columns]])
                showinfo(
                    title='Read file',
                    message='Read file successfully ! \n' + self.file_path
                )
            else:
                showerror(
                    title="Error",
                    message="cannot reading file"
                )







