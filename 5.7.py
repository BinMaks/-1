price = 20.4
print("Количество штук | Стоимость (руб.)")
print("-! * 20")
for quantity in range(2, 21):
    total_cost = price * quantity
    print(f"{quantity:12} | {total_cost:15.2f}")