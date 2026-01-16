arr = list(map(int, input("Введите элементы: ").split()))
k = int(input("Позиция k (1-{}): ".format(len(arr)))) - 1
last = arr.pop()
arr.insert(k, last)
print(arr)