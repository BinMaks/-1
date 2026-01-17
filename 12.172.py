word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()
from collections import Counter
count1 = Counter(word1)
count2 = Counter(word2)
can_form = all(count1[letter] >= count2[letter] for letter in count2)
print("Можно ли сформировать второе слово из букв первого (вар. 1):", can_form)