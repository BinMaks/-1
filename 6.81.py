
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("Файл не найден")
        return 0

filename = input("Введите имя файла: ")
print("Количество строк в файле:", count_lines_in_file(filename))