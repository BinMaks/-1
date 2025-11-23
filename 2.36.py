celsius = float(input("Введите температуру по шкале Цельсия: "))
fahrenheit = celsius*1.8+32
kelvin = celsius + 273.15
print(f"\n ---- Результаты перевода ----")
print(f"Температура по Фаренгейту: {fahrenheit: .1f} F")
print(f"Температура по Кельвину: {kelvin: .2f} K")