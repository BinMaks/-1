word = input("Введите слово: ")
t = int(input("Номер первой буквы (t): ")) - 1
n = int(input("Номер второй буквы (n): ")) - 1
word_list = list(word)
word_list[t], word_list[n] = word_list[n], word_list[t]
result = ''.join(word_list)
print(result)