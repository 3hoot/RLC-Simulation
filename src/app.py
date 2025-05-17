import tkinter as tk


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Symulator obwodu RLC")

        # Initialization
        container = tk.Frame(self)
        container.grid(column=0, row=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Menu bar
        self.option_add('*tearOff', False)
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        menu_bar.add_command(
            label="Symulacja", command=lambda: self._show_frame(self._SimulationFrame))
        menu_bar.add_command(
            label="Ustawienia", command=lambda: self._show_frame(self._SettingsFrame))

        # Frames
        self.frames = {}
        for frame_class in (self._SimulationFrame, self._SettingsFrame):
            frame = frame_class(container, self)
            self.frames[frame_class] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self._show_frame(self._SimulationFrame)

    def _show_frame(self, frame_class) -> None:
        frame = self.frames[frame_class]
        frame.tkraise()

    class _SimulationFrame(tk.Frame):
        def __init__(self, parent, controller) -> None:
            super().__init__(parent)
            self.controller = controller
            self.label = tk.Label(self, text="Simulation Frame")
            self.label.grid(column=0, row=0, sticky="nsew")

    class _SettingsFrame(tk.Frame):
        def __init__(self, parent, controller) -> None:
            super().__init__(parent)
            self.controller = controller
            self.label = tk.Label(self, text="Settings Frame")
            self.label.grid(column=0, row=0, sticky="nsew")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
