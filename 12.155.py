expression = input("Введите выражение (например, '3-5+7-2'): ")
parts = expression.split("-")
result = int(parts[0])
for part in parts[1:]:
    if "+" in part:
        add_parts = part.split("+")
        for add_part in add_parts:
            if add_part:
                result -= int(add_part)
    else:
        result -= int(part)
print("Результат:", result)