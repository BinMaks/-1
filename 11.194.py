scores = list(map(int, input("20 очков команд (убывание): ").split()))
p = int(input("Очки команды p: "))
place = 1
for s in scores:
    if p < s:
        place += 1
    else:
        break
print(f"Место команды: {place}")