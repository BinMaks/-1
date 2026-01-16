arr = list(map(int, input("Введите элементы: ").split()))
n = int(input("Число n: "))
result = [arr[0]]
for i in range(1, len(arr)):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        result.append(n)
    result.append(arr[i])
print(result)