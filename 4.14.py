voltage1 = float(input("Напряжение на первом участке: "))
resistance1 = float(input("Сопротивление первого участка: "))
voltage2 = float(input("Напряжение на втором участке: "))
resistance2 = float(input("Сопротивление второго участка: "))
current1 = voltage1 / resistance1
current2 = voltage2 / resistance2
if current1 < current2:
    print("Меньший ток на первом участке. ")
elif current1 > current2:
    print("Меньший ток на втором участке. ")
else:
    print("Токи равны")