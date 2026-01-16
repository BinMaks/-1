arr = [int(x) for x in input("Введите элементы массива: ").split()]
print("Неотрицательные:", [x for x in arr if x >= 0])


print("≤ 100:", [x for x in arr if x <= 100])

