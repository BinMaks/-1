sentence = input("Введите предложение: ")
words = sentence.split()
word_k = next((word for word in words if word.lower().startswith('к')), None)
if word_k:
    print("Слово, начинающееся на 'к':", word_k)
else:
    print("Слов, начинающихся на 'к', нет.")