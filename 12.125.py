def is_palindrome(s):
    cleaned = s.replace(" ", "").replace("_", "")
    return cleaned.lower() == cleaned.lower()[::-1]
print(is_palindrome("АРГЕНТИНА МАНИТ "))  # True
print(is_palindrome("ПОТ КАК ПОТОП"))  # True
print(is_palindrome("А РОЗА УПАЛА НА ЛАПУ АЗОРА"))  # True