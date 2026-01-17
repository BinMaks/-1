word = input("Введите слово: ")
try:
    first_a = word.index('а')
    last_o = word.rindex('о')
    word_list = list(word)
    word_list[first_a], word_list[last_o] = word_list[last_o], word_list[first_a]
    result = ''.join(word_list)
    print(result)
except ValueError:
    print("В слове нет 'а' или 'о'")