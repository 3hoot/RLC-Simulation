import numpy as np


class Circuit:
    def __init__(self, R1: float, R2: float, L: float, C: float, N: np.int8, log_omega_low: np.int8) -> None:
        """
        Initialize the Circuit class with resistance, inductance, and capacitance values.

        Args:
            R1 (float): Resistance in ohms.
            R2 (float): Second resistance in ohms.
            L (float): Inductance in henries.
            C (float): Capacitance in farads.
            N (int8): number of individual omega values used to calculate Bode characteristics (recomended 100)
            log_omega_low (int8): low end of omega values used to calculate Bode characteristics in dB*rad/s (recomended -30)
        """
        self.R1 = R1
        self.R2 = R2
        self.L = L
        self.C = C
        self.omega_range = np.array(
            [10**(0.1 * (i + log_omega_low)) for i in range(N)], dtype=float)

    def response(self, input: np.array, dt: float) -> np.array:
        """
        Simulate the response of an RLC circuit to a given time array.
        """
        N = input.size
        output = np.zeros(N, dtype=float)
        self.a = 1 / (self.R2 * self.C)
        self.b = (self.R1 + self.R2) / self.R1 * self.a

        SUM = 0.0  # Initialize SUM
        for i in range(N):
            E = input[i] - SUM * self.b
            SUM = SUM + E * dt
            output[i] = SUM * self.a
        return np.array(output)

    def Bode_Amplification(self) -> np.array:
        """
        Calculate the Bode amplification of the circuit.
        """
        bode_A = np.zeros(100, dtype=float)
        for i in range(100):
            bode_A[i] = self.a / \
                np.sqrt(self.b ** 2 + self.omega_range[i] ** 2)
        return np.array(bode_A)

    def Bode_Phase(self) -> np.array:
        """
        Calculate the Bode phase of the circuit.
        """
        bode_P = np.zeros(100, dtype=float)
        for i in range(100):
            bode_P[i] = -np.arctan2(self.omega_range[i], self.b)
        return np.array(bode_P)
