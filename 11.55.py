masses = [float(x) for x in input("Введите массу 30 предметов: ").split()]
capacity = float(input("Введите грузоподъемность автомобиля: "))
total_mass = sum(masses)
if total_mass <= capacity:
    print("Общая масса не превышает грузоподъемность")
else:
    print("Общая масса превышает грузоподъемность")