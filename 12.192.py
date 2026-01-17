sentence1 = input("Введите первое предложение: ").split()
sentence2 = set(input("Введите второе предложение: ").split())
for word in sentence1:
    if word in sentence2:
        print(f"Слово '{word}' входит во второе предложение.")
    else:
        print(f"Слово '{word}' не входит во второе предложение.")