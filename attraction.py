class Attraction:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price

    def start(self):
        print(f"{self.name} запускается")

    def stop(self):
        print(f"{self.name} останавливается")