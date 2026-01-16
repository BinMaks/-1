
arr = list(map(int, input("Введите элементы: ").split()))
a = int(input("Число a: "))
insert_pos = 0
for x in arr:
    if '5' in str(x):
        insert_pos += 1
arr.insert(insert_pos, a)
print(arr)