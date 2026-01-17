word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()
letters_only_in_word1 = [letter for letter in word1 if letter not in word2]
letters_only_in_word2 = [letter for letter in word2 if letter not in word1]
result = letters_only_in_word1 + letters_only_in_word2
print("Буквы, которые есть только в одном из слов:", ''.join(result))