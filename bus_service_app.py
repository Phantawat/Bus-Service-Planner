import os.path
import tkinter as tk
import csv
from bus_service_view import BusServicePlanner


def read_csv_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    data = []
    with open(os.path.join(__location__, 'Bus_Service_Planner.csv')) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

if __name__ == '__main__':
    bus_data = read_csv_file()
    print(bus_data)
    root = tk.Tk()
    image_path = "route1.jpg"
    view = BusServicePlanner(root, bus_data, image_path)
    root.mainloop()
