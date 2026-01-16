pages = list(map(int, input("Введите количество страниц в 100 книгах: ").split()))
max_pages = max(pages)
print(f"Самая толстая книга содержит {max_pages} страниц")