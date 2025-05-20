import tkinter as tk
from PIL import Image, ImageTk


class imageFrame(tk.LabelFrame):
    def __init__(
        self,
        parent,
        controller,
        labeltext: str,
        imagepath: str,
        padX: int = 5,
        padY: int = 5,
        dimensionX: int = 400,
        dimensionY: int = 200,
    ) -> None:

        super().__init__(parent, text=labeltext)
        self.controller = controller
        self.imagepath = imagepath
        self.padX = padX
        self.padY = padY
        self.dimensionX = dimensionX
        self.dimensionY = dimensionY

        # sizing elements
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # load and display the image
        with open(imagepath, "rb") as img_file:
            self.imagePIL = Image.open(img_file)
            self.imagePIL = self.imagePIL.resize((self.dimensionX, self.dimensionY))
            self.image = ImageTk.PhotoImage(self.imagePIL)

            self.label = tk.Label(self, image=self.image)
            self.label.grid(column=0, row=0, sticky="nsew", padx=padX, pady=padY)
