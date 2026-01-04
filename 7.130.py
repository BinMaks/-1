sequence = [int(input(f"Число {i+1}: ")) for i in range(20)]
count = 0
for i in range(19):
    if sequence[i] == sequence[i+1]:
        count += 1
print(f"Количество повторений: {count}")