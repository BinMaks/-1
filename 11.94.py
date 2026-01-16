heights = [float(x) for x in input("Рост учеников (отрицательные — мальчики): ").split()]
boys = [abs(h) for h in heights if h < 0]
girls = [h for h in heights if h >= 0]
avg_boys = sum(boys) / len(boys)
avg_girls = sum(girls) / len(girls)
if avg_boys - avg_girls > 10:
    print("Средний рост мальчиков > среднего роста девочек на >10 см")
else:
    print("Условие не выполняется")