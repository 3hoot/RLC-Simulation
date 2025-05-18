import tkinter as tk
from frames.settings_frame import SettingsFrame
from frames.simulation_frame import SimulationFrame
from utils import frameUtils as u


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Symulator obwodu RLC")

        # Variables
        self.simulationVars = (
            ("R1", tk.DoubleVar(value=10.0), "kΩ"),
            ("R2", tk.DoubleVar(value=10.0), "kΩ"),
            ("C1", tk.DoubleVar(value=10.0), "μF"),
            ("L1", tk.DoubleVar(value=10.0), "mH"),
        )

        # self.settingsVars = {
        #     "N": tk.IntVar(value=100),
        #     "log_omega_low": tk.IntVar(value=100),
        # }

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
        for frame_class in (SimulationFrame, SettingsFrame):
            frame = frame_class(container, self)
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        u.showFrame(self, SimulationFrame)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
