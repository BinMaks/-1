books = [int(x) for x in input("Введите численность книг в 35 разделах: ").split()]
total_books = sum(books)
if 100000 <= total_books <= 999999:
    print("Общее число книг — шестизначное число")
else:
    print("Общее число книг не является шестизначным числом")