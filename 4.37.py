a = int(input("Число a:"))
b = int(input("Число b: "))
if b % a == 0:
    print(f"{a} - делитель {b}")
else:
    print(f"{a} не является делителем {b}")
if a % b == 0:
    print(f"{b} - делитель {a}")
else:
    print(f"{b} не является делителем {a}")