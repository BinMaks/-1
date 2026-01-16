arr = [int(x) for x in input("Введите элементы массива: ").split()]
print(f"Сумма: {sum(arr)}")

from functools import reduce
import operator
arr = [int(x) for x in input("Введите элементы массива: ").split()]
product = reduce(operator.mul, arr, 1)
print(f"Произведение: {product}")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
print(f"Сумма квадратов: {sum(x**2 for x in arr)}")

arr = [int(x) for x in input("Введите элементы массива: ").split()]
print(f"Сумма первых шести: {sum(arr[:6])}")

arr = [int(x) for x in input("Введите элементы массива: ").split()]
k1 = int(input("k1: ")) - 1
k2 = int(input("k2: ")) - 1
if 0 <= k1 < k2 < len(arr):
    print(f"Сумма с {k1+1}-го по {k2+1}-й: {sum(arr[k1:k2+1])}")
else:
    print("Неверные индексы!")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
print(f"Среднее арифметическое: {sum(arr)/len(arr)}")


arr = [int(x) for x in input("Введите элементы массива: ").split()]
s1 = int(input("s1: ")) - 1
s2 = int(input("s2: ")) - 1
if 0 <= s1 < s2 < len(arr):
    avg = sum(arr[s1:s2+1]) / (s2 - s1 + 1)
    print(f"Среднее арифметическое: {avg}")
else:
    print("Неверные индексы!")