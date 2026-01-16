arr = list(map(int, input("Введите элементы: ").split()))
a = int(input("Число a: "))
num = int(input("Число для вставки: "))
result = []
for x in arr:
    if x % a == 0:
        result.append(num)
    result.append(x)
print(result)


arr = list(map(int, input("Введите элементы: ").split()))
num = int(input("Число для вставки: "))
last_neg_idx = -1
for i, x in enumerate(arr):
    if x < 0:
        last_neg_idx = i
if last_neg_idx == -1:
    arr.append(num)
else:
    arr.insert(last_neg_idx + 1, num)
print(arr)