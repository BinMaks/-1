sentence = input("Введите предложение: ")
if 'чу' in sentence or 'щу' in sentence:
    if 'чу' in sentence:
        pos = sentence.find('чу')
    else:
        pos = sentence.find('щу')
    print("Буквосочетание найдено, номер первой буквы:", pos + 1)
else:
    print("Буквосочетаний 'чу' или 'щу' нет")