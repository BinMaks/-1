t = float(input("Время в минутах (t): "))
cycle = 5
green_time = 3
position = t % cycle
if position < green_time:
    print("Горит зеленый сигнал")
else:
    print("Горит красный сигнал")