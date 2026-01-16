arr = list(map(int, input("Элементы списка: ").split()))
n = len(arr)
arr = [arr[n-1]] + arr[:n-1]
print(arr)