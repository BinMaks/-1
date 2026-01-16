arr = [int(x) for x in input("Введите элементы массива: ").split()]
greater_than_neighbors = sum(1 for i in range(1, len(arr) - 1) if arr[i] > arr[i-1] and arr[i] > arr[i+1])
print(f"Элементов, больших соседей: {greater_than_neighbors}")