import tkinter as tk
from tkinter import Canvas, Frame, ttk
from PIL import Image, ImageTk
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


image = Image.open(image_dir+'panda.jpg')
root.resizable(False, False)

frame = Frame(root, bg="white", width=600, height=300)
frame.pack()

canvas = Canvas(frame, bg = "white", width=600, height=300)
canvas.pack()


zoom = 0.4
pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
canvas.create_image(300, 100, image=img)

canvas.create_text(300,200,text="@Copyright by Heo")

frame_1 = Frame(root, bg="white", width=600, height=100)
frame_1.pack()
text = tk.StringVar()
textbox = ttk.Entry(frame_1, textvariable=text, justify='center')
textbox.pack()

root.mainloop()