
a = list(map(int, input("Массив a: ").split()))
neg = [x for x in a if x < 0]
pos = [x for x in a if x >= 0]
b = neg + pos
print("Переставленный массив:", b)