n = int(input("Введите число n (≤ 999999): "))
arr = [0] * 6
for i in range(6):
    arr[i] = n % 10
    n //= 10
print(arr)