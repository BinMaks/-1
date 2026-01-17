word = input("Введите 12-буквенное слово: ")
result = ""
for i in range(6):
    result += word[i] + word[11-i]
print(result)