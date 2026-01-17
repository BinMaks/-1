sentence = input("Введите предложение: ")
for i in range(len(sentence) - 1):
    if sentence[i:i+2] == "нн":
        print("нн")