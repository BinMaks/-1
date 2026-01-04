scores = list(map(float, input("Оценки судей (через пробел): ").split()))
scores.remove(max(scores))
scores.remove(min(scores))

avg_score = sum(scores) / len(scores)
print(f"Итоговая оценка: {avg_score:.2f}")