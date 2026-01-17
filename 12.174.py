words = [input(f"Введите {i+1}-е слово: ").lower() for i in range(3)]
common_letters = set(words[0])
for word in words[1:]:
    common_letters &= set(word)
print("Общие буквы:", ''.join(sorted(common_letters)))