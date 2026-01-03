
n = int(input("Количество домов: "))
residents = [int(input(f"Жителей в доме {i+1}: ")) for i in range(n)]
sum_odd_side = sum(residents[i] for i in range(0, n, 2))
sum_even_side = sum(residents[i] for i in range(1, n, 2))
if sum_odd_side > sum_even_side:
    print("Больше жителей на стороне с нечетными номерами домов.")
elif sum_even_side > sum_odd_side:
    print("Больше жителей на стороне с четными номерами домов.")
else:
    print("Количество жителей одинаково на обеих сторонах.")