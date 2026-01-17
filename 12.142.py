word = input("Введите слово: ")
k = int(input("k: ")) - 1
last_letter = word[-1]
result = word[:-1]
result = result[:k] + last_letter + result[k:]
print(result)