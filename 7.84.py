a = [int(input(f"a[{i}]: ")) for i in range(10)]
positive_count = sum(1 for x in a if x > 0)
print("Количество положительных чисел не превышает 5" if positive_count <= 5 else "Количество положительных чисел превышает 5")