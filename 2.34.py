v1 = float(input("Скорость первого автомобиля (км/ч): "))
v2 = float(input("Скорость второго автомобиля (км/ч): "))
s = float(input("Расстояние между автомобилями  (км): "))
v_sbl = v1+v2
t_hours = s/v_sbl
hours = int(t_hours)
minutes = round((t_hours-hours)*60)
print(f"\n Автомобили встретятся через {hours} часов {minutes} минут.")