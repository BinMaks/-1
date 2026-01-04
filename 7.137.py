distances = [float(input(f"Расстояние до города {i+1}: ")) for i in range(int(input("Количество городов: ")))]
max_distance = max(distances)
print(f"Самое удаленное расстояние: {max_distance}")