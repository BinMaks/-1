
s = [int(input(f"s[{i+1}] = ")) for i in range(12)]
max_val = max(s)
min_val = min(s)
max_count = s.count(max_val)
min_count = s.count(min_val)
print(f"Максимальное значение встречается {max_count} раз")
print(f"Минимальное значение встречается {min_count} раз")