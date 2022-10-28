
from src.config import  __image_dir__
def center(screen, title = "", width = 600, height = 400, resizable = False):
    if title != "":
        screen.title(title)
    screen.iconbitmap(__image_dir__ +'panda.ico')
    window_width = width  
    window_height = height
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
    center_x = int(screen_width /2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    if not resizable:
        screen.resizable(False, False)