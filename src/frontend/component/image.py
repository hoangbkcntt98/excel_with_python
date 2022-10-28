
from PIL import Image, ImageTk

class PandaImage(ImageTk.PhotoImage):
    def __init__(self,path, zoom):
        self.path = path
        self.zoom = zoom
        image = Image.open(self.path)
        self.pixels_x, self.pixels_y = tuple([int(self.zoom * x) for x in image.size])
        super().__init__(image.resize((self.pixels_x, self.pixels_y)))
