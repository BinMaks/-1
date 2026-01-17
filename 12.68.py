sentence = input("Введите предложение: ")
vowels = "аеиоуыэюя"
count = 0
for char in sentence.lower():
    if char in vowels:
        count += 1
print("Количество гласных букв:", count)