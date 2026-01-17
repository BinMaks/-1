city1 = input("Первый город: ")
city2 = input("Второй город: ")
city3 = input("Третий город: ")
cities = [city1, city2, city3]
longest = max(cities, key=len)
shortest = min(cities, key=len)
print(f"Самое длинное название: {longest}")
print(f"Самое короткое название: {shortest}")