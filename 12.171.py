word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()
from collections import Counter
count1 = Counter(word1)
count2 = Counter(word2)
result = []
for letter in set(word1 + word2):
    if count1[letter] == 1 and count2[letter] == 1:
        result.append(letter)
print("Буквы, встречающиеся в обоих словах только один раз:", ''.join(result))