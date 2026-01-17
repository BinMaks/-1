sentence = input("Введите предложение: ")
positions = [0, 1, 4, 5, 8, 9]  
for pos in positions:
    if pos < len(sentence):
        print(sentence[pos])