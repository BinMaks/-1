price_candy_per_kg=float(input("Введите стоимость 1 кг конфет (руб.): "))
price_cookies_per_kg=float(input("Введите стоимость 1 кг печенья (руб.): "))
price_apples_per_kg=float(input("Введите стоимость 1 кг яблок (руб.): "))
x=float(input("Сколько кг конфет купили ?"))
y=float(input("Сколько кг печенья купили? "))
z=float(input("Сколько кг яблок купили?"))
total_candy_cost=price_candy_per_kg*x
total_cookies_cost=price_cookies_per_kg*y
total_apples_cost=price_apples_per_kg*z
total_cost=total_candy_cost+total_cookies_cost+total_apples_cost
print(f"\n ---Чек---")
print(f"Конфеты: {x} кг * {price_candy_per_kg: .2f} руб. = {total_candy_cost: .2f} руб.")
print(f"Печенье: {y} кг * {price_cookies_per_kg: .2f} руб. = {total_cookies_cost: .2f} руб.")
print(f"Яблоки: {z} кг * {price_apples_per_kg: .2f} руб. = {total_apples_cost: .2f} руб.")
print(f"Итого: {total_cost: .2f} руб.")