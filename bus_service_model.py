"""The Model of bus service planner compose of the algorithm that solve the problem"""
import pandas as pd
import matplotlib.pyplot as plt


class BusServiceModel:
    def __init__(self):
        self.data = None
        self.df = pd.DataFrame(self.data)

    def set_data(self, data):
        self.data = data

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
                    common = [line for line in stops_lines[stop1] if line in stops_lines[stop2]]
                    if common:
                        common_lines[(stop1, stop2)] = stops_lines[stop1]
        return common_lines

    def find_shortest_route(self, start, end):
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
        """Story telling from the data"""
        # return self.df.head()
        pass

    def create_graph(self):
        """Create a graph of distances between bus stops"""
        # Extract relevant data for visualization
        # stops = self.df['Bus stop']
        # distances = self.df[['Distance for Line 1 (Km)', 'Distance for Line 3 (Km)', 'Distance for Special Line (Km)']]
        #
        # # Plotting
        # plt.figure(figsize=(10, 6))
        # for i in range(len(distances.columns)):
        #     plt.plot(stops, distances.iloc[:, i], marker='o', label=distances.columns[i])
        #
        # # Adding labels and title
        # plt.xlabel('Bus Stops')
        # plt.ylabel('Distance (Km)')
        # plt.title('Distances between Bus Stops for Different Lines')
        # plt.xticks(rotation=45)
        # plt.legend()
        # plt.grid(True)
        #
        # # Show plot
        # plt.tight_layout()
        # plt.show()
        pass
