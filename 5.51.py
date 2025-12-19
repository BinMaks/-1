area = 100
yield_per_ha = 20
rate_area = 0.05
rate_yield = 0.02

print("Урожайность (ц/га):")
for year in range(2, 9):
    yield_per_ha *= 1 + rate_yield
    print(f"Год {year}: {yield_per_ha:.2f}")

print("\nПлощадь участка (га):")
for year in range(4, 8):
    area *= 1 + rate_area
    print(f"Год {year}: {area:.2f}")


total_harvest = 0
curr_area = 100
curr_yield = 20
for year in range(6):
    harvest = curr_area * curr_yield
    total_harvest += harvest
    curr_area *= 1 + rate_area
    curr_yield *= 1 + rate_yield
print(f"Общий урожай за 6 лет: {total_harvest:.2f} ц")