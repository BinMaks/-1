residents = list(map(int, input("Введите количество жильцов на 15 этажах: ").split()))
res_with_index = [(res, i+1) for i, res in enumerate(residents)]
res_sorted = sorted(res_with_index)
print(f"Два этажа с наименьшим числом жильцов: {res_sorted[0][1]}")