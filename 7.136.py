best_time = None
while True:
    time = float(input("Время спортсмена (или -1 для завершения): "))
    if time == -1:
        break
    if best_time is None or time < best_time:
        best_time = time
    print(f"Лучший результат на данный момент: {best_time}")