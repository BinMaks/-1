text = input("Введите предложение: ")
result = ""
for i, char in enumerate(text):
    if char != "о" or i % 2 == 0:
        result += char
print(result)