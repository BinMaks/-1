boys = []
girls = []
n = int(input("Количество учеников: "))
for _ in range(n):
    height = float(input("Рост ученика: "))
    if height < 0:
        boys.append(abs(height))
    else:
        girls.append(height)
avg_boys = sum(boys) / len(boys)
avg_girls = sum(girls) / len(girls)
if avg_boys - avg_girls > 10:
    print("Да, средний рост мальчиков превышает средний рост девочек более чем на 10 см.")
else:
    print("Нет.")