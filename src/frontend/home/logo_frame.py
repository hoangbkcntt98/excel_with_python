import tkinter as tk 
from tkinter import Canvas, ttk
from src.frontend.component.image import PandaImage
from src.config import __image_dir__, __sr_width__,__base_font__, __output_dir__
from src.frontend.component.util import align_center
from button_frame import ButtonFrame
from src.frontend.asset.style.styles import PandaStyle
from tkinter.messagebox import showinfo, showerror
from src.backend.csv.csv_app import read_execl_file, to_csv, read_data_from_csv
from tkinter import filedialog as fd
import os.path
class LogoFrame(ttk.Frame):
    def __init__(self,container, control):
        super().__init__(container, width=__sr_width__,height=400)
        PandaStyle()
        self.config(style="bBlue.TFrame")
        canvas = Canvas(self, width=__sr_width__, height=300, bg="white")
        canvas.create_text(canvas.winfo_reqwidth()/2,40, text="Hello, Panda!", font=__base_font__)
        img = PandaImage(__image_dir__+'panda.jpg',0.4)
        self.img = img # to prevent the image garbage collected.
        left, top = align_center(canvas)
        canvas.create_image(left, top, image=img)

        canvas.create_text(left,top+70, text="@copyright by hoangbk")

        canvas.grid(row=0,column=0)
        ButtonFrame(self, control)
        self.place(x=0,y=0)
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
        if filenames:
            filepath = os.path.abspath(filenames.name)
            res = read_execl_file(filepath)
            new_file_path = __output_dir__+'output.csv'
            to_csv(new_file_path, res['data_frame'])
            read_data_from_csv(new_file_path)

        if res:
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
        control.view_frame = 1
        control.change_frame()

