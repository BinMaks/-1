sentence = input("Введите предложение: ")
comma_positions = [i for i, char in enumerate(sentence) if char == ',']
if len(comma_positions) >= 2:
    start, end = comma_positions[0] + 1, comma_positions[1]
    print("Символы между первой и второй запятыми:", sentence[start:end])
elif len(comma_positions) == 1:
    print("Символы после единственной запятой:", sentence[comma_positions[0] + 1:])
else:
    print("Запятых в предложении нет")