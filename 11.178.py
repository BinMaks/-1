arr = list(map(int, input("Введите элементы: ").split()))
s = int(input("Позиция s (1-{}): ".format(len(arr)))) - 1
k = int(input("Позиция k (1-{}): ".format(len(arr)))) - 1
if s < k:
    elem = arr.pop(s)
    arr.insert(k, elem)
print(arr)