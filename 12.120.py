text = input("Введите предложение: ")
n1 = int(input("n1: ")) - 1
n2 = int(input("n2: ")) - 1
result = text[:n1] + text[n2+1:]
print(result)