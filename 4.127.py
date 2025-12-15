a, b, c = map(int, input("Введите три числа: ").split())
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c
if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c
if (a != max_num and a != min_num):
    mid_num = a
elif (b != max_num and b != min_num):
    mid_num = b
else:
    mid_num = c
print(f"Самое большое: {max_num}")
print(f"Самое маленькое: {min_num}")
print(f"Среднее: {mid_num}")