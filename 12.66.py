text = input("Введите текст: ")
plus_count = text.count('+')
minus_count = text.count('-')
total = plus_count + minus_count
print("Всего символов '+' и '-':", total)