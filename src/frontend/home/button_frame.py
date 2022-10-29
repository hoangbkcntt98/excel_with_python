import os.path
from tkinter import ttk
from src.config import  __sr_width__, __output_dir__
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showerror
from src.backend.csv.csv_app import read_execl_file, to_csv, read_data_from_csv, check_exist_file
from src.frontend.asset.style.styles import PandaStyle
class ButtonFrame(ttk.Frame):
    def __init__(self, container, control):
        super().__init__(container,width=__sr_width__, height=100)
        self.configure(style="bWhite.TFrame")
        PandaStyle()
        self.container = container
        self.control = control
        self.data = None
        import_btn = ttk.Button(
            self,
            text="Generate Data",
            command=self.hanle_import
        )
        import_btn.grid(column=0,row =0, padx=5)
        review_btn = ttk.Button(
            self,
            text="Edit Data",
            command=lambda :self.review_data(self.control)
        )
        review_btn.grid(column=1,row =0,padx=5,pady=20)
        exit_btn = ttk.Button(
            self, text="Other")
        exit_btn.grid(column=2,row =0, padx=5, pady=20)
        self.grid(row=1, column =0)
        self.pack_propagate(0)

    def hanle_import(self):
        self.control.view_frame = 2
        self.control.change_frame()


    def select_files(self):
        print('import')
        filetypes = (
            ('Excel 2016', '*.xlsx'),
            ('Csv', '*.csv'),
            ('Excel', '*.xls'),
        )

        filenames = fd.askopenfile(
            title='Read file',
            initialdir='/',
            filetypes=filetypes)
        res = {}
        data_csv = []
        if filenames:
            filepath = os.path.abspath(filenames.name)
            res = read_execl_file(filepath)
            new_file_path = __output_dir__+'output.csv'
            to_csv(new_file_path, res['data_frame'])
        if res:
            self.control.data_csv = read_data_from_csv(__output_dir__ + 'output.csv')
            self.control.update_frame(1)
            showinfo(
                title='Read file',
                message='Read file successfully ! \n' + filepath
            )
        else:
            showerror(
                title="Error",
                message="cannot reading file"
            )

    def review_data(self,control):
        if check_exist_file(__output_dir__+'output.csv'):

            control.view_frame = 1
            control.change_frame()
        else:
            showerror("Empty File", message="Please Import A File!!!")