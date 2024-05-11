"""The Model of bus service planner compose of the algorithm that solve the problem"""
import pandas as pd
import matplotlib.pyplot as plt


class BusServiceModel:
    def __init__(self):
        self.data = None
        self.df = None

    def set_data(self, data):
        """Set up data"""
        self.data = data

    def set_data_frame(self):
        """Set up data frame"""
        self.df = pd.DataFrame(self.data)

    def find_common_lines(self):
        stops_lines = {}
        for stop in self.data:
            stop_name = stop['Bus stop']
            lines = stop['Line']
            stops_lines[stop_name] = lines
        common_lines = {}
        for stop1 in stops_lines:
            for stop2 in stops_lines:
                if stop1 != stop2:  # Ensure we're not comparing the same stop
                    common = [line1 for line1 in stops_lines[stop1] if line1 in stops_lines[stop2]]
                    if common:
                        if len(stops_lines[stop1]) > len(stops_lines[stop2]):
                            common_lines[(stop1, stop2)] = stops_lines[stop2]
                        else:
                            common_lines[(stop1, stop2)] = stops_lines[stop1]
        return common_lines

    def find_shortest_route(self, start, end):
        # Check whether start or end is blank.
        if start == '' or end == '':
            return f'Please, choose your destination', 'press back to go back.'
        # Find common line and filter data
        common_lines = self.find_common_lines()
        common_line = common_lines[(start, end)]
        filtered_data = {(start, end): common_line}
        # Find distance
        if filtered_data[(start, end)] is None:
            return f"Sorry, there is no bus line pass your destination.", '-'
        distance = 0
        for stop in self.data:
            if stop['Bus stop'] == start:
                distance -= float(stop[f'Distance for Line {common_line[0]} (Km)'])
            elif stop['Bus stop'] == end:
                distance += float(stop[f'Distance for Line {common_line[0]} (Km)'])
        return f"You can take Line: {filtered_data[(start, end)]}", f"Total distance: {distance} Km"

    def storytelling(self):
        """Generate a data storytelling narrative based on the bus service data."""
        # Basic storytelling example: summarize the number of stops and lines
        self.set_data_frame()
        num_stops = len(self.df)
        shape = self.df.shape
        story = f"The bus service data contains information about {num_stops} stops."
        return story, shape

    def information(self):
        """Generate information of Bus"""
        return
