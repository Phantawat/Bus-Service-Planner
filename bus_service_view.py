"""Doc string"""
import webbrowser
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class BusServicePlanner(tk.Frame):
    """Bus service planner class that keep all user-interface"""
    def __init__(self, parent, bus_data: list, image_path):
        self.parent = parent
        self.bus_data = bus_data
        self.image_path = image_path
        self.options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        self.init_components()

    def init_components(self):
        self.parent.title("(KU) Bus Service Planner")
        self.parent.config(background='green')
        font = ('Monospace', 16)
        self.parent.option_add('*Font', font)
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.frame1 = tk.Frame()
        self.frame2 = tk.Frame()
        self.frame3 = tk.Frame()

        self.add_menu_items()
        self.create_input_box("Route")
        self.create_input_box("Starting")
        self.create_input_box("Ending")
        self.submit_button()
        self.display_image()
        self.pack_components()

    def pack_components(self):
        """Pack components of all frame"""
        self.frame1.pack(side=tk.TOP, fill=tk.X)
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame3.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def add_menu_items(self):
        """Add menu items"""
        menu = tk.Menu(self.menubar, tearoff=0)
        menu.add_cascade(label="Route1", command=lambda x='route1.jpg': self.set_image_path(x))
        menu.add_cascade(label="Route3", command=lambda x='route3.jpg': self.set_image_path(x))
        menu.add_cascade(label="Special", command=lambda x='special.jpg': self.set_image_path(x))
        menu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="Route", menu=menu)

    def create_input_box(self, label_text):
        """Create an input box"""
        box_label = tk.Label(self.frame1, text=label_text)
        box_label.pack(side=tk.LEFT, padx=5, pady=5)
        box = ttk.Combobox(self.frame1)
        box.pack(side=tk.LEFT, padx=5, pady=5)
        if label_text == "Route":
            box['values'] = ['Route1', 'Route3', 'Special']
        elif label_text == "Starting":
            self.start_box = box
        elif label_text == "Ending":
            self.ending_box = box

    def display_image(self):
        """Display image on frame3"""
        img = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self.frame3, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.pack(expand=True)

    def clear_image(self):
        """Clear image for inserting a new one"""
        for widget in self.frame3.winfo_children():
            widget.destroy()

    def submit_button(self):
        """Submit function for getting the starting and ending bus stops"""
        self.submit = ttk.Button(self.frame1, text="Submit", command=self.button_clicked).pack(side=tk.RIGHT)

    def button_clicked(self):
        """Command handle when the button was clicked"""
        pass

    def show_route(self):
        # Open a new web page in the default browser to display the route on a map
        webbrowser.open_new_tab("https://www.google.com/maps/dir/" + self.start_box.get() + "/" + self.ending_box.get())

    def set_image_path(self, image_path):
        """Change Image"""
        self.image_path = image_path
        self.clear_image()
        self.display_image()

    def set_controller(self, controller):
        self.controller = controller
