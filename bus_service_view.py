"""Doc string"""
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk


class BusServicePlanner(tk.Frame):
    """Bus service planner class that keep all user-interface"""
    def __init__(self, parent, bus_data: list, image_path):
        super().__init__(parent)
        self.info_choice = []
        self.parent = parent
        self.bus_data = bus_data
        self.image_path = image_path
        self.options = {'sticky': tk.NSEW, 'padx': 5, 'pady': 5}
        self.info_status = 'close'
        self.init_components()

    def init_components(self):
        font = ('Times', 12)
        self.parent.option_add('*Font', font)
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.title_frame = tk.Frame()
        self.input_frame = tk.Frame()
        self.map_frame = tk.Frame()
        self.info_frame = tk.Frame()

        self.label_title()
        self.create_input_box("Route")
        self.create_input_box("Starting")
        self.create_input_box("Ending")
        self.create_button()
        self.display_image()
        self.add_info_items()
        self.pack_components()

    def pack_components(self):
        """Pack components of all frame"""
        self.title_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.info_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.map_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.parent.config(background="#fffac5")
        self.title_frame.config(background="#ffffff")
        self.input_frame.config(background="#fffac5")
        self.map_frame.config(background="#fffac5")
        self.info_frame.config(background="#ffc152")

    def label_title(self):
        """Create label in frame 1"""
        text = tk.StringVar()
        label = tk.Label(self.title_frame, textvariable=text)
        label.pack(side=tk.TOP, expand=True)
        label.config(bg="#ffffff")
        text.set("Welcome to Bus Service Planner")

    def add_info_items(self):
        """Add info in the frame"""
        self.info_box = tk.Listbox(self.info_frame)
        self.info_box.pack(fill=tk.Y, expand=True)
        self.info_box.config(bg="#af8f55", width=10)
        self.info_box.bind('<Double-Button-1>', self.info_selected)
        self.info_choice = ['- Route info', '- Graph', '- Story telling', '- Information', '- Comment']
        for choice in self.info_choice:
            self.info_box.insert(tk.END, choice)

    def create_input_box(self, label_text):
        """Create an input box"""
        box_label = tk.Label(self.input_frame, text=label_text)
        box_label.pack(side=tk.TOP)
        box_label.config(background="#fffac5")
        box = ttk.Combobox(self.input_frame)
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
        self.submit = tk.Button(self.input_frame, text="Submit", command=self.button_clicked)
        self.submit.pack(side=tk.TOP, padx=5, pady=5)

    def get_bus_stop(self):
        """Get bus stop in term list of name"""
        bus_stop = []
        for station in self.bus_data:
            bus_stop.append(station['Bus stop'])
        return bus_stop

    def display_image(self):
        """Display image on frame3"""
        img = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(self.map_frame, image=photo)
        label.image = photo
        label.pack(expand=True)

    def display_result(self, text1, text2):
        """A new page displays the result"""
        self.result_frame = tk.Frame()
        self.show_result()
        # Create labels to display the result
        result_label = tk.Label(self.result_frame, text=text1)
        result_label.pack()
        distance_label = tk.Label(self.result_frame, text=text2)
        distance_label.pack()
        back_button = tk.Button(self.result_frame, text="Back", command=self.hide_result)
        back_button.pack()

    def hide_result(self):
        """Hide the result page"""
        self.result_frame.pack_forget()
        self.pack_components()

    def show_result(self):
        """Show result page"""
        self.result_frame.pack(fill=tk.BOTH)
        self.hide_components()
        self.map_frame.pack_forget()

    def info_selected(self, event):
        """Handle selected infos"""
        index = self.info_box.curselection()[0]
        value = self.info_choice[index]
        if self.info_status == 'close':
            self.select_frame = tk.Frame()
            self.select_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.info_status = 'open'
            if value == '- Route info':
                self.hide_components()
                self.map_frame.pack(fill=tk.BOTH, expand=True)
                label = tk.Label(self.select_frame, text='Route')
                label.config(background="#fffac5")
                label.pack()
                box = ttk.Combobox(self.select_frame)
                box.pack(side=tk.TOP, padx=5, pady=5)
                box['values'] = ['Route1', 'Route3', 'Special']
                box.bind("<<ComboboxSelected>>", self.handle_combobox_select)
            elif value == '- Story telling':
                self.controller.get_data_story(self.bus_data)
            elif value == '- Graph':
                self.controller.get_graph(self.bus_data)
        elif self.info_status == 'open':
            self.select_frame.pack_forget()
            self.pack_components()
            self.info_status = 'close'

    def hide_components(self):
        """Hide function that will hide the first page"""
        self.map_frame.pack_forget()
        self.input_frame.pack_forget()

    def button_clicked(self):
        """Command handle when the button was clicked"""
        start = self.start_box.get()
        end = self.ending_box.get()
        self.controller.handle_clicked(self.bus_data, start, end)

    def handle_combobox_select(self, event):
        """Callback function for combobox selection"""
        selected_value = event.widget.get().lower() + ".jpg"
        self.set_image_path(selected_value)

    def set_image_path(self, image_path):
        """Change Image"""
        self.image_path = image_path
        for widget in self.map_frame.winfo_children():
            widget.destroy()
        self.display_image()

    def set_controller(self, controller):
        self.controller = controller
