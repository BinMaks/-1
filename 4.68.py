minutes = int(input("Длительность разговора (мин): "))
day = input("День недели (пн,вт, ..., вс): ").lower()
if day in ["сб", "вс"]:
    cost_per_min = 1.5
else:
    cost_per_min = 2.0
total_cost = minutes * cost_per_min
print(f"Стоимость разговора: {total_cost:.2f} руб.")