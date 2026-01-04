n = int(input("Количество покупателей: "))
service_times = [float(input(f"Время обслуживания {i+1}-го покупателя: ")) for i in range(n)]
waiting_times = [0] * n
for i in range(1, n):
    waiting_times[i] = waiting_times[i-1] + service_times[i-1]
min_waiting = min(waiting_times)
last_customer = len(waiting_times) - waiting_times[::-1].index(min_waiting)
print(f"Номер последнего покупателя с минимальным временем пребывания: {last_customer}")