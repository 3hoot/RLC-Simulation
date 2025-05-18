import tkinter as tk
from utils import frameUtils as u


class variablesFrame(tk.LabelFrame):
    def __init__(
        self, parent, controller, labeltext: str, variables: tuple, entryWidth: int = 6
    ) -> None:
        super().__init__(parent, text=labeltext)
        self.controller = controller

        # create a label and entry for each variable
        for i, (name, var, desc) in enumerate(variables):
            entry = self._variableEntry(
                self, controller, name, var, desc, entryWidth=entryWidth
            )
            entry.grid(column=0, row=i, sticky="nsew", padx=3, pady=3)

    class _variableEntry(tk.Frame):

        def __init__(
            self,
            parent,
            controller,
            name: str,
            var: tk.Variable,
            desc: str,
            entryWidth: int,
        ) -> None:
            super().__init__(parent)
            self.controller = controller
            self.name = name
            self.var = var
            self.desc = desc

            label = tk.Label(self, text=name)
            label.grid(column=0, row=0, sticky="nsew")

            vcmd = (self.register(lambda P: u.check(type(var), P)), "%P")
            entry = tk.Entry(
                self,
                textvariable=var,
                validate="key",
                validatecommand=vcmd,
                width=entryWidth,
            )
            entry.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
            entry.bind(
                "<Return>",
                lambda event, v=var, e=entry: u.updateVal(self, v, e),
            )
            entry.bind(
                "<FocusOut>",
                lambda event, v=var, e=entry: u.updateVal(self, v, e),
            )

            description = tk.Label(self, text=desc)
            description.grid(column=2, row=0, sticky="nsew")
