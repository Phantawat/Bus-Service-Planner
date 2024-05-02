"""The Model of bus service planner compose of the algorithm that solve the problem"""
import heapq
from collections import defaultdict, deque


class BusServiceModel:
    def __init__(self):
        self.graph = None

    def create_graph(self, data):
        graph = defaultdict(list)
        prev_stop = None

        for stop_data in data:
            stop = stop_data['Bus stop']
            line = stop_data['Line']
            if prev_stop is not None:
                if prev_stop != stop:
                    distance = float(stop_data[f'Distance for Line {line[0]} (Km)'])
                    graph[prev_stop].append((stop, distance))
            prev_stop = stop
        self.graph = graph
        return graph

    def bfs_shortest_route(self, start, end):
        visited = set()
        queue = deque([(start, [start], 0)])
        total_distance = 0
        start_passed = False

        while queue:
            current, path, distance = queue.popleft()
            if start_passed:
                total_distance += distance

            if current == end:
                return path, total_distance

            if current == start:
                start_passed = True

            visited.add(current)
            for neighbor, dist in self.graph[current]:
                if neighbor not in visited and neighbor not in path[:-1]:
                    queue.append((neighbor, path + [neighbor], dist))

        return None, None
    # def __init__(self):
    #     self.data = None
    #
    # def set_data(self, data):
    #     self.data = data
    #
    # def dijkstra_shortest_route(self, start, end):
    #     distances = {stop['Bus stop']: float('inf') for stop in self.data}
    #     distances[start] = 0
    #     queue = [(0, start)]
    #     visited = set()
    #
    #     while queue:
    #         current_distance, current = heapq.heappop(queue)
    #         if current in visited:
    #             continue
    #         visited.add(current)
    #
    #         if current == end:
    #             path = []
    #             while current in distances:
    #                 path.insert(0, current)
    #                 current = distances[current][1]
    #             return path, distances[end]
    #
    #         for stop in self.data:
    #             if stop['Bus stop'] == current:
    #                 next_stops = []
    #                 for line in stop['Line'].split(' and '):
    #                     if line == 'special':
    #                         next_stops.append(stop['Bus stop'] + ' (2)')
    #                     else:
    #                         next_stops.append(stop['Next stop'])
    #                 for neighbor in next_stops:
    #                     distance = float(stop[f'Distance for Line {line[0]} (Km)'])
    #                     if neighbor in visited:
    #                         continue
    #                     new_distance = current_distance + distance
    #                     if new_distance < distances[neighbor]:
    #                         distances[neighbor] = new_distance, current
    #                         heapq.heappush(queue, (new_distance, neighbor))
    #
    #     return None, None
