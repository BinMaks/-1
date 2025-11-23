monitor_price = float(input("Стоимость монитора (руб.): "))
system_unit_price = float(input("Стоимость системного блока (руб.): "))
keyboard_price = float(input("Стоимость клавиатуры (руб.): "))
mouse_price = float(input("Стоимость мыши (руб.): "))
n = int(input("Сколько компьютеров нужно собрать? "))
one_pc_cost = monitor_price+system_unit_price+keyboard_price+mouse_price
total_cost = one_pc_cost*n
print(f"\n --- Результат ---")
print(f"Стоимость одного компьютера: {one_pc_cost: .2f} руб.")
print(f"Общая стоимость {n} компьютеров: {total_cost: .2f} руб.")
