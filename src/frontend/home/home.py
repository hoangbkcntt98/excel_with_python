import tkinter as tk
from tkinter import ttk
from logo_frame import LogoFrame
from src.frontend.csv.handle import CreateRecordFrame
from src.frontend.csv.import_frame import ImportFrame
from src.frontend.asset.style.styles import PandaStyle
from src.frontend.component.menu import MenuBar
from src.frontend.component.app import App
from src.backend.csv.csv_app import get_sheet_name
from src.config import __sr_width__
class ControlFrame(ttk.Frame):
    def __init__(self, container):

        super().__init__(container, height=400, width=__sr_width__)
        PandaStyle()

        self.container = container
        self.view_frame = 0
        self.sheet_name = get_sheet_name()
        self.data_csv = {
            "data":[],
            'header':[]
        }
        # initialize frames
        self.frames = {
            0: LogoFrame(container, self),
            1: CreateRecordFrame(container, self),
            2: ImportFrame(container,self)
        }

        self.change_frame()
        self.place(x=0, y=0)

    def change_frame(self):
        print('showing frame',self.view_frame)
        for f in self.frames.values():
            if f != self.frames[self.view_frame]:
                self.refresh_frame(f)
        frame = self.frames[self.view_frame]
        frame.tkraise()

    def refresh_frame(self, f):
        f.destroy()
        f.__init__(self.container, self)
    def update_frame(self, num_of_frame):
        frame = self.frames[num_of_frame]
        frame.destroy()
        frame.__init__(self.container,self)


class Home(App):
    def __init__(self, resizable= True):
        super().__init__(resizable)
        self.view_frame = 0
        self.__create_widgets()

    def __create_widgets(self):

        menubar = MenuBar(self)
        self.menubar = menubar
        self.config(menu=menubar)
        self.config(bg='white')

if __name__ == "__main__":
    app = Home()
    ControlFrame(app)
    app.mainloop()
