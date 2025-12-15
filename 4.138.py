suit_num = int(input("Введите номер масти (1–4): "))
suits = ["пики", "трефы", "бубны", "червы"]
if 1 <= suit_num <= 4:
    print(f"Масть: {suits[suit_num - 1]}")
else:
    print("Некорректный номер масти")