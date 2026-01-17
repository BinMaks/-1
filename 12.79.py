sentence = input("Введите предложение (слова разделены одним пробелом): ")
words = sentence.split()
first_six = []
for i in range(min(6, len(words))):
    first_six.append(words[i])
print("Первые 6 слов:", first_six)