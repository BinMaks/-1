word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()
for letter in word1:
    if letter in word2:
        print(letter, "да")
    else:
        print(letter, "нет")