weights = list(map(float, input("Введите веса людей: ").split()))
min_weight = min(weights)
max_weight = max(weights)
condition = (max_weight / min_weight) > 2
print(f"Вес самого тяжелого превышает вес самого легкого более чем в 2 раза: {condition}")