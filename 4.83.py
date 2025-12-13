k = int(input("Введите количество грибов: "))
if 10 <= k % 100 <= 20:
    suffix = "грибов"
elif k % 10 == 1:
    suffix = "гриб"
elif 2 <= k % 10 <= 4:
    suffix = "гриба"
else:
    suffix = "грибов"
print(f"Мы нашли {k} {suffix} в лесу.")