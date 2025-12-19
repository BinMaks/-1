k = int(input("Введите k: "))
num, den = 1, 1  
if k == 1:
    print("1/1")
elif k == 2:
    print("2/1")
else:
    for _ in range(3, k + 1):
        num, den = num + den, den + num
    print(f"{num}/{den}")