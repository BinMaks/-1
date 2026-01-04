scores = [int(input(f"Очки {i+1}-й команды: ")) for i in range(12)]

max_score = max(scores)
second_max_score = max(s for s in scores if s != max_score)

print(f"Очки команды, занявшей первое место: {max_score}")
print(f"Очки команды, занявшей второе место: {second_max_score}")