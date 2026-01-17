sentence = input("Введите предложение: ").lower()
count_o = sentence.count('о')
count_a = sentence.count('а')
if count_o > count_a:
    print("Буква 'о' встречается чаще")
elif count_a > count_o:
    print("Буква 'а' встречается чаще")
else:
    print("Буквы 'о' и 'а' встречаются одинаковое количество раз")