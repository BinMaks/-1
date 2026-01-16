dominoes = list(map(int, input("22 числа (кости домино): ").split()))
valid_a = True
for i in range(1, len(dominoes)):
    left = dominoes[i-1] % 10
    right = dominoes[i] // 10
    if left != right:
        valid_a = False
        break
print("Случай а) валиден:", valid_a)
valid_b = True
for i in range(1, len(dominoes)):
    digits1 = [dominoes[i-1] // 10, dominoes[i-1] % 10]
    digits2 = [dominoes[i] // 10, dominoes[i] % 10]
    if not (digits1[1] in digits2):
        valid_b = False
        break
print("Случай б) валиден:", valid_b)