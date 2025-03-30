from carousel import Carousel
from dessert_place import DessertPlace
from cafe import Cafe
from shop import Shop
from theater import Theater
from park import Park

def main():
    # Создаем объекты
    carousel = Carousel("Веселая карусель", 20, 100, 10)
    dessert_place = DessertPlace("Сладкое королевство", ["мороженое", "пирожное"], "шоколадный торт")
    cafe = Cafe("Кофейня у озера", ["кофе", "чай", "булочки"])
    shop = Shop("Магазин сувениров", ["магниты", "футболки"])
    theater = Theater("Волшебник страны Оз")

    # Создаем парк и добавляем объекты
    park = Park()
    park.add_attraction(carousel)
    park.add_food_place(dessert_place)
    park.add_food_place(cafe)
    park.add_shop(shop)
    park.set_theater(theater)

    # Открываем парк
    park.open_park()

if __name__ == "__main__":
    main()