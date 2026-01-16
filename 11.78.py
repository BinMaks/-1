arr = [int(x) for x in input("Введите элементы массива: ").split()]
even_count = sum(1 for x in arr if x % 2 == 0)
ends_with_5 = sum(1 for x in arr if str(x).endswith('5'))
print(f"Четных элементов: {even_count}, оканчивающихся на 5: {ends_with_5}")