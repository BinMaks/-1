
scores = [int(input()) for _ in range(20)]
N = int(input("Очки команды N: "))

place = 1
for s in scores:
    if N < s:
        place += 1
print("Место команды:", place)