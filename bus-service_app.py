import tkinter as tk
from bus-service_view import BusServicePlanner

if __name__ == '__main__':
    bus_data = [
        ("E1", "1 and 3, special", 0.000), ("E2", "1 and 3", 0.350), ("S1", "1 and 3", 0.250),
        ("C1", "1 and special", 0.150), ("C2", "1", 0.250), ("E12", "1", 0.400), ("E14", "1", 0.300),
        ("C6", "1", 0.200), ("C7", "1", 0.200), ("C8", "1", 0.200), ("W7", "1", 0.300), ("W1", "1", 0.100),
        ("W2", "1", 0.300), ("W3", "1", 0.200), ("C9", "1", 0.200), ("C10", "1", 0.100), ("C11", "1", 0.200),
        ("C12", "1 and special", 0.200), ("E6", "1 and 3", 0.200), ("E5", "1 and 3", 0.200),
        ("E4", "1 and 3", 0.100), ("E3", "1 and 3", 0.100), ("E1 (2)", "1 and 3, special", 0.600)
    ]
    root = tk.Tk()
    view = BusServicePlanner(root, bus_data)
    root.mainloop()
