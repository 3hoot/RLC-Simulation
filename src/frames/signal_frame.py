import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class SignalFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        container = tk.LabelFrame(self, text="Odpowiedź układu na sygnał")
        container.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

        # degug text
        debug_text = tk.Text(container, height=5, width=50)
        debug_text.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        debug_text.insert(tk.END, "Debug text\n")
