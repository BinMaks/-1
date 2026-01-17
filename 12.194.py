sentence1 = input("Введите первое предложение: ").split()
sentence2 = input("Введите второе предложение: ").split()
set1, set2 = set(sentence1), set(sentence2)
only_in_first = set1 - set2
only_in_second = set2 - set1
print("Слова только в первом предложении:", only_in_first)
print("Слова только во втором предложении:", only_in_second)