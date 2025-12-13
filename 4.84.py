n = int(input("Введите стоимость в копейках (1–9999): "))
rubles = n // 100
kopecks = n % 100
if kopecks == 0:
    print(f"{rubles} рубль ровно")
else:
    print(f"{rubles} рублей {kopecks} копеек")