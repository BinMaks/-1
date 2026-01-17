sentence = input("Введите предложение: ")
words = sentence.split()
result_words = []
for word in words:
    word = word.replace('е', 'ё').replace('Е', 'Ё')
    word = word.replace('ы', '').replace('Ы', '')
    word = word.replace('и', 'й').replace('И', 'Й')
    word = word.replace('ъ', '').replace('Ъ', '')
    result_words.append(word)
print("Преобразованное предложение:", ' '.join(result_words))