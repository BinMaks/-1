results = [float(x) for x in input("Введите результаты 20 спортсменов: ").split()]
avg = sum(results) / len(results)
sum_above_avg = sum(r for r in results if r > avg)
count_below_avg = sum(1 for r in results if r < avg)
max_result = max(results)
print(f"Сумма результатов выше среднего: {sum_above_avg}")
print(f"Количество результатов ниже среднего: {count_below_avg}")
print(f"Максимальный результат: {max_result}")