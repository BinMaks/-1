
arr = list(map(int, input("Элементы массива: ").split()))
first_elem = arr[0]
count = 0
for elem in arr:
    if elem == first_elem:
        count += 1
    else:
        break
print(f"Количество равных элементов: {count}")
print(f"Элементы после них: {arr[count:]}")