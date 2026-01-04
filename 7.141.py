areas = [float(input(f"Площадь квадрата {i+1}: ")) for i in range(int(input("Количество квадратов: ")))]
max_area = max(areas)
side = max_area ** 0.5
diagonal = side * (2 ** 0.5)
print(f"Диагональ самого большого квадрата: {diagonal:.2f}")