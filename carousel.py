from attraction import Attraction

class Carousel(Attraction):
    def __init__(self, name, capacity, price, number_of_horses):
        super().__init__(name, capacity, price)
        self.number_of_horses = number_of_horses

    def start(self):
        print(f"Карусель {self.name} с {self.number_of_horses} лошадками запускается")