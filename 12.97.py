sentence = input("Введите строку: ")
t, n = map(int, input("Введите номера символов t и n: ").split())
substring = sentence[t:n+1]
if substring == '666':
    print("Подстрока образует число 666")
else:
    print("Подстрока не образует число 666")