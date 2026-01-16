
arr = list(map(float, input("Введите элементы массива: ").split()))
A = float(input("Введите число A: "))
first_elem = arr[0]
arr_a = [x * 2 for x in arr]
print(f"а) Увеличенные в 2 раза: {arr_a}")
arr_b = [x - A for x in arr]
print(f"б) Уменьшённые на {A}: {arr_b}")
arr_c = [x / first_elem for x in arr]
print(f"в) Разделенные на {first_elem}: {arr_c}")