text = input("Введите строку: ")
result = text.replace("а", "X").replace("б", "а").replace("X", "б")
result = result.replace("А", "X").replace("Б", "А").replace("X", "Б")
print(result)