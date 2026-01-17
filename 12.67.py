text = input("Введите текст: ")
sentences = text.count('.') + text.count('!') + text.count('?')
print("Количество предложений:", sentences)