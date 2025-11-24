seat_number = int(input("Введите номер места:"))
compartment_number = (seat_number - 1) // 4+1
print("Номер купе:", compartment_number)