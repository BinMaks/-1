arr = [int(x) for x in input("Введите элементы массива: ").split()]
even_positions = arr[1::2]
odd_positions = arr[0::2]
print("Четные позиции:", even_positions)
print("Нечетные позиции:", odd_positions)