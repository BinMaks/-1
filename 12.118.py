word = input("Введите слово: ")
if 'о' in word:
    first_o = word.index('о')
    result = word[:first_o] + word[first_o+1:]
    print(result)
else:
    print("В слове нет буквы 'о'")


word = input("Введите слово: ")
if 'л' in word:
    last_l = word.rindex('л')
    result = word[:last_l] + word[last_l+1:]
    print(result)
else:
    print("В слове нет буквы 'л'")