"""Bus service view for display the Bus Service app"""
import tkinter as tk
import pandas as pd
import seaborn as sns
from tkinter import ttk
from tkinter import font
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk


class BusServicePlanner(tk.Frame):
    """Bus service planner class that keeps all user-interface"""

    def __init__(self, parent, bus_data: list, image_path):
        super().__init__(parent)
        self.info_choice = []
        self.parent = parent
        self.bus_data = bus_data
        self.image_path = image_path
        self.options = {'sticky': tk.NSEW, 'padx': 5, 'pady': 5}
        self.info_status = 'close'
        self.fig = Figure()
        self.ax = self.fig.add_subplot()
        self.init_components()

    def init_components(self):
        font = ('Times', 12)
        self.parent.option_add('*Font', font)
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)
        self.df = pd.read_csv("Bus_Service_Planner.csv")

        self.title_frame = tk.Frame()
        self.input_frame = tk.Frame()
        self.map_frame = tk.Frame()
        self.info_frame = tk.Frame()
        self.statistics_frame = tk.Frame()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.statistics_frame)
        self.statistics_label = ttk.Label()

        self.label_title()
        self.create_input_box("Route")
        self.create_input_box("Starting")
        self.create_input_box("Ending")
        self.create_button()
        self.display_image()
        self.add_info_items()
        self.pack_components()

    def pack_components(self):
        """Pack components of all frames"""
        self.title_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.info_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.map_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.statistics_frame.pack_forget()
        self.statistics_label.pack_forget()

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
        self.info_box.config(bg="#af8f55", width=20)
        self.info_box.bind('<Double-Button-1>', self.info_selected)
        self.info_choice = ['- Route info', '', '- Information', '', '- Data Storytelling', '  - Distribution Graph',
                            '  - Descriptive statistics', '  - Correlation', '', '- Comment']
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
        self.submit = ttk.Button(self.input_frame, text="Submit", command=self.button_clicked)
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
        if hasattr(self, 'result_frame') and self.result_frame is not None:
            self.result_frame.destroy()
        self.result_frame = tk.Frame()
        self.show_result()
        # Create labels to display the result
        result_label = tk.Label(self.result_frame, text=text1)
        result_label.pack()
        distance_label = tk.Label(self.result_frame, text=text2)
        distance_label.pack()
        back_button = ttk.Button(self.result_frame, text="Back", command=self.hide_result)
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

        # Check if info_status is 'close'
        if self.info_status == 'close':
            # Show select_frame and set info_status to 'open'
            self.select_frame = tk.Frame()
            self.select_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.info_status = 'open'
            self.hide_components()  # Hide components based on selected value
            back_label = tk.Label(self.select_frame, text='Double click on the same place to go back')
            back_label.pack(side=tk.BOTTOM)
            back_label.config(foreground='red')
            # Based on the selected value, show different components
            if value == '- Route info':
                label = tk.Label(self.select_frame, text='Route')
                label.config(background="#fffac5")
                label.pack()
                box = ttk.Combobox(self.select_frame)
                box.pack(side=tk.TOP, padx=5, pady=5)
                box['values'] = ['Route1', 'Route3', 'Special']
                box.bind("<<ComboboxSelected>>", self.handle_combobox_select)
                self.map_frame.pack(side=tk.TOP, fill=tk.BOTH)
            elif value == '  - Distribution Graph':
                self.plot_hist()
            elif value == '  - Correlation':
                self.show_correlation()
            elif value == '  - Descriptive statistics':
                self.show_statistics()
            elif value == '- Information':
                box = ttk.Combobox(self.select_frame)
                box.pack(side=tk.TOP, padx=5, pady=5)
                box['value'] = self.get_bus_stop()
                box.bind('<<ComboboxSelected>>', self.show_bus_information)
        # Check if info_status is 'open'
        elif self.info_status == 'open':
            # Hide select_frame
            self.select_frame.pack_forget()
            self.statistics_frame.pack_forget()
            self.canvas.get_tk_widget().pack_forget()
            self.ax.clear()
            self.pack_components()
            self.info_status = 'close'

    def hide_components(self):
        """Hide function that will hide the first page"""
        self.map_frame.pack_forget()
        self.input_frame.pack_forget()
        self.statistics_frame.pack()

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

    def plot_hist(self):
        """Plot a histogram graph"""
        self.ax.clear()
        sns.histplot(self.df['Distance between 2 stations (Km)'], ax=self.ax)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_correlation(self):
        """Show correlation between data"""
        self.ax.clear()
        sns.heatmap(self.df.corr(numeric_only=True), annot=True,
                    cmap=sns.color_palette('coolwarm'),
                    ax=self.ax
                    )
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_statistics(self):
        """Method for displaying the statistics value of data"""
        self.statistics_label.pack()
        # Calculate statistics
        mean = self.df.mean(numeric_only=True)
        median = self.df.median(numeric_only=True)
        statistics_text = f"Mean: {mean}\nMedian: {median}"
        self.statistics_label.config(text=statistics_text)

    def show_bus_information(self, event):
        """Show information about a selected bus route"""
        # Get bus information for the selected route
        route = event.widget.get()
        text = ''
        for stop in self.bus_data:
            if stop['Bus stop'] == route:
                info = stop
                for i in info:
                    text += f"{i}: {stop[i]} >>\n"
        self.display_result(text, None)
