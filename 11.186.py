arr = list(map(int, input("12 элементов: ").split()))
result = []
for i in range(6):
    result.append(arr[i])
    result.append(arr[11 - i])
print(result)