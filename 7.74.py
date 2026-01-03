
n = int(input("Количество троек: "))
count_triangles = 0
for _ in range(n):
    a, b, c = map(int, input("Введите a, b, c: ").split())
    if a + b > c and a + c > b and b + c > a:
        count_triangles += 1
print("Количество троек, образующих треугольник:", count_triangles)