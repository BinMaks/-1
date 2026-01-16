
scores = [float(x) for x in input("Введите баллы спортсмена в 10 видах спорта: ").split()]
threshold = float(input("Введите пороговое значение баллов: "))
total_score = sum(scores)
if total_score > threshold:
    print("Спортсмен вышел в следующий этап")
else:
    print("Спортсмен не вышел в следующий этап")