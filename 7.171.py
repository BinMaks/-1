n = int(input("Количество чисел: "))
x = [int(input(f"x[{i+1}] = ")) for i in range(n)]


sorted_x = sorted(x, reverse=True)
max1, max2 = sorted_x[0], sorted_x[1]
print(f"а) Два максимальных элемента: {max1}, {max2}")


sorted_x = sorted(x)
min1, min2 = sorted_x[0], sorted_x[1]
print(f"б) Два минимальных элемента: {min1}, {min2}")