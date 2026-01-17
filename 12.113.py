word = input("Введите 12-буквенное слово: ")
part_to_reverse = word[2:10]
reversed_part = part_to_reverse[::-1]
result = word[:2] + reversed_part + word[10:]
print(result)