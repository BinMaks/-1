hour = int(input("введите час (0-23): "))
if 5 <= hour < 12:
    print("Утро")
elif 12 <= hour < 17:
    print("День")
elif 17 <= hour < 23:
    print("Вечер")
else:
    print("Ночь")