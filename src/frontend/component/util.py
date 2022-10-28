def align_center(widget):
    widget.update()
    c_width = widget.winfo_reqwidth()
    c_height = widget.winfo_reqheight()
    left = int(c_width / 2)
    top = int(c_height / 2)
    return left, top
