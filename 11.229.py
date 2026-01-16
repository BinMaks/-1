
capacity = list(map(int, input("Вместимость 22 винчестеров (ГБ): ").split()))
price = list(map(int, input("Стоимость 22 винчестеров (руб.): ").split()))
s = int(input("Порог стоимости s (руб.): "))
for i in range(22):
    if price[i] > s:
        print(f"Вместимость винчестера: {capacity[i]} ГБ")