word = input("Введите слово: ").lower()
letter_count = {}
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1
for letter, count in letter_count.items():
    if count == 2:
        print("Буква, встречающаяся дважды:", letter)
        break