a , b , c = map(float, input("введите три числа: ").split())
max_val = a if a > b else b
max_val = max_val if max_val > c else c
min_val = a if a < b else b
min_val = min_val if min_val < c else c
print(f"Наибольшее: {max_val}, наименьшее: {min_val}")