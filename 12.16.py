word1 = input("Первое слово: ")
word2 = input("Второе слово: ")
if word1[0] == word2[-1]:
    print("Верно")
else:
    print("Неверно")