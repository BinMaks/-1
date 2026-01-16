arr = [int(x) for x in input("Введите элементы массива: ").split()]
last_element = arr[-1]
count_diff = sum(1 for x in arr if x != last_element)  # а)
a = int(input("Введите число a: "))
count_multiple = sum(1 for x in arr if x % a == 0)  # б)
print(f"Количество элементов, отличных от последнего: {count_diff}")
print(f"Количество элементов, кратных {a}: {count_multiple}")