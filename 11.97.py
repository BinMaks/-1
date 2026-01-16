heights = [float(x) for x in input("Рост 25 учеников: ").split()]
avg_height = sum(heights) / len(heights)
count = sum(1 for h in heights if h > avg_height)
print(f"Учеников с ростом > среднего: {count}")