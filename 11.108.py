arr = list(map(int, input("Введите ненулевые целые числа: ").split()))
sign_changes = 0
for i in range(1, len(arr)):
    if arr[i-1] * arr[i] < 0:
        sign_changes += 1
print(f"Количество смен знака: {sign_changes}")
