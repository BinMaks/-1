classes = list(map(int, input("Численность классов (через пробел): ").split()))
diff = max(classes) - min(classes)
print(f"Разница: {diff} учеников")