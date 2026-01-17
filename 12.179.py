sentence = input("Введите предложение: ")
words = sentence.split()
filtered_words = [word for word in words if word.lower() != "привет"]
print("Слова, отличные от 'привет':", ' '.join(filtered_words))