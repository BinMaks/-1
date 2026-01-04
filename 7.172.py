results = [float(input(f"Результат {i+1}-го спортсмена: ")) for i in range(22)]
min_result = min(results)
second_min_result = min(r for r in results if r != min_result)
first_place_idx = results.index(min_result) + 1
second_place_idx = results.index(second_min_result) + 1
print(f"Первое место: спортсмен №{first_place_idx}, результат: {min_result}")
print(f"Второе место: спортсмен №{second_place_idx}, результат: {second_min_result}")