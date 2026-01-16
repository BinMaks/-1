
income1 = list(map(float, input("Доход магазина 1 за февраль: ").split()))
income2 = list(map(float, input("Доход магазина 2 за февраль: ").split()))
total1 = sum(income1)
total2 = sum(income2)
if total1 < total2:
    print("Меньше доход у магазина 1: ", total1)
else:
    print("Меньше доход у магазина 2: ", total2)