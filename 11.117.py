heights = list(map(float, input("Введите рост 25 человек: ").split()))
max_height = max(heights)
min_height = min(heights)
diff = max_height - min_height
print(f"Разница в росте: {diff:.2f} см")