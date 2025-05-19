import tkinter as tk


class ButtonsFrame(tk.Frame):
    def __init__(self, parent, controller, buttons: tuple) -> None:
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)

        # create a button for each variable
        for i, (name, command) in enumerate(buttons):
            button = tk.Button(
                self,
                text=name,
                command=command,
            )
            button.grid(column=i, row=0, sticky="nsew", padx=3, pady=3)
            self.grid_columnconfigure(i, weight=1)
