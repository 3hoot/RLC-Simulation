import tkinter as tk
from .variables_frame import variablesFrame
from .image_frame import imageFrame
from .buttons_frame import ButtonsFrame


class SimulationFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        schematic_frame = imageFrame(
            self,
            controller,
            labeltext="Schemat układu RLC",
            imagepath="assets/schematic.png",
            dimensionX=800,
            dimensionY=400,
        )
        schematic_frame.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        simulationVars_frame = variablesFrame(
            self,
            controller,
            "Parametry układu RLC",
            controller.simulationVars,
            entryWidth=8,
            gridDimension=(1, 1, 1),
        )
        simulationVars_frame.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)

        buttons_frame = ButtonsFrame(self, controller, controller.buttons)
        buttons_frame.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=5, pady=5)
