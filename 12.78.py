sentence = input("Введите предложение (слова разделены одним пробелом): ")
words = sentence.split()
last_two = words[-2:]
print("Два последних слова:", last_two[0], last_two[1])