arr = list(map(int, input("30 скоростей автомобилей: ").split()))
for i in range(29):
    if arr[i] > arr[i + 1]:
        arr[i:] = sorted(arr[i:])
        break
print(arr)