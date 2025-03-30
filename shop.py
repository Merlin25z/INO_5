class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def sell_item(self):
        print(f"В {self.name} продают {self.items}")