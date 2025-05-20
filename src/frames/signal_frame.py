import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class SignalFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = tk.LabelFrame(self, text="Odpowiedź układu na sygnał")
        container.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Input signal plot
        input_fig = Figure(figsize=(12, 3), dpi=80)
        self.input_plot = input_fig.add_subplot(111)
        self.input_canvas = FigureCanvasTkAgg(input_fig, master=container)
        self.input_canvas.draw()
        self.input_canvas.get_tk_widget().grid(
            column=0, row=0, sticky="nsew", padx=5, pady=5
        )

    def update_plot(self):
        # Check if circuit exists
        if not hasattr(self.controller, "circuit"):
            return

        choosen_signal = self.controller.selectedFunction.get()
        y_func = self.controller.signal.functionManifest.get(choosen_signal)
        y_func()
        y = self.controller.signal.inputSignal
        x = self.controller.signal.timeRange

        # Input signal plot
        self.input_plot.clear()
        self.input_plot.set_title("Sygnał wejściowy")
        self.input_plot.set_xlabel("Czas [s]")
        self.input_plot.set_ylabel("Amplituda [V]")
        self.input_plot.plot(x, y)
        self.input_plot.grid()
        self.input_canvas.draw()
