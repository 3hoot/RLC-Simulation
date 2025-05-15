import numpy  as np

# Test version for reference 
class Circuit:
    def __init__(self, R1: float, R2: float, L: float, C: float) -> None:
        """
        Initialize the Circuit class with resistance, inductance, and capacitance values.
        This is a test version of the class. Implement the actual logic in the future.
        
        Args:
            R (float): Resistance in ohms.
            R2 (float): Second resistance in ohms.
            L (float): Inductance in henries.
            C (float): Capacitance in farads.
        """
        self.R1 = R1
        self.R2 = R2
        self.L = L
        self.C = C 
        self.omega_range = np.zeros(100, dtype: int8)
        for i in range(100):
            self.omega_range(i) = 10^(0.1*(i-30))

    
    def response(self, input: np.array, dt: float) -> np.array:
        """
        Simulate the response of an RLC circuit to a given time array.
        This is a test version of the method. Implement the actual logic in the future.
        
        Args:
            input (np.array): Signal array for simulation.
            dt (float): Time step for the simulation.
        
        Returns:
            np.array: Simulated response of the RLC circuit.
        """
        N = input.size

        output = np.zeros(N, dtype: float)

        self.a = 1/self.R2/self.C
        self.b = (self.R1 + self.R2)/self.R1*self.a

        for i in range(N):
            E = input(i) - SUM*self.b
            SUM = SUM + E* dt
            output(i) = SUM * self.a
        return output
    
    def Bode_Amplification(self) -> np.array:
        bode_A =  np.zeros(100, dtype: float)
        for i in range(100):
            bode_A(i) = self.a/np.sqrt(self.b^2+self.omega_range(i)^2)
        return bode_A
    
    def Bode_Phase(self) -> np.array:
        bode_P =  np.zeros(100, dtype: float)
        for i in range(100):
            bode_P(i) = -np.arctan2(self.omega_range(i),self.b)
        return bode_P
