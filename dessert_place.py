from food_place import FoodPlace

class DessertPlace(FoodPlace):
    def __init__(self, name, menu, special_dessert):
        super().__init__(name, menu)
        self.special_dessert = special_dessert

    def serve_dessert(self):
        print(f"В {self.name} подают особенный десерт: {self.special_dessert}")