
arr = list(map(float, input("Введите элементы массива: ").split()))
B = float(input("Введите число B: "))
last_elem = arr[-1]
arr_a = [x - 20 for x in arr]
print(f"а) Уменьшённые на 20: {arr_a}")
arr_b = [x * last_elem for x in arr]
print(f"б) Умноженные на {last_elem}: {arr_b}")
arr_c = [x + B for x in arr]
print(f"в) Увеличенные на {B}: {arr_c}")