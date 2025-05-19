import tkinter as tk
from .variables_frame import variablesFrame


class SignalFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        pass
