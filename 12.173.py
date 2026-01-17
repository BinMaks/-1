words = [input(f"Введите {i+1}-е слово: ").lower() for i in range(3)]
from collections import Counter
all_letters = ''.join(words)
letter_count = Counter(all_letters)
result = [letter for letter in all_letters if letter_count[letter] == 1]
print("Буквы, встречающиеся только в одном слове (вар. 1):", ''.join(result))