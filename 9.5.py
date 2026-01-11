salaries = []
print("Введите зарплату для 12 работников за 3 месяца:")
for i in range(12):
    row = []
    for j in range(3):
        salary = float(input(f"Работник {i+1}, месяц {j+1}: "))
        row.append(salary)
    salaries.append(row)
total_salary = sum(sum(row) for row in salaries)
print(f"Общая сумма за квартал: {total_salary}")
print("Зарплата каждого работника за квартал:")
for i, row in enumerate(salaries, 1):
    quarterly_salary = sum(row)
    print(f"Работник {i}: {quarterly_salary}")
monthly_totals = [0, 0, 0]
for row in salaries:
    for j in range(3):
        monthly_totals[j] += row[j]
print("Общая зарплата за каждый месяц:")
for j, total in enumerate(monthly_totals, 1):
    print(f"Месяц {j}: {total}")