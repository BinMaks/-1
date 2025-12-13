a, b = map(int, input("Прибытие поезда (часы минуты): ").split())
c, d = map(int, input("Отправление поезда (часы минуты): ").split())
n, m = map(int, input("Прибытие пассажира (часы минуты): ").split())
arrival_train = a * 60 + b
departure_train = c * 60 + d
arrival_passenger = n * 60 + m
if arrival_train <= arrival_passenger <= departure_train:
    print("Поезд будет стоять на платформе.")
else:
    print("Поезд не будет стоять на платформе.")