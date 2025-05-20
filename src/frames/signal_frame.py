import tkinter as tk
import numpy as np
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
        container.grid_rowconfigure(1, weight=1)

        # Input signal plot
        input_fig = Figure(figsize=(1, 3), dpi=60)
        self.input_plot = input_fig.add_subplot(111)
        self.input_canvas = FigureCanvasTkAgg(input_fig, master=container)
        self.input_canvas.draw()
        self.input_canvas.get_tk_widget().grid(
            column=0, row=0, sticky="nsew", padx=2, pady=2
        )

        # Output signal plot
        output_fig = Figure(figsize=(1, 3), dpi=60)
        self.output_plot = output_fig.add_subplot(111)
        self.output_canvas = FigureCanvasTkAgg(output_fig, master=container)
        self.output_canvas.draw()
        self.output_canvas.get_tk_widget().grid(
            column=0, row=1, sticky="nsew", padx=2, pady=2
        )

    def update_plot(self):
        # Check if circuit exists
        if not hasattr(self.controller, "circuit"):
            return

        choosen_signal = self.controller.selectedFunction.get()
        if choosen_signal == "":
            y_input = np.zeros(len(self.controller.signal.timeRange))
        else:
            y_func = self.controller.signal.functionManifest.get(
                choosen_signal)
            y_func()
            y_input = self.controller.signal.inputSignal
        x = self.controller.signal.timeRange

        # Input signal plot
        self.input_plot.clear()
        self.input_plot.set_xlim(
            self.controller.signal.timeRange[0],
            self.controller.signal.timeRange[-1],
        )
        self.input_plot.set_title("Sygnał wejściowy")
        self.input_plot.set_xlabel("Czas [s]")
        self.input_plot.set_ylabel("Amplituda [V]")
        self.input_plot.plot(x, y_input)
        self.input_plot.grid()
        self.input_plot.figure.tight_layout()
        self.input_canvas.draw()

        y_output = self.controller.circuit.response(
            y_input, self.controller.signal.timeStep)

        # Output signal plot
        self.output_plot.clear()
        self.output_plot.set_xlim(
            self.controller.signal.timeRange[0],
            self.controller.signal.timeRange[-1],
        )
        self.output_plot.set_title("Odpowiedź układu")
        self.output_plot.set_xlabel("Czas [s]")
        self.output_plot.set_ylabel("Amplituda [V]")
        self.output_plot.plot(x, y_output)
        self.output_plot.grid()
        self.output_plot.figure.tight_layout()
        self.output_canvas.draw()
