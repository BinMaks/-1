rate = float(input("Введите курс доллара к рублю: "))
print("Доллары | Рубли")
print("-! * 20")
for i in range(1, 21):
    rubles = i * rate
    print(f"{i:7} | {rubles:7.2f}")