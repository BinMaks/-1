file_path = input("Введите полное имя файла (например, C:\\Windows\\System32\\calc.exe): ")
parts = file_path.split('\\')
for part in parts:
    print(part)