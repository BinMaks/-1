sentence1 = input("Введите первое предложение: ").split()
sentence2 = set(input("Введите второе предложение: ").split())
unique_words = set(sentence1)
for word in unique_words:
    if word in sentence2:
        print(f"Слово '{word}' входит во второе предложение.")
    else:
        print(f"Слово '{word}' не входит во второе предложение.")