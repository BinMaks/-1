word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()
unique_letters = set(word1)
for letter in unique_letters:
    if letter in word2:
        print(letter, "да")
    else:
        print(letter, "нет")