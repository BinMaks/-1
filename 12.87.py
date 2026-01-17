word1, word2 = input("Введите два слова через пробел: ").split()
count = 0
min_len = min(len(word1), len(word2))
for i in range(min_len):
    if word1[i] == word2[i]:
        count += 1
    else:
        break
print("Количество совпадающих начальных букв:", count)