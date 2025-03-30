class FoodPlace:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def serve_food(self):
        print(f"В {self.name} подают {self.menu}")