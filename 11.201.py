engines = [int(input(f"Мощность {i+1}-й модели: ")) for i in range(30)]
if any(power > 200 for power in engines):
    print("Есть модель с мощностью > 200 л. с.")
else:
    print("Нет моделей с мощностью > 200 л. с.")