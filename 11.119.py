scores = list(map(float, input("Введите 8 оценок судей: ").split()))
max_score = max(scores)
min_score = min(scores)
scores_filtered = [s for s in scores if s != max_score or scores.count(max_score) > 1]
scores_filtered = [s for s in scores_filtered if s != min_score or scores.count(min_score) > 1]
final_score = sum(scores_filtered) / len(scores_filtered)
print(f"Итоговая оценка: {final_score:.2f}")