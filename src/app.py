import tkinter as tk
from frames import SettingsFrame, SimulationFrame, SignalFrame, BodeFrame
from utils import frameUtils as u
from signal_simulator import Signal
from circuit import Circuit


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Symulator obwodu RLC")

        # Variables
        self.simulationVars = (
            ("R1", tk.DoubleVar(value=10.0), "[kΩ]"),
            ("R2", tk.DoubleVar(value=10.0), "[kΩ]"),
            ("C1", tk.DoubleVar(value=10.0), "[μF]"),
            ("L1", tk.DoubleVar(value=10.0), "[mH]"),
        )

        self.settingVars = (
            (
                "N",
                tk.IntVar(value=100),
                ": Liczba punktów do obliczeń charakterystyki Bodego",
            ),
            (
                "log_omega_low",
                tk.IntVar(value=-30),
                ": Dolna granica częstotliwości [dB*rad/s]",
            ),
        )

        self.signalParams = (
            ("Długość sygnału", tk.IntVar(value=10), "[s]"),
            ("Krok czasowy", tk.DoubleVar(value=0.01), "[s]"),
            ("Częstotliwość", tk.DoubleVar(value=1.0), "[Hz]"),
            ("Amplituda", tk.DoubleVar(value=1.0), "[V]"),
        )

        self.dummySignal = Signal(
            int(self.signalParams[0][1].get() /
                self.signalParams[1][1].get()),
            self.signalParams[1][1].get(),
            self.signalParams[2][1].get(),
            self.signalParams[3][1].get(),
            None,
        )

        def signal_function_wrapper(self):
            self.circuit = Circuit(
                self.simulationVars[0][1].get() * (10**3),
                self.simulationVars[1][1].get() * (10**3),
                self.simulationVars[2][1].get() / (10**6),
                self.simulationVars[3][1].get() / (10**3),
                self.settingVars[0][1].get(),
                self.settingVars[1][1].get(),
            )
            self.signal = Signal(
                int(self.signalParams[0][1].get() /
                    self.signalParams[1][1].get()),
                self.signalParams[1][1].get(),
                self.signalParams[2][1].get(),
                self.signalParams[3][1].get(),
            )
            u.showFrame(self, SignalFrame)

        def bode_function_wrapper(self):
            self.circuit = Circuit(
                self.simulationVars[0][1].get() * (10**3),
                self.simulationVars[1][1].get() * (10**3),
                self.simulationVars[2][1].get() / (10**6),
                self.simulationVars[3][1].get() / (10**3),
                self.settingVars[0][1].get(),
                self.settingVars[1][1].get(),
            )
            u.showFrame(self, BodeFrame)

        self.buttons = (
            ("Symulacja odpowiedzi", lambda: signal_function_wrapper(self)),
            ("Charakterystyki Bodego", lambda: bode_function_wrapper(self)),
        )

        self.selectedFunction = tk.StringVar(value="")

        # Initialization
        container = tk.Frame(self)
        container.grid(column=0, row=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        # Menu bar
        self.option_add("*tearOff", False)
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        menu_bar.add_command(
            label="Symulacja", command=lambda: u.showFrame(self, SimulationFrame)
        )
        menu_bar.add_command(
            label="Ustawienia", command=lambda: u.showFrame(self, SettingsFrame)
        )

        # Frames
        self.frames = {}
        for frame_class in (SimulationFrame, SettingsFrame, SignalFrame, BodeFrame):
            frame = frame_class(container, self)
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        u.showFrame(self, SimulationFrame)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
