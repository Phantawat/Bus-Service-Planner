"""Doc string"""
import webbrowser
import tkinter as tk
from tkinter import ttk

class BusServicePlanner(tk.Frame):
    """Bus service planner class that keep all user-interface"""
    def __init__(self, parent, bus_data):
        self.parent = parent
        self.bus_data = bus_data

    def init_components(self):
        self.parent.title("(KU) Bus Service Planner")

        self.start_label = tk.Label(self.parent, text="Starting Bus Stop:")
        self.start_entry = tk.Entry(self.parent)
        self.end_label = tk.Label(self.parent, text="Destination Bus Stop:")
        self.end_entry = tk.Entry(self.parent)
        self.submit_button = tk.Button(self.parent, text="Find Route", command=self.submit)
        self.route_label = tk.Label(self.parent, text="")
        self.distance_label = tk.Label(self.parent, text="")

        # Place GUI components in the window
        self.start_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.start_entry.grid(row=0, column=1, padx=10, pady=5)
        self.end_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.end_entry.grid(row=1, column=1, padx=10, pady=5)
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.route_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.distance_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def submit(self):
        """Submit function for getting the starting and ending bus stops"""

    def display_route(self, route, distance):
        # Display the shortest route and total distance to the user
        self.route_label.config(text=f"Shortest Route: {route}")
        self.distance_label.config(text=f"Total Distance: {distance} km")

    def show_route(self):
        # Open a new web page in the default browser to display the route on a map
        webbrowser.open_new_tab("https://www.google.com/maps/dir/" + self.start_entry.get() + "/" + self.end_entry.get())

    def set_controller(self, controller):
        self.controller = controller
