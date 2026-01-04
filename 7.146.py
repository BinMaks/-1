heights = list(map(float, input("Росты (через пробел): ").split()))
diff = max(heights) - min(heights)
print(f"Разница: {diff:.2f} см")