sentence = input("Введите предложение: ")
words = sentence.split()
same_start_end = [word for word in words if word[0].lower() == word[-1].lower()]
print("Слова, начинающиеся и оканчивающиеся на одну букву:", ' '.join(same_start_end))
three_e = [word for word in words if word.lower().count('е') == 3]
print("Слова с ровно тремя 'е':", ' '.join(three_e))
with_o = [word for word in words if 'о' in word.lower()]
print("Слова, содержащие 'о':", ' '.join(with_o))