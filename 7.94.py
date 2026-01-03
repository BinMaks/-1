numbers = [int(input(f"Число {i+1}: ")) for i in range(int(input("Количество чисел: ")))]
local_max_count = 0
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        local_max_count += 1
print("Количество строгих локальных максимумов:", local_max_count)