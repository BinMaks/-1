scores = list(map(int, input("Очки команд: ").split()))
is_ordered = all(scores[i] >= scores[i+1] for i in range(len(scores) - 1))
if is_ordered:
    print("Команды перечислены в порядке занятых мест")
else:
    print("Команды не перечислены в порядке занятых мест")