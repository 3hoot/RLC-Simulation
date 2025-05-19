import tkinter as tk
from .variables_frame import variablesFrame


class SettingsFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # frame for the Bode plot settings
        settingVars_frame = variablesFrame(
            self,
            controller,
            "Ustawienia charakterystyki Bodego",
            controller.settingVars,
            entryWidth=5,
            gridDimension=(1, 1, 2),
        )
        settingVars_frame.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        # frame for the signal response settings
        signalList_frame = tk.LabelFrame(self, text="Rodzaj funkcji do symulacji")
        signalList_frame.grid(column=0, row=2, sticky="nsew", padx=5, pady=5)
        signalList = tk.Listbox(
            signalList_frame,
            listvariable=tk.Variable(
                value=[
                    str(k) for k in controller.dummySimulator.functionManifest.keys()
                ]
            ),
            selectmode=tk.SINGLE,
            height=5,
            exportselection=False,
        )
        signalList.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        # Lazy implementation of the signal response settings
        def on_select(event):
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                value = event.widget.get(index)
                controller.selectedFunction.set(value)

        signalList.bind("<<ListboxSelect>>", on_select)

        signalParams_frame = variablesFrame(
            self,
            controller,
            "Parametry funkcji do symulacji",
            controller.signalParams,
            entryWidth=5,
            gridDimension=(1, 1, 2),
        )
        signalParams_frame.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

        # frame for the description
        description = tk.Label(
            self, text="Autorzy programu: Mikołaj Kuryło & Piotr Kujawski"
        )
        description.grid(column=0, row=3, sticky="nsew", padx=5, pady=5)
