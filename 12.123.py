word = input("Введите слово: ")
seen = set()
result = ""
for char in word:
    if char not in seen:
        result += char
        seen.add(char)
print(result)