from collections import defaultdict, deque


class BusServiceController:
    """A class for handling user input and updating the Model"""
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_clicked(self, data, start, end):
        """Handling user clicked"""
        self.model.set_data(data)
        path, total_distance = self.model.find_shortest_route(start, end)
        self.view.display_result(path, total_distance)

    def get_data_story(self, data):
        """Get a story telling"""
        self.model.set_data(data)
        story, shape = self.model.storytelling()
        self.view.display_result(story, shape)
