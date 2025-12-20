n = int(input("Введите натуральное число: "))
cube = 0
current_odd = 1
for i in range(n):
    sum_of_odds = 0
    for _ in range(i + 1):
        sum_of_odds += current_odd
        current_odd += 2
    cube += sum_of_odds
print(f"Куб числа {n} равен {cube}")