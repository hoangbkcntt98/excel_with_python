import tkinter as tk
from tkinter import ttk
image_dir = '../resource/asset/images/'
root = tk.Tk()

root.title('Panda Importer')
# root.geometry('600x400+50+50')

window_width = 600  
window_height = 400

#get the screen dimension

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width /2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap(image_dir + 'panda.ico')



root.resizable(False, False)

root.mainloop()