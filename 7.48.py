total_pages = 0
while True:
    pages = int(input("Число страниц (0 — завершить): "))
    if pages == 0:
        break
    if pages > 16:  
        total_pages += pages
print("Общее число страниц в журналах:", total_pages)