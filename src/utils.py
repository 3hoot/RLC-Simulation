import tkinter as tk
import re


class frameUtils:
    def __init__(self):
        pass

    @staticmethod
    def getFrameName(frame):
        return frame.__class__.__name__

    @staticmethod
    def getFrameType(frame):
        return type(frame).__name__

    @staticmethod
    def showFrame(self, frame_class) -> None:
        frame = self.frames[frame_class]
        frame.tkraise()

    @staticmethod
    def updateVal(self, var: tk.Variable, entry: tk.Entry) -> None:
        try:
            match type(var):
                case tk.IntVar():
                    var.set(int(entry.get()))
                case tk.DoubleVar():
                    var.set(float(entry.get()))

            # debug
            # display the value in the entry
            print(f"{var.get()} {type(var)}")

        except tk.TclError:
            match type(var):
                case tk.IntVar():
                    var.set(0)
                case tk.DoubleVar():
                    var.set(0.0)
            entry.delete(0, tk.END)
            entry.insert(0, str(var.get()))

        except ValueError:
            pass

    @staticmethod
    def check(var_type, value: str) -> bool:
        match var_type:
            case tk.IntVar:
                return re.match(r"^\d+$", value) is not None
            case tk.DoubleVar:
                return re.match(r"^\d+(\.\d+)?$", value) is not None
            case tk.StringVar:
                return re.match(r"^[a-zA-Z0-9_]+$", value) is not None
            case _:
                return False
