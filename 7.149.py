masses = list(map(float, input("Массы (через пробел): ").split()))
if max(masses) / min(masses) > 2:
    print("Да, превышает более чем в 2 раза")
else:
    print("Нет, не превышает")