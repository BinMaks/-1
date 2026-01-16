arr = list(map(int, input("Возрастающий массив: ").split()))
n = int(input("Число n: "))
for i, x in enumerate(arr):
    if x > n:
        print("Элементы после первого > n:", arr[i+1:])
        break
else:
    print("Нет элементов > n")