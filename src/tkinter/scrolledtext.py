import tkinter as tk
from tkinter.scrolledtext import ScrolledText


root = tk.Tk()
root.title("ScrolledText Widget")


st = ScrolledText(root, width=50,  height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()