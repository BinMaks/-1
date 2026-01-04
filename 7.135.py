n = int(input("Введите n: "))
numbers = [float(input(f"x{i+1}: ")) for i in range(15)]

max_val = min_val = numbers[0]
for num in numbers[1:]:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"Максимальное: {max_val}")
print(f"Минимальное: {min_val}")