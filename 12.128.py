word = input("Введите слово (оканчивается '_'): ")
k = int(input("k: "))
result = word[:k] + "т" + word[k:]
print(result)