import tkinter as tk
from .variables_frame import variablesFrame
from .image_frame import imageFrame


class SimulationFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        schematic_frame = imageFrame(
            self,
            controller,
            labeltext="Schemat układu RLC",
            imagepath="assets/schematic.png",
        )
        schematic_frame.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        simVars_frame = variablesFrame(
            self,
            controller,
            "Parametry symulacji",
            controller.simulationVars,
            entryWidth=6,
        )
        simVars_frame.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
