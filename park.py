class Park:
    def __init__(self):
        self.attractions = []
        self.food_places = []
        self.shops = []
        self.theater = None

    def add_attraction(self, attraction):
        self.attractions.append(attraction)

    def add_food_place(self, food_place):
        self.food_places.append(food_place)

    def add_shop(self, shop):
        self.shops.append(shop)

    def set_theater(self, theater):
        self.theater = theater

    def open_park(self):
        print("Парк открыт!")
        for attraction in self.attractions:
            attraction.start()
        for food_place in self.food_places:
            food_place.serve_food()
        for shop in self.shops:
            shop.sell_item()
        if self.theater:
            self.theater.start_show()