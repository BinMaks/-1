word = input("Введите слово из четного числа букв: ")
result = ""
for i in range(0, len(word), 2):
    if i + 1 < len(word):
        result += word[i + 1] + word[i]
print(result)