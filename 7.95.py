numbers = [int(input(f"Число {i+1}: ")) for i in range(int(input("Количество чисел: ")))]
sign_changes = 0
for i in range(1, len(numbers)):
    if (numbers[i-1] > 0 and numbers[i] < 0) or (numbers[i-1] < 0 and numbers[i] > 0):
        sign_changes += 1
print("Количество смен знака:", sign_changes)