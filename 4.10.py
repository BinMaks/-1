km = float(input("Введите расстояние в километрах: "))
feet = float(input("введите расстояние в футах: "))
feet_in_km = feet * 0.0003048
if km < feet_in_km:
    print("Расстояние в километрах меньше.")
elif km > feet_in_km:
    print("Расстояние в футах меньше.")
else:
    print("Расстояние равны")