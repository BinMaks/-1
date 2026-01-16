
precipitation = list(map(float, input("Осадки за каждый день (мм): ").split()))
temperature = list(map(float, input("Температура за каждый день (°C): ").split()))
snow = sum(precipitation[i] for i in range(len(precipitation)) if temperature[i] <= 0)
rain = sum(precipitation[i] for i in range(len(precipitation)) if temperature[i] > 0)
print("Осадки в виде снега: ", snow, "мм")
print("Осадки в виде дождя: ", rain, "мм")