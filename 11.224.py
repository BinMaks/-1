championship1 = list(map(int, input("Мячи в 1-м чемпионате (26 игр): ").split()))
championship2 = list(map(int, input("Мячи во 2-м чемпионате (26 игр): ").split()))
total_goals = sum(championship1) + sum(championship2)
print("Общее количество мячей:", total_goals)