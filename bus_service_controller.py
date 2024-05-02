from collections import defaultdict, deque


class BusServiceController:
    """A class for handling user input and updating the Model"""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_clicked(self, data, start, end):
        """Handling user clicked"""
        # self.model.set_data(data)
        # path, total_distance = self.model.dijkstra_shortest_route(start, end)
        self.model.create_graph(data)
        path, total_distance = self.model.bfs_shortest_route(start, end)
        self.view.display_result(path, total_distance)

