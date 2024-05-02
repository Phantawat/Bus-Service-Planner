"""Doc string"""
import webbrowser
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class BusServicePlanner(tk.Frame):
    """Bus service planner class that keep all user-interface"""
    def __init__(self, parent, bus_data: list, image_path):
        super().__init__(parent)
        self.parent = parent
        self.bus_data = bus_data
        self.image_path = image_path
        self.options = {'sticky': tk.NSEW, 'padx': 2, 'pady': 2}
        self.result = 'close'
        self.init_components()

    def init_components(self):
        font = ('Helvetica', 16)
        self.parent.option_add('*Font', font)
        self.menubar = tk.Menu(self.parent)
        self.menubar2 = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.frame1 = tk.Frame()
        self.frame2 = tk.Frame()
        self.frame3 = tk.Frame()

        self.label_title()
        self.add_menu_items()
        self.create_input_box("Route")
        self.create_input_box("Starting")
        self.create_input_box("Ending")
        self.create_button()
        self.display_image()
        self.pack_components()

    def pack_components(self):
        """Pack components of all frame"""
        self.frame1.pack(side=tk.TOP, fill=tk.BOTH)
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame3.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.parent.config(background="#fffac5")
        self.frame1.config(background="#ffffff")
        self.frame2.config(background="#fffac5")
        self.frame3.config(background="#fffac5")

    def label_title(self):
        """Create label in frame 1"""
        text = tk.StringVar()
        label = tk.Label(self.frame1, textvariable=text)
        label.pack(side=tk.TOP, expand=True)
        label.config(bg="#ffffff", )
        text.set("Welcome to Bus Service Planner")

    def add_menu_items(self):
        """Add menu items"""
        # Create a single menu object
        self.menubar = tk.Menu(self.parent)

        # Add menu items to the first menu
        menu1 = tk.Menu(self.menubar, tearoff=0)
        menu1.add_cascade(label="Route1", command=lambda x='route1.jpg': self.set_image_path(x))
        menu1.add_cascade(label="Route3", command=lambda x='route3.jpg': self.set_image_path(x))
        menu1.add_cascade(label="Special", command=lambda x='special.jpg': self.set_image_path(x))
        menu1.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="Route", menu=menu1)

        # Add menu items to the second menu
        menu2 = tk.Menu(self.menubar, tearoff=0)
        menu2.add_command(label="Bar graph")
        self.menubar.add_cascade(label="Graph", menu=menu2)

        # Configure the parent with the merged menu
        self.parent.config(menu=self.menubar)

    def create_input_box(self, label_text):
        """Create an input box"""
        box_label = tk.Label(self.frame2, text=label_text)
        box_label.pack(side=tk.TOP, padx=5, pady=5, expand=True)
        box_label.config(background="#fffac5")
        box = ttk.Combobox(self.frame2)
        box.pack(side=tk.TOP, padx=5, pady=5)
        if label_text == "Route":
            box['values'] = ['Route1', 'Route3', 'Special']
            box.bind("<<ComboboxSelected>>", self.handle_combobox_select)
        elif label_text == "Starting":
            self.start_box = box
            self.start_box['value'] = self.get_bus_stop()
        elif label_text == "Ending":
            self.ending_box = box
            self.ending_box['value'] = self.get_bus_stop()

    def create_button(self):
        """Submit function for getting the starting and ending bus stops"""
        self.submit = tk.Button(self.frame2, text="Submit", command=self.button_clicked)
        self.submit.pack(side=tk.LEFT, padx=20, pady=10, expand=True)

    def get_bus_stop(self):
        """Get bus stop in term list of name"""
        bus_stop = []
        for station in self.bus_data:
            bus_stop.append(station['Bus stop'])
        return bus_stop

    def display_image(self):
        """Display image on frame3"""
        img = Image.open(self.image_path)
        img = img.resize((600, 400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self.frame3, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.pack(expand=True)

    def display_result(self, path, distance):
        """A new page displays the result"""
        self.result_frame = tk.Frame()
        self.show_result()
        # Create labels to display the result
        result_label = tk.Label(self.result_frame, text=f"Shortest path: {path}")
        result_label.pack()
        distance_label = tk.Label(self.result_frame, text=f"Total distance: {distance} Km")
        distance_label.pack()
        back_button = tk.Button(self.result_frame, text="Back", command=self.hide_result)
        back_button.pack()
        # self.show_route()

    def hide_result(self):
        """Hide the result page"""
        self.result_frame.pack_forget()
        self.result = 'close'
        self.pack_components()

    def show_result(self):
        """Show result page"""
        self.result_frame.pack(fill=tk.BOTH)
        self.result = 'open'
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()

    def button_clicked(self):
        """Command handle when the button was clicked"""
        start = self.start_box.get()
        end = self.ending_box.get()
        self.controller.handle_clicked(self.bus_data, start, end)

    def show_route(self):
        # Open a new web page in the default browser to display the route on a map
        webbrowser.open_new_tab("https://www.google.com/maps/dir/" + self.start_box.get() + "/" + self.ending_box.get())

    def handle_combobox_select(self, event):
        """Callback function for combobox selection"""
        selected_value = event.widget.get().lower() + ".jpg"
        self.set_image_path(selected_value)

    def set_image_path(self, image_path):
        """Change Image"""
        self.image_path = image_path
        for widget in self.frame3.winfo_children():
            widget.destroy()
        self.display_image()

    def set_controller(self, controller):
        self.controller = controller
