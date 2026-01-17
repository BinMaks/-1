word = input("Введите слово: ")
k = int(input("Введите k: ")) - 1
s = int(input("Введите s: ")) - 1
part_to_reverse = word[k+1:s]
reversed_part = part_to_reverse[::-1]
result = word[:k+1] + reversed_part + word[s:]
print(result)