y = [float(input()) for _ in range(15)]
n = float(input("n: "))


total = sum(y_i for y_i in y if y_i < n)
print("Сумма чисел < n:", total)


for i in range(14):
    if y[i] < n < y[i+1]:
        print(f"Элементы: {y[i]} (позиция {i+1}) и {y[i+1]} (позиция {i+2})")
        break