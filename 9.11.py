salaries = []
print("Введите зарплату для 12 работников за 3 месяца:")
for i in range(12):
    print(f"Работник {i + 1}:")
    row = []
    for j in range(3):
        salary = float(input(f"Месяц {j + 1}: "))
        row.append(salary)
    salaries.append(row)
print("\nМесяц с наибольшей зарплатой для каждого работника:")
for i, row in enumerate(salaries, 1):
    max_month = row.index(max(row)) + 1
    print(f"Работник {i}: месяц {max_month}")
print("\nРаботник с наибольшей зарплатой за каждый месяц:")
for j in range(3):
    max_salary = max(salaries[i][j] for i in range(12))
    worker_index = [salaries[i][j] for i in range(12)].index(max_salary) + 1
    print(f"Месяц {j + 1}: работник {worker_index} (зарплата {max_salary})")