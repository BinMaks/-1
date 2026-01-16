arr = list(map(int, input("Введите элементы массива: ").split()))
s = int(input("Позиция s: ")) - 1
k = int(input("Позиция k: ")) - 1
temp = arr[s]
for i in range(s, k, -1):
    arr[i] = arr[i - 1]
arr[k] = temp
print(arr)