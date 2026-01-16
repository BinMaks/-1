arr = [float(x) for x in input("Введите элементы вещественного массива: ").split()]
positives = sum(1 for x in arr if x > 0)
small_elements = sum(1 for x in arr if x <= 50.55)
print(f"Положительных элементов: {positives}, не превышает 5: {positives <= 5}")
print(f"Элементов ≤ 50.55: {small_elements}, кратно четырем: {small_elements % 4 == 0}")