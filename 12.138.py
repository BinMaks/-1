word = input("Введите слово: ")
s = int(input("s: ")) - 1
k = int(input("k: ")) - 1
letter = word[s]
result = word[:s] + word[s+1:k] + letter + word[k:]
print(result)