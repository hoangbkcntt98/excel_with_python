import tkinter as tk
from tkinter import Menu
class MenuBar(tk.Menu):
    def __init__(self, container):
        super().__init__(container,background='lightblue', foreground='black',
               activebackground='#004c99', activeforeground='white')
        self.config(background="blue")
        # Declare file and edit for showing in menubar
        file = Menu(self, tearoff=False)
        edit = Menu(self, tearoff=False)

        # Add commands in in file menu
        file.add_command(label="New")
        file.add_command(label="Exit", command=container.quit)

        # Add commands in edit menu
        edit.add_command(label="Cut")
        edit.add_command(label="Copy")
        edit.add_command(label="Paste")

        # Display the file and edit declared in previous step
        self.add_cascade(label="File", menu=file)
        self.add_cascade(label="Edit", menu=edit)

