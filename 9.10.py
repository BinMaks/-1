results = []
print("Введите результаты для 10 спортсменов (по 5 видам спорта):")
for i in range(10):
    print(f"Спортсмен {i + 1}:")
    row = []
    for j in range(5):
        score = float(input(f"Вид спорта {j + 1}: "))
        row.append(score)
    results.append(row)
avg_results = []
for i, row in enumerate(results):
    avg = sum(row) / 5
    avg_results.append(avg)
    print(f"Среднее для спортсмена {i + 1}: {avg:.2f}")
total_sum = sum(sum(row) for row in results)
total_avg = total_sum / (10 * 5)
print(f"\nОбщее среднее по всем участникам: {total_avg:.2f}")
above_avg_count = sum(1 for avg in avg_results if avg > total_avg)
print(f"Спортсменов с результатом выше среднего: {above_avg_count}")
print("\nСпортсмены с результатом > 90:")
for i, row in enumerate(results):
    if any(score > 90 for score in row):
        print(f"Спортсмен {i + 1}")