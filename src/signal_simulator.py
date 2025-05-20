import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Signal:
    def __init__(
        self,
        signalLength: int,
        timeStep: float,
        frequency: float,
        amplitude: float = 1.0,
        inputSignal: np.array = None,
    ) -> None:
        self.signalLength = signalLength
        self.timeStep = timeStep
        self.frequency = frequency
        self.amplitude = amplitude
        self.inputSignal = (
            inputSignal if inputSignal is not None else np.zeros(signalLength)
        )

        self.functionManifest = {
            "Sinus": self.sine,
            "Prostokątny": self.square,
            "Piłokształtny": self.sawtooth,
            "Trójkątny": self.triangle,
        }

        self.timeRange = np.array(
            [t * self.timeStep
             for t in range(self.signalLength)], dtype=float
        )

    def sine(self) -> None:
        self.inputSignal = np.array(
            [self.amplitude * np.sin(2 * np.pi * self.frequency * t * self.timeStep)
                for t in range(self.signalLength)]
        )

    def square(self) -> None:
        self.inputSignal = np.array(
            [self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * t * self.timeStep))
                for t in range(self.signalLength)]
        )

    def sawtooth(self) -> None:
        self.inputSignal = np.array(
            [self.amplitude * (2 * (t * self.timeStep * self.frequency - np.floor(t * self.timeStep * self.frequency + 0.5)))
                for t in range(self.signalLength)]
        )

    def triangle(self) -> None:
        self.inputSignal = np.array(
            [self.amplitude * (2 * np.abs(2 * (t * self.timeStep * self.frequency - np.floor(t * self.timeStep * self.frequency + 0.5))) - 1)
                for t in range(self.signalLength)]
        )
