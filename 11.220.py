
arr = list(map(int, input("20 чисел: ").split()))
seen = set()
for num in arr:
    if num in seen:
        print("Повторяющийся элемент:", num)
        break
    seen.add(num)