power = [int(input(f"Мощность двигателя модели {i+1} (л. с.): ")) for i in range(30)]
has_over_200 = any(p > 200 for p in power)
print("Есть модель с мощностью > 200 л. с." if has_over_200 else "Нет модели с мощностью > 200 л. с.")