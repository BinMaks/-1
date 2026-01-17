word = input("Введите слово: ")
length = len(word)
if length % 2 == 1:
    mid = length // 2
    result = word[:mid] + word[mid+1:]
else:
    mid1 = length // 2 - 1
    mid2 = length // 2
    result = word[:mid1] + word[mid2+1:]
print(result)