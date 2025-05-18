import tkinter as tk


class SettingsFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller
        self.label = tk.Label(self, text="Settings Frame")
        self.label.grid(column=0, row=0, sticky="nsew")
