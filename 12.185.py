sentence = input("Введите предложение: ")
words = sentence.split()
longest_word = max(words, key=len)
is_long = len(longest_word) > 10
print("Самое длинное слово длиннее 10 символов:", is_long)