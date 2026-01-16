arr = list(map(int, input("Введите элементы: ").split()))
k = int(input("Позиция k (1-{}): ".format(len(arr)))) - 1
first = arr.pop(0)
arr.insert(k, first)
print(arr)