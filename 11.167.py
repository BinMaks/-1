
arr = list(map(int, input("Введите элементы: ").split()))
num = int(input("Число для вставки: "))
for i, x in enumerate(arr):
    if x < 0:
        arr.insert(i+1, num)
        break
print(arr)


arr = list(map(int, input("Введите элементы: ").split()))
num = int(input("Число для вставки: "))
last_even_idx = -1
for i, x in enumerate(arr):
    if x % 2 == 0:
        last_even_idx = i
if last_even_idx != -1:
    arr.insert(last_even_idx, num)
print(arr)