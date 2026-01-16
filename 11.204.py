arr = list(map(int, input("Убывающий массив: ").split()))
a = int(input("Число a: "))
after_first_less = []
greater_than_a = [x for x in arr if x > a]
for i, x in enumerate(arr):
    if x < a:
        after_first_less = arr[i+1:]
        break
print("После первого < a:", after_first_less)
print("Все элементы > a:", greater_than_a)