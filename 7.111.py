heights = []
n = int(input("Количество учеников: "))
for i in range(n):
    height = float(input(f"Рост ученика {i+1} (отрицательный для мальчиков): "))
    heights.append(height)
boys_heights = [h for h in heights if h < 0]
girls_heights = [h for h in heights if h >= 0]
avg_boys = sum(boys_heights) / len(boys_heights) if boys_heights else 0
avg_girls = sum(girls_heights) / len(girls_heights) if girls_heights else 0
print(f"Средний рост мальчиков: {-avg_boys} см")
print(f"Средний рост девочек: {avg_girls} см")