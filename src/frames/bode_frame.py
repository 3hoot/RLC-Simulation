import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class BodeFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = tk.LabelFrame(self, text="Charakterystyki Bodego")
        container.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Amplitude plot
        amplitude_fig = Figure(figsize=(6, 5), dpi=80)
        self.amplitude_plot = amplitude_fig.add_subplot(111)
        self.amplitude_canvas = FigureCanvasTkAgg(amplitude_fig, master=container)
        self.amplitude_canvas.draw()
        self.amplitude_canvas.get_tk_widget().grid(
            column=0, row=0, sticky="nsew", padx=5, pady=5
        )

        # Phase plot
        phase_fig = Figure(figsize=(6, 5), dpi=80)
        self.phase_plot = phase_fig.add_subplot(111)
        self.phase_canvas = FigureCanvasTkAgg(phase_fig, master=container)
        self.phase_canvas.draw()
        self.phase_canvas.get_tk_widget().grid(
            column=1, row=0, sticky="nsew", padx=5, pady=5
        )

        # Information text
        self.info_label = tk.Label(container)
        self.info_label.grid(
            column=0, row=1, columnspan=2, sticky="nsew", padx=5, pady=5
        )

    def update_plot(self):
        # Check if circuit exists
        if not hasattr(self.controller, "circuit"):
            return

        x = self.controller.circuit.omega_range

        # Amplitude plot
        self.amplitude_plot.clear()
        self.amplitude_plot.set_title("Charakterystyka amplitudowa")
        self.amplitude_plot.set_xlabel("Pulsacja [rad/s]")
        self.amplitude_plot.set_ylabel("Wzmocnienie [dB]")
        y_amp = self.controller.circuit.Bode_Amplification()
        self.amplitude_plot.plot(x, y_amp)
        self.amplitude_plot.grid()
        self.amplitude_plot.set_xscale("log")
        self.amplitude_canvas.draw()

        # Phase plot
        self.phase_plot.clear()
        self.phase_plot.set_title("Charakterystyka fazowa")
        self.phase_plot.set_xlabel("Pulsacja [rad/s]")
        self.phase_plot.set_ylabel("Faza [rad]")
        y_phase = self.controller.circuit.Bode_Phase()
        self.phase_plot.plot(x, y_phase)
        self.phase_plot.grid()
        self.phase_plot.set_xscale("log")
        self.phase_canvas.draw()

        # Update info text
        info_text = (
            f"R1 = {self.controller.simulationVars[0][1].get()} [kΩ], "
            + f"R2 = {self.controller.simulationVars[1][1].get()} [kΩ], "
            + f"C1 = {self.controller.simulationVars[2][1].get()} [μF], "
            + f"L1 = {self.controller.simulationVars[3][1].get()} [H]"
        )
        self.info_label.config(text=info_text)
