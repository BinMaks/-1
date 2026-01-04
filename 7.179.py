residents = [int(input(f"Жителей в квартире {i+1}: ")) for i in range(int(input("Количество квартир: ")))]
max_residents = max(residents)
max_apartment = residents.index(max_residents) + 1
print(f"Больше всего жильцов в квартире №{max_apartment} ({max_residents} человек)")