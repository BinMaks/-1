n = int(input("Количество квартир: "))
residents = [int(input(f"Жильцов в квартире {i+1}: ")) for i in range(n)]
max_residents = max(residents)
max_apartment = len(residents) - residents[::-1].index(max_residents)
print(f"Квартира с наибольшим количеством жильцов: {max_apartment}")