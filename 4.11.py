km_per_hour = float(input("Скорость в км/ч: "))
m_per_sec = float(input("Скорость в м/c: "))
km_per_hour_in_m_per_sec = km_per_hour * 0.2778
if km_per_hour_in_m_per_sec > m_per_sec:
    print("Скорость в км/ч больше. ")
elif km_per_hour_in_m_per_sec < m_per_sec:
    print("Скорость в м/с больше. ")
else:
    print("Скорости равны. ")

