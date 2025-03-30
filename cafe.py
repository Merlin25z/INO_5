from food_place import FoodPlace

class Cafe(FoodPlace):
    def __init__(self, name, menu):
        super().__init__(name, menu)

    def serve_coffee(self):
        print(f"В {self.name} подают кофе")