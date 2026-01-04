dominoes = [int(input(f"Кость {i+1} (число 0–66): ")) for i in range(20)]
valid = True
for i in range(1, 20):
    left = dominoes[i-1] % 10
    right = dominoes[i] // 10
    if left != right:
        valid = False
        break
print("Последовательность корректна" if valid else "Последовательность некорректна")


dominoes = [int(input(f"Кость {i+1} (число 0–66): ")) for i in range(20)]
valid = True
for i in range(1, 20):
    prev = dominoes[i-1]
    curr = dominoes[i]
    if not ((prev % 10 == curr // 10) or (prev % 10 == curr % 10) or
            (prev // 10 == curr // 10) or (prev // 10 == curr % 10)):
        valid = False
        break
print("Последовательность корректна" if valid else "Последовательность некорректна")