"""The Model of bus service planner compose of the algorithm that solve the problem"""
import heapq
from collections import defaultdict, deque


class BusServiceModel:
    # def __init__(self):
    #     self.graph = None
    #
    # def create_graph(self, data):
    #     graph = defaultdict(list)
    #     prev_stop = None
    #
    #     for stop_data in data:
    #         stop = stop_data['Bus stop']
    #         line = stop_data['Line']
    #         if prev_stop is not None:
    #             if prev_stop != stop:
    #                 distance = float(stop_data[f'Distance for Line {line[0]} (Km)'])
    #                 graph[prev_stop].append((stop, distance))
    #         prev_stop = stop
    #     self.graph = graph
    #     return graph
    #
    # def bfs_shortest_route(self, start, end):
    #     visited = set()
    #     queue = deque([(start, [start], 0)])
    #     total_distance = 0
    #     start_passed = False
    #
    #     while queue:
    #         current, path, distance = queue.popleft()
    #         if start_passed:
    #             total_distance += distance
    #
    #         if current == end:
    #             return path, total_distance
    #
    #         if current == start:
    #             start_passed = True
    #
    #         visited.add(current)
    #         for neighbor, dist in self.graph[current]:
    #             if neighbor not in visited and neighbor not in path[:-1]:
    #                 queue.append((neighbor, path + [neighbor], dist))
    #
    #     return None, None
    def __init__(self):
        self.data = None

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
                if stops_lines[stop1] in stops_lines[stop2]:
                    stops_lines[stop1] = stops_lines[stop2]
                    common = stops_lines[stop1]
                    common_lines[(stop1, stop2)] = common
                else:
                    return None
        return common_lines

    def find_shortest_route(self, start, end):
        # Find common line and filter data
        common_lines = self.find_common_lines()
        if common_lines is None:
            return "Sorry, There is no bus line pass your destination.", '-'
        common_line = common_lines[(start, end)]
        filtered_data = {(start, end): common_line}
        # Find distance
        distance = 0
        for stop in self.data:
            if stop['Bus stop'] == start:
                distance -= float(stop[f'Distance for Line {common_line[0]} (Km)'])
            elif stop['Bus stop'] == end:
                distance += float(stop[f'Distance for Line {common_line[0]} (Km)'])
        return filtered_data[(start, end)], distance

