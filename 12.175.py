words = [input(f"Введите {i+1}-е слово: ") for i in range(3)]
all_letters = ''.join(words).lower()
letter_count = {}
for letter in all_letters:
    letter_count[letter] = letter_count.get(letter, 0) + 1
unique_letters = [letter for letter, count in letter_count.items() if count == 1]
print("Неповторяющиеся буквы:", ''.join(sorted(unique_letters)))