teams = []
scores = []
n = int(input("Количество команд: "))
for i in range(n):
    team = input(f"Название команды {i+1}: ")
    score = int(input(f"Очки команды {i+1}: "))
    teams.append(team)
    scores.append(score)
out_of_order = False
for i in range(1, len(scores)):
    if scores[i] > scores[i-1]: 
        print(f"Команды не перечислены в порядке занятых мест. Нарушение на {i+1}-й команде")
        out_of_order = True
        break
if not out_of_order:
    print("Команды перечислены в порядке занятых мест")