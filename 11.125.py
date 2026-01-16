heights = list(map(float, input("Рост 35 человек: ").split()))
max_height = max(heights)
count = heights.count(max_height)
print(f"Человек с самым большим ростом: {count}")