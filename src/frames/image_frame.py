import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os


class imageFrame(tk.LabelFrame):
    def __init__(
        self,
        parent,
        controller,
        labeltext: str,
        imagepath: str,
        padX: int = 5,
        padY: int = 5,
        scaleX: int = 400,
        scaleY: int = 200,
    ) -> None:

        super().__init__(parent, text=labeltext)
        self.controller = controller
        self.imagepath = imagepath
        self.padX = padX
        self.padY = padY
        self.scaleX = scaleX
        self.scaleY = scaleY

        # sizing elements
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # load and display the image
        with open(imagepath, "rb") as img_file:
            self.imagePIL = Image.open(img_file)
            self.imagePIL = self.imagePIL.resize((self.scaleX, self.scaleY))
            self.image = ImageTk.PhotoImage(self.imagePIL)

            self.label = tk.Label(self, image=self.image)
            self.label.grid(column=0, row=0, sticky="nsew", padx=padX, pady=padY)
