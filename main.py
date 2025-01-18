import tkinter as tk
from tkinter import messagebox

# Circuit Analysis Functions
def ohms_law(voltage=None, current=None, resistance=None):
    if voltage is None:
        return current * resistance
    elif current is None:
        return voltage / resistance
    elif resistance is None:
        return voltage / current
    else:
        raise ValueError("At least one of voltage, current, or resistance must be None.")

def total_resistance_series(resistors):
    return sum(resistors)

def total_resistance_parallel(resistors):
    if any(r == 0 for r in resistors):
        raise ValueError("Resistors cannot be zero in parallel.")
    return 1 / sum(1 / r for r in resistors)

def total_capacitance_series(capacitors):
    if any(c == 0 for c in capacitors):
        raise ValueError("Capacitors cannot be zero in series.")
    return 1 / sum(1 / c for c in capacitors)

def total_capacitance_parallel(capacitors):
    return sum(capacitors)

def total_inductance_series(inductors):
    return sum(inductors)

def total_inductance_parallel(inductors):
    if any(l == 0 for l in inductors):
        raise ValueError("Inductors cannot be zero in parallel.")
    return 1 / sum(1 / l for l in inductors)

# Component Management
class Component:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.type}): {self.value}"

class ComponentManager:
    def __init__(self):
        self.components = []

    def add_component(self, name, type, value):
        self.components.append(Component(name, type, value))

    def view_components(self):
        return "\n".join(str(c) for c in self.components)

    def get_component_values(self, type):
        return [c.value for c in self.components if c.type == type]

# Graphical User Interface (GUI)
class ElectricalEngineeringApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Electrical Engineering Calculator")
        self.component_manager = ComponentManager()

        self.create_menu()
        self.create_main_frame()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Add Component", command=self.add_component)
        tools_menu.add_command(label="View Components", command=self.view_components)
        menubar.add_cascade(label="Tools", menu=tools_menu)

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        self.create_ohms_law_frame()
        self.create_series_parallel_frame()

    def create_ohms_law_frame(self):
        ohms_frame = tk.LabelFrame(self.main_frame, text="Ohm's Law")
        ohms_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(ohms_frame, text="Voltage (V):").grid(row=0, column=0, padx=5, pady=5)
        self.voltage_entry = tk.Entry(ohms_frame)
        self.voltage_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(ohms_frame, text="Current (I):").grid(row=1, column=0, padx=5, pady=5)
        self.current_entry = tk.Entry(ohms_frame)
        self.current_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ohms_frame, text="Resistance (R):").grid(row=2, column=0, padx=5, pady=5)
        self.resistance_entry = tk.Entry(ohms_frame)
        self.resistance_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = tk.Button(ohms_frame, text="Calculate", command=self.calculate_ohms_law)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_series_parallel_frame(self):
        series_parallel_frame = tk.LabelFrame(self.main_frame, text="Series and Parallel")
        series_parallel_frame.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(series_parallel_frame, text="Resistors (Ω):").grid(row=0, column=0, padx=5, pady=5)
        self.resistors_entry = tk.Entry(series_parallel_frame)
        self.resistors_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(series_parallel_frame, text="Capacitors (F):").grid(row=1, column=0, padx=5, pady=5)
        self.capacitors_entry = tk.Entry(series_parallel_frame)
        self.capacitors_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(series_parallel_frame, text="Inductors (H):").grid(row=2, column=0, padx=5, pady=5)
        self.inductors_entry = tk.Entry(series_parallel_frame)
        self.inductors_entry.grid(row=2, column=1, padx=5, pady=5)

        calculate_button = tk.Button(series_parallel_frame, text="Calculate", command=self.calculate_series_parallel)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_ohms_law(self):
        try:
            voltage = float(self.voltage_entry.get()) if self.voltage_entry.get() else None
            current = float(self.current_entry.get()) if self.current_entry.get() else None
            resistance = float(self.resistance_entry.get()) if self.resistance_entry.get() else None

            result = ohms_law(voltage, current, resistance)
            messagebox.showinfo("Result", f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def calculate_series_parallel(self):
        try:
            resistors = [float(r) for r in self.resistors_entry.get().split(",") if r.strip()]
            capacitors = [float(c) for c in self.capacitors_entry.get().split(",") if c.strip()]
            inductors = [float(l) for l in self.inductors_entry.get().split(",") if l.strip()]

            total_resistance_series = total_resistance_series(resistors)
            total_resistance_parallel = total_resistance_parallel(resistors)
            total_capacitance_series = total_capacitance_series(capacitors)
            total_capacitance_parallel = total_capacitance_parallel(capacitors)
            total_inductance_series = total_inductance_series(inductors)
            total_inductance_parallel = total_inductance_parallel(inductors)

            result = f"Total Resistance (Series): {total_resistance_series} Ω\n"
            result += f"Total Resistance (Parallel): {total_resistance_parallel} Ω\n"
            result += f"Total Capacitance (Series): {total_capacitance_series} F\n"
            result += f"Total Capacitance (Parallel): {total_capacitance_parallel} F\n"
            result += f"Total Inductance (Series): {total_inductance_series} H\n"
            result += f"Total Inductance (Parallel): {total_inductance_parallel} H"

            messagebox.showinfo("Result", result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_component(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Component")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(add_window)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.type_entry = tk.Entry(add_window)
        self.type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Value:").grid(row=2, column=0, padx=5, pady=5)
        self.value_entry = tk.Entry(add_window)
        self.value_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = tk.Button(add_window, text="Add", command=self.add_component_to_manager)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_component_to_manager(self):
        name = self.name_entry.get()
        type = self.type_entry.get()
        value = float(self.value_entry.get())
        self.component_manager.add_component(name, type, value)
        messagebox.showinfo("Success", "Component added successfully.")
        self.name_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)

    def view_components(self):
        components = self.component_manager.view_components()
        messagebox.showinfo("Components", components)

if __name__ == "__main__":
    root = tk.Tk()
    app = ElectricalEngineeringApp(root)
    root.mainloop()