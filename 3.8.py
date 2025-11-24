seat_number = int(input("Введите номер места:"))
total_seats = 20*15
if seat_number < 1 or seat_number > total_seats:
    print("Ошибка: в зале всего 300 мест (с 1 по 300).")
else:
    row = (seat_number - 1) // 15+1
    print("Место находится в ряду:", row)