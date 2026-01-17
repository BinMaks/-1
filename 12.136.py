word = input("Введите слово: ")
k = int(input("k: ")) - 1
first_letter = word[0]
result = word[1:k+1] + first_letter + word[k+1:]
print(result)