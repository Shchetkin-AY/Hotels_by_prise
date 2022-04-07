class Hotel:
    """Класс Отель"""

    def __init__(self, name, star, cost):
        self.name = name
        self.star = star
        self.cost = cost

    def str(self):
        return (f'{self.name} {self.star} {self.cost}')


hotels = []

hotels.append(Hotel('Atlantic Castle Hotel', 3, 45000))
hotels.append(Hotel('Oriental Tide Hotel & Spa', 5, 92000))
hotels.append(Hotel('Bronze Mansion Resort', 4, 84000))
hotels.append(Hotel('Parallel Harbor Hotel', 4, 80000))
hotels.append(Hotel('Obsidian Vertex Hotel', 5, 120000))
hotels.append(Hotel('Noble Memorial Hotel', 4, 59000))
hotels.append(Hotel('Mirth Hotel', 4, 64000))
hotels.append(Hotel('Felicity Motel', 3, 29000))
hotels.append(Hotel('Renaissance Hotel', 3, 49000))
hotels.append(Hotel('Rainbow Hotel & Spa', 5, 154000))

user_prise = int(input())

filtered = [hotel for hotel in hotels if hotel.cost <= user_prise]
result = sorted(filtered, key=lambda hotel: hotel.cost, reverse=True)
if result:
    for hotel in result[:3]:
        print(hotel.name, hotel.star, hotel.cost)
else:
    print('вариантов нет')